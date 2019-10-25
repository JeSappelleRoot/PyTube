# PyTube

PyTube is an implementation of the great Youtube_dl library


## Requirements

PyTube use several libraries : 
- **sys** for some checks  
- **argparse** to parse arguments in command line  
- **requests** to get links of videos in a playlist
- **youtube_dl** to download music from video  
- **os** with **path** to check if folder or file exist  
- **termcolor** to add color in your boring terminal  
- **BeautifulSoup** to parse requests module results


## Requirement file

```
argparse==1.2.1
requests==2.21.0
youtube_dl==2019.9.28
termcolor==1.1.0
beautifulsoup4==4.8.0
```

Just run `pip3 install -r requirements.txt` to install all modules needed by PyTube

# Sources and ideas

* Official documentation of Youtube_dl module  
 https://github.com/ytdl-org/youtube-dl

* The best source I used to make PyTube  
 https://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas

* Get information about a video   
 https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php

 * Availables options for download process and postprocess  
 https://github.com/ytdl-org/youtube-dl/issues/10328

 * Postprocess avalaibles codecs and formats  
 https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/postprocessor/ffmpeg.py

 * Retrieve video links from a Youtube playlist  
 https://www.geeksforgeeks.org/python-program-to-download-complete-youtube-playlist/


# Download music from Youtube

PyTube takes several arguments in command line : 
- `--mode` : single, playlist or file, to specify how use PyTube script  
  - `single` mode allow to download a single music, from an URL or a video ID
  - `playlist` mode allow to download all music from a Youtube playlist
  - `file` mode allow to download URL or ID from a text file
- `--url` specify the Youtube video URL
- `--id` specify the Youtube video ID
- `--file` specify the file where are stored URL or ID to download
- `--output` is used to specify the output folder where music will be downloaded
- `--name` can be use to specify a name of downloaded music
- `--format` can specify the music format (mp3, aac, flac or wav only)
- `-v` to increase verbosity of PyTube (maximum is `-vv`)

