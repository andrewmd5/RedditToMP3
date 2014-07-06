RedditToMP3
===========

Parse Reddit or any other page for youtube links and automatically download and convert them to MP3's

#Features
* Parse a youtube playlist and convert all songs to an mp3
* Parse a reddit thread or page to get all youtube links and convert them to mp3's
* Saves all youtube urls found to a local list for your convience

#Requirements
* [Pafy](https://github.com/np1/pafy)
* Beautifulsoup (bs4)
* [PyDub](https://github.com/jiaaro/pydub)
* Python 3

#TODO

* Handling direct video input rather than parsing
* Loading urls from text
* Searching for Bobby Fischer
* error handling
* threading
* clean up this mess


#Usage

Run the reddit2mp3.py

Enter a url you wish to parse for videos. It can be a playlist like so 

```
https://www.youtube.com/playlist?list=PLeovi-ZvQ66BMG78S9a4F3Yklai2kkvyu
```
Or a reddit thread

```
http://www.reddit.com/r/Music/comments/29tt6a/what_is_your_goto_summer_driving_song/?limit=500
```

then select your output folder

```
C:/output/

```

If any youtube links can be found, they will be downloaded


![example](http://i.imgur.com/ystFKu2.gif)
