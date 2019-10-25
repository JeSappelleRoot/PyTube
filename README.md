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
- `--name` can be use to specify a name of downloaded music (**by default, PyTube use the video name to named the audio file**)
- `--format` can specify the music format with mp3, aac, flac or wav only (**default is mp3**)
- `-v` to increase verbosity of PyTube (maximum is `-vv`)
  - First level of verbosity `-v` add download information (e.g progress bar) 
  - Last level of verbosity `-vv` add debug information about youtube_dl module

## Command line conflicts

Some arguments are incompatibles : 
- Only one mode at a time
- with `--mode single`, you can only use `--id` or `--url` to specify the targeted video
- with `--mode playlist`, you have to specify entire Youtube video link (see bellow)
- with `--mode file`, the argument `--format` will be use for each audio file
- with `--mode playlist` and `--mode file`, **you can't specify a name for audio files**, PyTube will choose and assign automatically names (based on video title)


## Single mode download

Single mode is the easiest way to download music with PyTube.  
With `--format` argument, audio file will be in MP3 format 

You can use a full URL with `--url `like `https://www.youtube.com/watch?v=rZUppxT38Zk` or just the Youtube video ID with `--id`, here `rZUppxT38Zk` (part after `watch?v=` section)


### Some examples

* `python3 PyTube.py --mode single --url https://www.youtube.com/watch\?v\=rZUppxT38Zk --output ~/Downloads`


```

  _____    _______    _          
 |  __ \  |__   __|  | |         
 | |__) |   _| |_   _| |__   ___ 
 |  ___/ | | | | | | | '_ \ / _ \
 | |   | |_| | | |_| | |_) |  __/
 |_|    \__, |_|\__,_|_.__/ \___|
         __/ |                   
        |___/                    

[+] Video name auto-detected : Nausicaä of the Valley of the Wind Soundtrack
[+] Downloading music from https://www.youtube.com/watch?v=rZUppxT38Zk
[+] Downloaded successfully
```

* Same command with 1 level of verbosity (`-v`)

```

  _____    _______    _          
 |  __ \  |__   __|  | |         
 | |__) |   _| |_   _| |__   ___ 
 |  ___/ | | | | | | | '_ \ / _ \
 | |   | |_| | | |_| | |_) |  __/
 |_|    \__, |_|\__,_|_.__/ \___|
         __/ |                   
        |___/                    

[youtube] rZUppxT38Zk: Downloading webpage
[youtube] rZUppxT38Zk: Downloading video info webpage
[+] Video name auto-detected : Nausicaä of the Valley of the Wind Soundtrack
[+] Downloading music from https://www.youtube.com/watch?v=rZUppxT38Zk
[youtube] rZUppxT38Zk: Downloading webpage
[youtube] rZUppxT38Zk: Downloading video info webpage
[youtube] Downloading just video rZUppxT38Zk because of --no-playlist
[download] Destination: /home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.webm
[download] 100% of 9.36MiB in 00:13
[ffmpeg] Destination: /home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.mp3
Deleting original file /home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.webm (pass -k to keep)
[+] Downloaded successfully
```

* Same command with full verbosity (`-vv`)

```  _____    _______    _          
 |  __ \  |__   __|  | |         
 | |__) |   _| |_   _| |__   ___ 
 |  ___/ | | | | | | | '_ \ / _ \
 | |   | |_| | | |_| | |_) |  __/
 |_|    \__, |_|\__,_|_.__/ \___|
         __/ |                   
        |___/                    

[debug] Encodings: locale UTF-8, fs utf-8, out UTF-8, pref UTF-8
[debug] youtube-dl version 2019.09.28
[debug] Python version 3.7.5rc1 (CPython) - Linux-5.2.0-amd64-x86_64
[debug] exe versions: ffmpeg 4.1.4-1, ffprobe 4.1.4-1, phantomjs 2.1.1, rtmpdump 2.4
[debug] Proxy map: {}
[youtube] rZUppxT38Zk: Downloading webpage
[youtube] rZUppxT38Zk: Downloading video info webpage
[youtube] {18} signature length 107, html5 player vflsEMaQv

[...]

[youtube] {251} signature length 103, html5 player vflsEMaQv
[debug] Default format spec: bestvideo+bestaudio/best
[+] Video name auto-detected : Nausicaä of the Valley of the Wind Soundtrack
[+] Downloading music from https://www.youtube.com/watch?v=rZUppxT38Zk
[debug] Encodings: locale UTF-8, fs utf-8, out UTF-8, pref UTF-8
[debug] youtube-dl version 2019.09.28
[debug] Python version 3.7.5rc1 (CPython) - Linux-5.2.0-amd64-x86_64
[debug] exe versions: ffmpeg 4.1.4-1, ffprobe 4.1.4-1, phantomjs 2.1.1, rtmpdump 2.4
[debug] Proxy map: {}
[youtube] rZUppxT38Zk: Downloading webpage
[youtube] rZUppxT38Zk: Downloading video info webpage
[youtube] Downloading just video rZUppxT38Zk because of --no-playlist
[youtube] {18} signature length 107, html5 player vflsEMaQv
[youtube] {135} signature length 103, html5 player vflsEMaQv

[...]

[youtube] {251} signature length 103, html5 player vflsEMaQv
[debug] Invoking downloader on 'https://r6---sn-5ualdn7s.googlevideo.com/videoplayback?expire=1572064579&ei=43izXeyXBJmA1uUPt4StsAU&ip=107.141.128.56&id=o-AH-apRfP-TCv9bFhxeatO6PkoPd9YaNMyxlaTSEE8F6x&itag=251&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-5ualdn7s%2Csn-5uaeznde&ms=au%2Crdu&mv=m&mvi=5&pl=16&initcwndbps=918750&mime=audio%2Fwebm&gir=yes&clen=9812152&dur=567.861&lmt=1540037730177709&mt=1572042871&fvip=6&keepalive=yes&fexp=23842630&c=WEB&txp=5511222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRAIgeBB0BZwnZISSFBQokoGYnLfUgT4nVeZy-_LNPh014o4CIBlWYPFsK9_HOFmrekCSI6f2GP04-ZmE2Bw1zfGzZ2uu&sig=ALgxI2wwRAIgdcZbm7tumfFBEwIA_ojnqBuuodGm3ckMCeBRsSxV3oMCICgD2HbMFMC0e8Owb2r76XOtqBREzDsRP34xaJogtA_A&ratebypass=yes'
[download] Destination: /home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.webm
[download] 100% of 9.36MiB in 00:12
[debug] ffmpeg command line: ffprobe -show_streams 'file:/home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.webm'
[ffmpeg] Destination: /home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.mp3
[debug] ffmpeg command line: ffmpeg -y -loglevel repeat+info -i 'file:/home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.webm' -vn -acodec libmp3lame -b:a 320k 'file:/home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.mp3'
Deleting original file /home/Doe/Downloads/Nausicaä of the Valley of the Wind Soundtrack.webm (pass -k to keep)
[+] Downloaded successfully
```


## Playlist mode download

PyTube can download all music in a Youtube playlist, you need to use the URL (**not a video ID**)

You can specify `--format` argument, all audio files will have the same format

### Examples

