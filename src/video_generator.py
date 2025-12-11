from moviepy.editor import *
import os

def create_video(audio_file, output="podcast_video.mp4"):

    # background color clip
    clip = ColorClip(size=(1080, 1920), color=(20, 20, 20), duration=30)

    # load audio
    audio = AudioFileClip(audio_file)

    # set clip duration to audio length
    clip = clip.set_duration(audio.duration)

    # attach audio
    clip = clip.set_audio(audio)

    # write video file
    clip.write_videofile(output, fps=30)
    print("Video created:", output)

if __name__ == "__main__":
    create_video("podcast.wav")
