import os
os.system("pip install moviepy")
from moviepy.edit import *
mp4_file = input("Video yolunu giriniz: ")
mp3_file = input("Müzik adını giriniz sonuna .mp3 ekleyerek: ")
videoClip = VideoFileClip(mp4_file)
audioclip = videoClip.audio
audio.write_audiofile(mp3_file)
audioclip.close()
videoClip.close()
