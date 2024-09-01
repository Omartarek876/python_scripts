import yt_dlp

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/1xsDmAYVlrs?si=ZvWN1RKA6-l2KAag'])  # paste the url of the video you want to download 
