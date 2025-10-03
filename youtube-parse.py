from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {
    'skip_download': True,       # не качать файл
    'quiet': True,               # не спамить в консоль
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)  # получаем метаданные
    print("Заголовок:", info['title'])
    print("Видео URL:", info['url'])  # прямой потоковый URL
