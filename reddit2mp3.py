import html.parser

from bs4 import BeautifulSoup
import urllib

from functions import *


print("This software is literally thrown together, it will be improved over time. Keep that in mind")
print("Feel free to commit your own changes to the code base over on Github\n")
print("https://github.com/Codeusa/RedditToMP3\n")
print("If you need support feel free to tweet me @Codeusasoftware")
print("- Andrew\n")
html_parser = html.parser.HTMLParser()

#TODO
#Handling direct video input rather than parsing
#Loading urls from text
#Searching for Bobby Fischer
#error handling
#threading
#clean up this mess


#saving all of our urls to a text file

song_list = open("music.txt", "a")

#to be used for playlist check
last_id = ''

#user inputs, let them break it
page_url = input("Enter the url you'd like to parse for videos: ")

#wtf am i doing
output_path = input("Where would you like files to go?: (C:/output/)")

video_dir = output_path
music_dir = output_path
print("House Cleaning...")
os.chdir(output_path)
extensions = glob.glob('*.mp4')
for filename in extensions:
    os.unlink(filename)
extensions = glob.glob('*.mp3')
for filename in extensions:
    os.unlink(filename)

print("Parsing urls...")
#get our request ready
req = urllib.request.Request(page_url,
                             headers={
                             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'})  #let there be chrome
#get html source code
html = urllib.request.urlopen(req).read()

#setup godly soup
soup = BeautifulSoup("".join(str(html)))  #convert that pesky string to a string

#find all hyperlinks
links = soup.findAll("a", href=True)  #won't find all the links on reddit without the href true, *shrugs*

for href in links:
    if 'watch?v=' in href["href"]:  #ensure youtube videos only get listed
        video_link = href["href"]  #set for safety

        if 'http' not in video_link or 'https' not in video_link:  #playlist don't include the http forward
            video_link = 'http://www.youtube.com%s' % video_link

        video = pafy.new(video_link)  #setting up youtube API
        current_id = video_id(video.watchv_url)
        if current_id == last_id:  #because playlist have duplicates
            continue

        title = video.title  #getting the youtube video title

        video_link = html_parser.unescape(video.watchv_url)  #encoding html chars, do i even need this?

        title = html_parser.unescape(title)  #encoding html chars, do i even need this?

        print(('Song: %s | %s \n' % (title, video_link)))

        song_list.write(('%s|%s\n' % (title.encode('utf8'), video_link)))  #write the song title and url to a text file

        download(video_link)  #download the youtube video

        last_id = current_id  #set id of the last video downloaded

song_list.close()
print('Converting videos to mp3... (keep an eye on your output folder)')
convert_videos()  #no idea how to go about a progress bar atm, need soda
