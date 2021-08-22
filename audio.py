from conf import SAMPLE_OUTPUTS,SAMPLE_INPUTS
import os
from moviepy.editor import *
#from moviepy.audio.fx.all import volumex
source_path_audio=os.path.join(SAMPLE_INPUTS,"audio.mp3")
source_path_video=os.path.join(SAMPLE_INPUTS,"sample.mp4")
audio_output_dir=os.path.join(SAMPLE_OUTPUTS,"audio")
os.makedirs(audio_output_dir,exist_ok=True)

destination_path=os.path.join(audio_output_dir,"my_audio.mp3")
destination_path1=os.path.join(audio_output_dir,"my_audio1.mp3")
final_destination_path=os.path.join(audio_output_dir,"final_audio.mp3")
final_video_destination=os.path.join(audio_output_dir,"mixed_video.mp4")
#detach the audio
clip=VideoFileClip(source_path_video)

detach_audio=clip.audio

#detach_audio.write_audiofile(destination_path)

#merge audio with audio of video

audio_to_merge=AudioFileClip(source_path_audio)
audio_clip=audio_to_merge.subclip(0,clip.duration)
audio_clip=audio_clip.volumex(0.20)
#audio_clip.write_audiofile(destination_path1)

final_audio=CompositeAudioClip([detach_audio,audio_clip])
#final_audio.write_audiofile(final_destination_path,fps=detach_audio.fps)

# merge the audio to video

final_clip=clip.set_audio(final_audio)
final_clip.write_videofile(final_video_destination)