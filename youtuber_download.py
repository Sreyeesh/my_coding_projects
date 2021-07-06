"""
Project: Python script to help me download youtube videos for editing practice.

Author: Sreyeesh Garimella



"""

from pytube import YouTube
from moviepy.editor import *

path = "/Users/sreyeeshgarimella/Documents/youtube_downloads"

print(f'this is the path where we will save downloads',path)

link = input(f'please input the link of video you want to download: ')

for yt in link:
    print(f'this is the youtube link', yt)
    try:
        youtube_link_download = YouTube(yt)
    except:
        print("can't download the video")
    media_files = yt.filter('mp4')



