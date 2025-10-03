import instaloader
import urllib.parse
import contextlib, os

class InstaParse:
    def __init__(self, url):
        self.url = url
        self.L = instaloader.Instaloader()

    def _shortcode(self):
        self.path = urllib.parse.urlparse(self.url).path
        self.parts = [p for p in self.path.split("/") if p]
        if not self.parts:
            return {
                'status': 'error',
                'message': ValueError("Не удалось извлечь shortcode")
                }
        return self.parts[-1]

    def getURL(self):
        self.shortcode = self._shortcode()

        # отключаем лишний вывод instaloader
        with open(os.devnull, "w") as devnull:
            with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                try:
                    self.post = instaloader.Post.from_shortcode(self.L.context, self.shortcode)
                except instaloader.exceptions.LoginRequiredException:
                    return {
                        'status': 'error',
                        'message': "❗ Нужно залогиниться (Instagram требует авторизацию)"
                        }
                except instaloader.exceptions.InstaloaderException as e:
                    # сюда попадают 403 по другим причинам (лимиты, блок, неверный url и т.п.)
                    return {
                        'status': 'error',
                        'message': f"Ошибка Instagram: {e}"
                        }
                except Exception as e:
                    return {
                        'status': 'error',
                        'message': f"Неожиданная ошибка: {e}"
                        }

        # если получили пост — возвращаем ссылку
        if self.post.is_video:
            return {
                'status': 'success',
                'message': self.post.video_url
                }
        return {
            'status': 'success',
            'message': self.post.url
            }


# Пример использования
# url = ""
# parser = InstaParse(url)
# print(parser.getURL())