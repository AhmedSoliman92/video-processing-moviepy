from moviepy.tools import is_string
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image
source_path= os.path.join(SAMPLE_OUTPUTS,"thumbnails")
thumbnails_per_second_dir=os.path.join(SAMPLE_OUTPUTS,"thumbnails_per_second")
os.makedirs(thumbnails_per_second_dir,exist_ok=True)
output_video=os.path.join(thumbnails_per_second_dir,'thumb.mp4')
output_video_1=os.path.join(thumbnails_per_second_dir,'ImageClip.mp4')
img_dirs_for_every_second=os.listdir(source_path)
img_dirs_for_every_second_dict={}
#print(img_dirs_for_every_second)
for fname in img_dirs_for_every_second:
    fname_as_float=float(fname.replace("second ",""))
    frames_in_second=os.listdir(source_path+'\\'+fname)
    img_name_as_int=[]
    for frame in frames_in_second:
        img_name_as_int.append(int(frame.replace(".jpg","")))
    img_dirs_for_every_second_dict[fname_as_float]=img_name_as_int
#paths_of_all_frames
paths_of_all_frames=[]
for second in sorted(img_dirs_for_every_second_dict.keys()):
    for img in sorted(img_dirs_for_every_second_dict[second]):
        second_file="second "+str(int(second))
        frame_file=str(img)+".jpg"
        paths_of_all_frames.append(os.path.join(source_path,second_file,frame_file))
#print(paths_of_all_frames)
# clip= ImageSequenceClip(paths_of_all_frames,fps=30)
# clip.write_videofile(output_video)



my_clip=[]
#using all the images will generate the error:
#Unable to allocate 5.93 MiB for an array with shape (1080, 1920, 3) and data type uint8 
for path in paths_of_all_frames[0:200]:
    frame=ImageClip(path)
    my_clip.append(frame.img)

clip= ImageSequenceClip(my_clip,fps=5)
clip.write_videofile(output_video_1)

