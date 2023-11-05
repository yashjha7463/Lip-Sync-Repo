import requests
import os
import cv2
from os import path
from tqdm import tqdm
from pytube import YouTube
import shutil
import os
import subprocess
import gdown

# Download YouTube video
def download_video(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()
    video.download(filename='youtube_video.mp4')
    print("Video was downloaded successfully")

# Download video, process it, and save the output
def main():
    video_url = "https://www.youtube.com/watch?v=YMuuEv37s0o"
    download_video(video_url)
    os.system('ffmpeg -y -i youtube_video.mp4 -ss 0 -t 67 -async 1 ./input_video.mp4')
    os.system('gdown 1jhUOAeGw8lPjNf7Q1cIcBOvzE3CJ3gVz')
    os.system('cd .//Lip-Sync-Repo/Wav2Lip && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "../../input_video.mp4" --audio "../../output10.wav" --nosmooth --outfile ../../output_video.mp4 --fps 25 --face_det_batch_size 32 --wav2lip_batch_size 128')

if __name__ == "__main__":
    main()
