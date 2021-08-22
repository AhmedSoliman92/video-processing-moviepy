from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import VideoFileClip
from PIL import Image
source_path= os.path.join(SAMPLE_INPUTS,"sample.mp4")
thumbnail_dir= os.path.join(SAMPLE_OUTPUTS,"thumbnails")

os.makedirs(thumbnail_dir,exist_ok=True)

clip= VideoFileClip(source_path)

duration= clip.duration
max_duration=int(duration +1)
# for i in range(max_duration):
#     frame=clip.get_frame(i)
#     new_img_file=os.path.join(thumbnail_dir,f"{i}.jpg")
#     new_img= Image.fromarray(frame)
#     new_img.save(new_img_file)
#     print(f"frame at {i} sec is saved")


# extract frames for every second WAY 1
fps=int(clip.reader.fps) #freame per second
# frame_durations=[]
# frame_duration=1/fps
# for i in range(1,max_duration):
#     next_duration=frame_duration*i
#     frame_durations.append(next_duration)
# for i in range(1,max_duration):
#     path_sec=os.path.join(thumbnail_dir,f"second {i}")
#     os.makedirs(path_sec,exist_ok=True)
#     for j in range(len(frame_durations)):
#         frame=clip.get_frame(frame_durations[j]+i)
#         new_img_path=os.path.join(path_sec,f"{j}.jpg")
#         my_new_image=Image.fromarray(frame)
#         my_new_image.save(new_img_path)

        
    
# extract frames for every second WAY 2 
counter=fps
path_secs=[]
#generate file for every second
for i in range(1,fps+2):
    path_sec=os.path.join(thumbnail_dir,f"second {i}")
    os.makedirs(path_sec,exist_ok=True)
    path_secs.append(path_sec)
second=0
for i,frame in enumerate(clip.iter_frames()):
    if i % fps == 0 and i !=0:
        second+=1
        print(f"Extract the frames of second {second}")
    new_img_path=os.path.join(path_secs[second],f"{i+1}.jpg")
    my_new_image=Image.fromarray(frame)
    my_new_image.save(new_img_path)