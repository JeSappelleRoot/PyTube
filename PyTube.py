import youtube_dl
import pydub
import argparse
from termcolor import colored

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

def downloadMusic(path, url, outFormat, name, q, v):
# Function to download a single audio file from Youtube URL

    # Define a downloader
    yDownloader = youtube_dl.YoutubeDL()

    # Define options for youtube downloader
    singleURLOptions = {

            'verbose': v,
            'quiet': q,
            'fixup': 'detect_or_warn',                      # Automatically correct known faults of the file.
            'format': 'bestaudio/best',                     # choice of quality
            'extractaudio' : True,                          # only keep the audio
            'outtmpl': path,                                # name the file the title of the video
            'noplaylist' : False,                            # only download single song, not playlist

            'postprocessors': [{                            # Define postprocessors options
                'key': 'FFmpegExtractAudio',                # Which engine to perform postprocessors actions                
                'preferredcodec': outFormat,                # Output codec
                'preferredquality': '320',                  # Which quality in bitrate
                }],
        }

    print(colored(f"[+] Downloading music from {name}",'yellow'))
    # Try/Except to avoid downloading error
    try:
        # With statement to download 
        with youtube_dl.YoutubeDL(singleURLOptions) as yDownloader:
            yDownloader.download([url])

    except youtube_dl.DownloadError as e:
        print(colored("[!] An error occured during downloading video : ",'red'))
        print(e)
        exit()

    print(colored("[+] Downloaded successfully\n",'green'))


    return

# --------------------------------------------------------------------------------

def getInfo(url):
# Function to get info about a video, given by URL

    # Define options to set quiet mode
    getInfoOptions = {
                        'quiet': True,
                        'verbose':False,
                        'fixup': 'detect_or_warn',                        
                        }

    # Initilize Youtube Downloader
    yDownloader = youtube_dl.YoutubeDL(getInfoOptions)

    # Initialize a list, which contains ID and video title
    infoList = []

    try:
        # Get info
        yMetaData = yDownloader.extract_info(url, download=False)


    except youtube_dl.DownloadError as e:
        # Catch errors ?
        print(colored("[!] An error occured during get video info : ",'red'))
        print(e)
        exit()

    # Append info to list
    infoList.append(yMetaData['id'])
    infoList.append(yMetaData['title'])


    return infoList


# ------------------------------------------------------------------
# ------------------------------ Main ------------------------------
# ------------------------------------------------------------------


# Sources

# https://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas
# https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php
# https://github.com/ytdl-org/youtube-dl
# https://spapas.github.io/2018/03/06/easy-youtube-mp3-downloading/
# https://github.com/ytdl-org/youtube-dl/issues/10328

# https://pythonbasics.org/convert-mp3-to-wav/

# Postprocessors options 
# https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/postprocessor/ffmpeg.py



displayBanner()

# Single music url
singleURL = r'https://www.youtube.com/watch?v=fEqrt6nZTS4'

# Playlis url
playlistURL = r'https://www.youtube.com/watch?v=IVJ3aRQso9k'

info = getInfo(singleURL)

outputFolder = r'/home/scratch/Downloads'
videoName = info[1]
tempName = f"{videoName}.webm"
musicFullPath = f"{outputFolder}/{tempName}"

q = True
v = False

# Can be mp3/flac/aac/wav
outFormat = 'mp3'

downloadMusic(musicFullPath, singleURL, outFormat, videoName, q, v)


#getInfo(playlistURL)