# PyTube

PyTube is an implementation of the great Youtube_dl library

- [PyTube](#pytube)
  - [Requirements](#requirements)
  - [Requirement file](#requirement-file)
- [Sources and ideas](#sources-and-ideas)
- [Command line conflicts](#command-line-conflicts)
- [Full URL or video ID ?](#full-url-or-video-id)
- [Download modes](#download-modes)
  - [Single mode download](#single-mode-download)
    - [Some examples](#some-examples)
  - [Playlist mode download](#playlist-mode-download)
    - [Example](#example)
  - [File mode download](#file-mode-download)
    - [Example with mixed URL and video ID](#example-with-mixed-url-and-video-id)
  - [Album mode](#album-mode)
    - [Example with a Youtube video ID](#example-with-a-youtube-video-id)

>Do not abuse this material. Be responsible.

>All the content of PyTube script is for educational and research purposes only. Do not attempt to violate the law with anything contained here. The authors of this material, or anyone else affiliated in any way, are not going to accept responsibility for your actions. 






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
- `--name` can be use to specify a name of downloaded music (**by default, PyTube use the video name to named the audio file, and replace `/` char by `-`**)
- `--format` can specify the music format with mp3, aac, flac or wav only (**default is mp3**)
- `-v` to increase verbosity of PyTube (maximum is `-vv`)
  - First level of verbosity `-v` add download information (e.g progress bar) 
  - Last level of verbosity `-vv` add debug information about youtube_dl module

# Command line conflicts

Some arguments are incompatibles : 
- Only one mode at a time
- with `--mode single`, you can only use `--id` or `--url` to specify the targeted video
- with `--mode playlist`, you have to specify entire Youtube video link (see bellow)
- with `--mode file`, the argument `--format` will be use for each audio file
- with `--mode playlist` and `--mode file`, **you can't specify a name for audio files**, PyTube will choose and assign automatically names (based on video title)

# Full URL or video ID ? 

PyTube can download music from : 
- URL and video ID in **single mode**
- URL and video ID in **file mode**
- URL only in **playlist mode**

On a video URL (`https://www.youtube.com/watch?v=tLVDOTq5Vc0`), the ID will be the part after `watch?v=` : here it's `tLVDOTq5Vc0`

# Download modes

## Single mode download

Single mode is the easiest way to download music with PyTube.  
With `--format` argument, audio file will be in MP3 format 

You can use a full URL with `--url ` or just the Youtube video ID with `--id`


### Some examples

* With URL : `python3 PyTube.py --mode single --url https://www.youtube.com/watch\?v\=rZUppxT38Zk --output ~/Downloads`


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

* With video ID (shorter command line) : `python3 PyTube.py --mode single --id rZUppxT38Zk --output ~/Downloads`

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
[+] Downloading music from rZUppxT38Zk
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
The URL specified with `--url` argument can have an index number at the end, youtube_dl doesn't care (e.g `https://www.youtube.com/watch?v=znqOAm-DxLk&list=PLxXXw_Jlg3EOqB-gyY3pXleCaB0-iYUKj&index=4`)

If a video is unavailable in the playlist (geo-restriction,removed video), PyTube will aborted the download of the video but not the entire playlist

Note that PyTube don't allow `--name` argument in playlist mode. The video name will be use as audio file name, and use index of video in the playlist as a prefix (`01_video-name`, `02_video-name`, `03_video-name`)

> PyTube doesn't use the youtube_dl to download entire playlist  
> Requests and BeautifulSoup are used, to parse HTML response of the given playlist URL  
> All links are parsed to deduce Youtube video ID



### Example

* `python3 PyTube.py --mode playlist --url https://www.youtube.com/watch?v=unqOAm-DxLk&list=PLxXXw_Jlg3EOqB-gyY3pXleCaB0-iYUKj --output ~/Downloads/playlist`

```
 _____    _______    _          
 |  __ \  |__   __|  | |         
 | |__) |   _| |_   _| |__   ___ 
 |  ___/ | | | | | | | '_ \ / _ \
 | |   | |_| | | |_| | |_) |  __/
 |_|    \__, |_|\__,_|_.__/ \___|
         __/ |                   
        |___/                    

[+] Retrieve ID of videos in the playlist
[+] Videos ID successfully retrieves

[+] Video name auto-detected : You Got A Friend In Me - Randy Newman (Toy Story)
[+] Downloading music from R9SK4OseyBo
[+] Downloaded successfully

[+] Video name auto-detected : The Time of Your Life - Randy Newman (A Bug's Life)
[+] Downloading music from NlePQR7CMMg
[+] Downloaded successfully

[+] Video name auto-detected : When She Loved Me - Sarah McLachlan (Toy Story 2)
[+] Downloading music from lzKAmpoeNBQ
[+] Downloaded successfully

[+] Video name auto-detected : If I Didn't Have You - Billy Crystal & John Goodman (Monsters Inc.)
[+] Downloading music from unqOAm-DxLk
[+] Downloaded successfully

[+] Video name auto-detected : Real Gone - Sheryl Crow (Cars)
[+] Downloading music from Y0wU9BTzfB8
[+] Downloaded successfully

[...]
```


## File mode download

As single mode download, file mode can parse a text file to download URL or video ID  
Just specify `--file` in command line  
The `--format` argument will be apply to all audio files, as `--output`  

The `--name` can be used with file mode, PyTube will set automatically the audio file name based on video name

> PyTube will skip invalid URL/ID, empty lines in file or unvalaible videos (country blocking, removed video)
> Your download process will continue in case of error on a video

### Example with mixed URL and video ID

With a file `references.txt` which have the following content (with some invalid URL/ID for the demo) : 
```
https://www.youtube.com/watch?v=L1OeXcUP3hA
https://www.youtube.com/watch?v=L1OeXcUP
KG7fIFuQTMw
KG7fIFuQ123
https://www.youtube.com/watch?v=qXsuPkyFQuQ
https://www.youtube.com/watch?v=qXsuPkyAAAA
FC4AGdwcy-Q
```

With command line `python3 PyTube.py --mode file --output ~/Downloads/multi --file ~/Downloads/references.txt`, we obtain the following console : 

```
  _____    _______    _          
 |  __ \  |__   __|  | |         
 | |__) |   _| |_   _| |__   ___ 
 |  ___/ | | | | | | | '_ \ / _ \
 | |   | |_| | | |_| | |_) |  __/
 |_|    \__, |_|\__,_|_.__/ \___|
         __/ |                   
        |___/                    

[+] Video name auto-detected : Randy Brecker, Mike Stern, Tom Kennedy, L. Cordew & Ozone Makoto - Some Skunk Funk - Tokyo Jazz 2014
[+] Downloading music from https://www.youtube.com/watch?v=L1OeXcUP3hA

[+] Downloaded successfully

ERROR: Incomplete YouTube ID L1OeXcUP. URL https://www.youtube.com/watch?v=L1OeXcUP
 looks truncated.


[+] Video name auto-detected : Mike Stern - Chromazone
[+] Downloading music from KG7fIFuQTMw

[+] Downloaded successfully

WARNING: Unable to extract video title
WARNING: unable to extract description; please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output.
ERROR: This video is unavailable.
Sorry about that.


[+] Video name auto-detected : Hiromi's Sonicbloom - Time Out
[+] Downloading music from https://www.youtube.com/watch?v=qXsuPkyFQuQ

[+] Downloaded successfully

WARNING: Unable to extract video title
WARNING: unable to extract description; please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output.
ERROR: This video is unavailable.
Sorry about that.


[+] Video name auto-detected : Hiromi Uehara - Caravan
[+] Downloading music from FC4AGdwcy-Q

[+] Downloaded successfully
```
## Album mode

PyTube can automatically detect chapters sections on a video. It will based on video tracklist

![chapters](https://user-images.githubusercontent.com/52102633/68952568-b8c22f00-0785-11ea-8781-542118ef4797.png)

> PyTube will automatically set audio files names, based on tracklist  
> If an audio format is set in command line, it will be apply on each audio files
### Example with a Youtube video ID

With the command line `python3 PyTube.py --mode album --id Ef7uqh_IJ5o --output ~/Music --format flac` : 

```
  _____    _______    _          
 |  __ \  |__   __|  | |         
 | |__) |   _| |_   _| |__   ___ 
 |  ___/ | | | | | | | '_ \ / _ \
 | |   | |_| | | |_| | |_) |  __/
 |_|    \__, |_|\__,_|_.__/ \___|
         __/ |                   
        |___/                    

  [+] Successfully detected tracklist for Ef7uqh_IJ5o
  [+] Following automatic splitting will be apply
  
  - A1 Strollin' : 0.0s - 334.0s
  - A2 Look to the Sky : 334.0s - 661.0s
  - A3 Perk's Blues : 661.0s - 912.0s
  - A4 The Firefly : 912.0s - 1162.0s
  - B1 Movin' Along : 1162.0s - 1497.0s
  - B2 A Taste of Honey : 1497.0s - 1632.0s
  - B3 Inception : 1632.0s - 1946.0s
  - B4 In a Sentimental Mood : 1946.0s - 2416s
  [+] Downloading music from Ef7uqh_IJ5o
  [+] Downloaded successfully
  
  [+] Extracting ~/Music/A1 Strollin'.flac
  [+] Extracting ~/Music/A2 Look to the Sky.flac
  [+] Extracting ~/Music/A3 Perk's Blues.flac
  [+] Extracting ~/Music/A4 The Firefly.flac
  [+] Extracting ~/Music/B1 Movin' Along.flac
  [+] Extracting ~/Music/B2 A Taste of Honey.flac
  [+] Extracting ~/Music/B3 Inception.flac
  [+] Extracting ~/Music/B4 In a Sentimental Mood.flac
```

> You can also specify a video URL

