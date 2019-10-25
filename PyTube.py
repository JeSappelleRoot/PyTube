import sys
import pydub
import argparse
import requests
import youtube_dl
from os import path
from termcolor import colored
from bs4 import BeautifulSoup

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

def downloadMusic(path, targetVideo, outFormat, name, quiet, verbose):
# Function to download a single audio file from Youtube URL

    # Define a downloader
    yDownloader = youtube_dl.YoutubeDL()

    # Define options for youtube downloader
    singleLOptions = {

            'verbose': verbose,
            'quiet': quiet,
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


    print(colored(f"[+] Downloading music from {targetVideo}",'yellow'))
    # Try/Except to avoid downloading error
    try:
        # With statement to download 
        with youtube_dl.YoutubeDL(singleLOptions) as yDownloader:
            yDownloader.download([targetVideo])

    except youtube_dl.DownloadError:
        # Youtube-DL provide his own error message if the video is unvalaible/country blocked
        exit()

    print(colored("[+] Downloaded successfully\n",'green'))


    return

# --------------------------------------------------------------------------------

def getInfo(url,quiet,verbose):
# Function to get info about a video, given by URL

    # Define options to set quiet mode
    getInfoOptions = {
                        'quiet': quiet,
                        'verbose':verbose,
                        'fixup': 'detect_or_warn', 
                        'ignoreerrors': True                       
                        }

    # Initilize Youtube Downloader
    yDownloader = youtube_dl.YoutubeDL(getInfoOptions)

    # Initialize a list, which contains ID and video title
    infoList = []

    try:
        # Get info
        yMetaData = yDownloader.extract_info(url, download=False)


    except youtube_dl.DownloadError:
        # Youtube-DL provide his own error message if the video is unvalaible/country blocked
        exit()

    # Append info to list
    infoList.append(yMetaData['id'])
    infoList.append(yMetaData['title'])

    return infoList    

# --------------------------------------------------------------------------------

def getPlaylistInfos(target):
# Function to retrieve links of videos in playlist

    print(colored('[+] Retrieve ID of videos in the playlist','yellow'))

    # Make a request to get HTML document
    request = requests.get(target)
    # Parse previous request in BeautifulSoup with html parser
    ySoup = BeautifulSoup(request.content, 'html.parser')

    rawLinks = []
    # Loop on the content to get the good class in <a> labels
    for link in ySoup.findAll('a', attrs={'class': 'spf-link playlist-video clearfix yt-uix-sessionlink spf-link'}):
        rawLinks.append(link.get('href'))

    # Clean rawLinks
    # /watch?vOAhCfI5hLjU&listPLwPd55WyRFm-qt3k8Gh9QS-DHSrY0z5SB&index1
    # Split on '=' give ['/watch?v', 'OAhCfI5hLjU&list', 'PLwPd55WyRFm-qt3k8Gh9QS-DHSrY0z5SB&index', '1']
    # index [1] give 'OAhCfI5hLjU&list'
    # Split on '&' give ['OAhCfI5hLjU', 'list']
    # Get video ID with index [0]

    # Same process to get index of video

    # Initiate a dict to contain index of video and ID
    videosID = {}

    for link in rawLinks:
        idVideo = (link.split('=')[1]).split('&')[0]            # Get Youtube video ID
        indexVideo= (link.split('&')[-1]).split('=')[-1]        # Get Youtube video index in the playlist

        videosID[indexVideo] = idVideo                          # Add entry in dict

    

    return videosID



# ------------------------------------------------------------------
# ------------------------------ Main ------------------------------
# ------------------------------------------------------------------

# Define an argument parser
parser = argparse.ArgumentParser(
formatter_class=argparse.RawDescriptionHelpFormatter,
)

# Add a exclusive group to make conflicts between args
target = parser.add_mutually_exclusive_group()

parser.add_argument('--mode', help='Specifiy the mode to use [url/playlist/file]', choices=['single','playlist','file'], required=True)
target.add_argument('--url', help='Get music from this url, only for URL and playlist mode')
target.add_argument('--id', help='Get music from this Youtube video ID (only for URL and playlist mode)')
target.add_argument('--file', help='File which contain URL and formats (separated by space)')
parser.add_argument('--output', help='Specify the folder where music will be saved', required=True)
parser.add_argument('--name', help='Specify the name (without extension) of the audio file, else PyTube will used the video name instead')
parser.add_argument('--format', help='Specify format of the audio file [mp3/acc/flac/wav] (Default is mp3)', default='mp3',choices=['mp3','aac','flac','wav'])
parser.add_argument('-v', help='Increase verbosity to debug video downloading (repeat -v to increase verbosity)', default=0, action='count')

displayBanner()


# Parse arguments
args = parser.parse_args()      

# Parse mode
mode = args.mode
# If mode is single url
if mode == 'single':
    # If full URL is specified
    if args.url:
        # target will be the URL
        target = args.url
    # else if ID is specified    
    elif args.id:
        # target will be the video ID
        target = args.id
    # else target variable is None
    else:
        print(colored('[!] A URL or and ID must be specified in single mode','red'))
        exit()

# If mode is playlist
elif mode == 'playlist':
    # If a name is gived in argument, playlist mode choose names of audio files
    if args.name:
        print(colored('[!] Playlist mode only allow automatic name','red'))
        print(colored('[!] Please remove --name argument','red'))
        exit()
    # If a playlist ID is given, only URL is allowed    
    if args.id:
        print(colored('[!] Playlist mode only allow URL','red'))
        print(colored('[!] Please specify url with --url instead --id','red'))
        exit()
    # Only URL for the target, no ID
    if args.url:
        target = args.url
    # Else target variable is None    
    else:
        print(colored('[!] A URL must be specified in playlist mode','red'))
        exit()


# If mode is file mode
elif mode == 'file':
    # If a name is gived in argument, playlist mode choose names of audio files
    if args.name:
        print(colored('[!] File mode only allow automatic name','red'))
        print(colored('[!] Please remove --name argument','red'))
        exit()
    # If an ID is given, only file is allowed    
    if args.id:
        print(colored('[!] File mode only allow file','red'))
        print(colored('[!] Please specify file with --file instead --id','red'))
        exit()
    # If an URL is given, only file is allowed
    if args.url:
        print(colored('[!] File mode only allow file','red'))
        print(colored('[!] Please specify file with --file instead --url','red'))
        exit()
    # If file argument is None
    if args.file is None:
        print(colored("[!] File mode needs a file",'red'))
        print(colored('[!] Please specify a file with --file argument','red'))
        exit()
    # Else if the file specified doesn't exist
    elif not path.isfile(args.file):
        print(colored("Input file does'nt exist : ",'red'))
        print(colored(args.file,'red'))
        exit()
    # Else if the file exist, assign argument to target
    elif path.isfile(args.file):
        target = args.file



outputFolder = args.output      # Parse output folder
outFormat = args.format         # Parse output audio file format

# Parse verbose argument (0 by default) and define different case
verbose = args.v 
if verbose == 0:
    quiet, verbose = True, False
elif verbose == 1:
    quiet, verbose = False, False
elif verbose > 1:
    quiet, verbose = False, True

# Parse name if specified
if args.name:
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

# Retrieve playlist URL songs
# https://www.geeksforgeeks.org/python-program-to-download-complete-youtube-playlist/


#
# ------------------------------- Single mode -------------------------------
#


if mode == 'single':

    # If videoName variable doesn't exist
    if 'videoName' not in locals(): 
        # Get info if the name is not set by the user
        # Use the video name instead
        info = getInfo(target, quiet, verbose)
        videoName = info[1]
        # Display auto detected name
        print(colored(f'[+] Video name auto-detected : {videoName}','green'))

    # Define a temporary name, before final conversion
    tempName = f"{videoName}.webm"
    # Fullpath of the audio file
    musicFullPath = f"{outputFolder}/{tempName}"

    # Download a single music
    downloadMusic(musicFullPath, target, outFormat, videoName, quiet, verbose)





#
# ------------------------------- Playlist mode -------------------------------
#


elif mode == 'playlist':

    # Get ID and index of videos in the playlist
    playlistInfo = getPlaylistInfos(target)

    # If the returned dict is empty
    if len(playlistInfo) == 0:
        print(colored('[!] Failed to retrieve videos of the playlist','red'))
    # Else
    else:
        print(colored('[+] Videos ID successfully retrieves\n','green'))
        # Extract ID and index from the dict to download
        for videoInfo in playlistInfo.items():
            target = videoInfo[1]
            videoIndex = videoInfo[0]
            # If videoIndex is between 1-9, add a 0 at the begining
            if len(videoIndex) == 1:
                videoIndex = f"0{videoIndex}"
            # Get info of the video with the ID
            info = getInfo(target, quiet, verbose)
            videoName = info[1]
            # Display auto detected name
            print(colored(f'[+] Video name auto-detected : {videoName}','green'))

            # Define a temporary name, before final conversion
            tempName = f"{videoIndex}_{videoName}.webm"
            videoName = f"{videoIndex}_{videoName}"
            # Fullpath of the audio file
            musicFullPath = f"{outputFolder}/{tempName}"
            
            # Finally download each music in the playlist 
            downloadMusic(musicFullPath, target, outFormat, videoName, quiet, verbose)





#
# ------------------------------- File mode -------------------------------
#

elif mode == 'file':











