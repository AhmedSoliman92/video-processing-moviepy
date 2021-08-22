from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from moviepy.video.fx.all import crop


source_path=os.path.join(SAMPLE_INPUTS,"sample.mp4")
gif_dir=os.path.join(SAMPLE_OUTPUTS,"gifs")

os.makedirs(gif_dir,exist_ok=True)

output_path=os.path.join(gif_dir,"my_gif.gif")
clip=VideoFileClip(source_path)
fps= clip.reader.fps
#print(clip.size)
# create gif with 5 second duration, and with the orginal video size
part_of_clip = clip.subclip(15,20)
#part_of_clip.write_gif(output_path,fps)

output_path_with_new_size=os.path.join(gif_dir,"my_gif_with_new_size.gif")
# part_of_clip_with_new_size=part_of_clip.resize(width=250)
# part_of_clip_with_new_size.write_gif(output_path_with_new_size,fps)


# create square gif
output_path_for_square_gif=os.path.join(gif_dir,"square_gif.gif")
w,h= clip.size
create_square_gif=crop(part_of_clip,width=500,height=500,x_center=w/2,y_center=h/2)
create_square_gif.write_gif(output_path_for_square_gif,fps=fps)