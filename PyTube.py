import sys
import pydub
import argparse
import youtube_dl
from os import path
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

# Define an argument parser
parser = argparse.ArgumentParser(
formatter_class=argparse.RawDescriptionHelpFormatter,
)

# Add a exclusive group to make conflicts between args
target = parser.add_mutually_exclusive_group()

parser.add_argument('--mode', help='Specifiy the mode to use [url/playlist/file]', choices=['url','playlist','file'])
target.add_argument('--url', help='Get music from this url, only for URL and playlist mode')
target.add_argument('--id', help='Get music from this Youtube video ID (only for URL and playlist mode)')
target.add_argument('--file', help='File which contain URL')
parser.add_argument('--output', help='Specify the folder where music will be saved', required=True)
parser.add_argument('--name', help='Specify the name (without extension) of the audio file, else PyTube will used the video name instead')
parser.add_argument('--format', help='Specify format of the audio file [mp3/acc/flac/wav] (Default is mp3)', default='mp3',choices=['mp3','aac','flac','wav'])
parser.add_argument('-v', help='Increase verbosity to debug video downloading (repeat -v to increase verbosity)', default=0, action='count')

displayBanner()


# Parse arguments
args = parser.parse_args()      

mode = args.mode                            # Parse mode
if mode == 'url' or mode == 'playlist':     # If mode a single url
    if args.url:                            # If full URL is specified
        target = args.url                   # target will be the URL
    elif args.id:                           # else if ID is specified
        target = args.id                    # target will be the video ID
    else:                                   # else target variable is None
        target = None

outputFolder = args.output      # Parse output folder
outFormat = args.format         # Parse output audio file format
verbose = args.v                # Parse verbose argument (0 by default)
if args.name:                   # Parse name if specified
    videoName = args.name

# If less than 2 arguments
# Print help section and quit
if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    exit()

# Test if output folder exist
if not path.isdir(outputFolder):
    print(colored("Output folder does'nt exist",'red'))
    print(colored(outputFolder,'red'))
    exit()



# Sources

# https://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas
# https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php
# https://github.com/ytdl-org/youtube-dl
# https://spapas.github.io/2018/03/06/easy-youtube-mp3-downloading/
# https://github.com/ytdl-org/youtube-dl/issues/10328

# https://pythonbasics.org/convert-mp3-to-wav/

# Postprocessors options 
# https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/postprocessor/ffmpeg.py


# Single music url
singleURL = r'https://www.youtube.com/watch?v=fEqrt6nZTS4'

# Playlis url
playlistURL = r'https://www.youtube.com/watch?v=IVJ3aRQso9k'


if 'videoName' not in locals(): 
    info = getInfo(singleURL)
    videoName = info[1]

tempName = f"{videoName}.webm"
musicFullPath = f"{outputFolder}/{tempName}"

print(target)

if mode == 'url' and target:
    downloadMusic(musicFullPath, target, outFormat, videoName, q, v)
else:
    print(colored('[!] A URL or and ID must be specified in url mode','red'))
    exit()


#getInfo(playlistURL)