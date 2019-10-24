import youtube_dl
import pydub


def displayBanner():

    print(r"""
  _____    _______    _          
 |  __ \  |__   __|  | |         
 | |__) |   _| |_   _| |__   ___ 
 |  ___/ | | | | | | | '_ \ / _ \
 | |   | |_| | | |_| | |_) |  __/
 |_|    \__, |_|\__,_|_.__/ \___|
         __/ |                   
        |___/                    

    """)

    return






# --------------------------------------------------------------------------------

def downloadSingleMusic(path, url, outFormat):

    yDownloader = youtube_dl.YoutubeDL()


    yDownloaderOptions = {

            'verbose': False,
            'quiet': False,
            'fixup': 'detect_or_warn',                      # Automatically correct known faults of the file.
            'format': 'bestaudio/best',                     # choice of quality
            'extractaudio' : True,                          # only keep the audio
            'outtmpl': path,                                # name the file the title of the video
            'noplaylist' : True,                            # only download single song, not playlist

            'postprocessors': [{                            # Define postprocessors options
                'key': 'FFmpegExtractAudio',                # Which engine to perform postprocessors actions                
                'preferredcodec': outFormat,                # Output codec
                'preferredquality': '320',                  # Which quality in bitrate
                }],
        }

    try:

        with youtube_dl.YoutubeDL(yDownloaderOptions) as yDownloader:
            yDownloader.download([url])

    except youtube_dl.DownloadError as e:
        print("[!] An error occured during downloading video : ")
        print(e)
        exit()

    return

# --------------------------------------------------------------------------------

def getInfo(url):
# Function to get info about a video, given by URL

    # Define options to set quiet mode
    getInfoOptions = {'quiet': True, 'verbose':False}

    # Initilize Youtube Downloader
    yDownloader = youtube_dl.YoutubeDL(getInfoOptions)

    # Initialize a list, which contains ID and video title
    infoList = []

    try:
        # Get info
        yMetaData = yDownloader.extract_info(url, download=False)
    except youtube_dl.DownloadError as e:
        # Catch errors ?
        print("[!] An error occured during get video info : ")
        print(e)
        exit()

    # Append info to list
    infoList.append(yMetaData['id'])
    infoList.append(yMetaData['title'])

    return infoList


# ------------------------------------------------------------------
# ------------------------------ Main ------------------------------
# ------------------------------------------------------------------


displayBanner()

url = r'https://www.youtube.com/watch?v=fEqrt6nZTS4'


info = getInfo(url)

outputFolder = r'/home/scratch/Downloads'
tempName = f"Temp_{info[0]}.webm"
musicFullPath = f"{outputFolder}/{tempName}"

# Can be mp3/flac/aac/wav
outFormat = 'wav'

downloadSingleMusic(musicFullPath,url,outFormat)

# Sources

# https://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas
# https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php
# https://github.com/ytdl-org/youtube-dl
# https://spapas.github.io/2018/03/06/easy-youtube-mp3-downloading/
# https://github.com/ytdl-org/youtube-dl/issues/10328



# https://pythonbasics.org/convert-mp3-to-wav/


# Postprocessors ? 
# https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/postprocessor/ffmpeg.py