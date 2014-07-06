__author__ = 'Andrew'
import re
import os
import glob
from urllib.parse import *

import pafy
from pydub import AudioSegment


extension_list = ('*.mp4', '*.flv')
video_dir = ''
music_dir = ''

#downloads the youtube video
def download(url):
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    video_file = video_dir + best.title + "." + best.extension
    best.download(quiet=False, filepath=video_file)


#extracts the video id from the url
def video_id(url):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None


#not used anymore, but keeping incase youtube API breaks
def get_between(source, start, stop):
    data = re.compile(start + '(.*?)' + stop).search(source)
    if data:
        found = data.group(1)
        return found.replace('\n', '')
    else:
        return 'none'


#converts the mp4 to an mp3.
def convert_videos():
    os.chdir(video_dir)
    for extension in extension_list:
        for video in glob.glob(extension):
            mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
            AudioSegment.from_file(video).export(music_dir + mp3_filename, format='mp3')