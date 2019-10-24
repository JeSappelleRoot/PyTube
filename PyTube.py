import youtube_dl

url = r'https://www.youtube.com/watch?v=fEqrt6nZTS4'

yDownloader = youtube_dl.YoutubeDL()


try:
    yMetaData = yDownloader.extract_info(url,download=False, verbose=False)
except youtube_dl.DownloadError as e:
    print("[!] An error occured during get video info : ")
    print(e)



videoTitle = yMetaData['title']

extension = 'ogg'
output = r'/home/scratch/Downloads'


mp3Options = {

        'verbose': False,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'format': 'bestaudio/best', # choice of quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
        'extractaudio' : True,      # only keep the audio
        'audioformat' : "mp3",      # convert to mp3 
        'outtmpl': f"{output}/{videoTitle}.webm",     # name the file the title of the video
        'noplaylist' : True,        # only download single song, not playlist
    }


try:

    with youtube_dl.YoutubeDL(mp3Options) as yDownloader:
        yDownloader.download([url])

except youtube_dl.DownloadError as e:
    print("[!] An error occured during downloading video : ")
    print(e)




# Sources

# https://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas
# https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php
# https://github.com/ytdl-org/youtube-dl
# https://spapas.github.io/2018/03/06/easy-youtube-mp3-downloading/
# https://github.com/ytdl-org/youtube-dl/issues/10328