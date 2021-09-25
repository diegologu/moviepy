import sys
from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip(sys.argv[1]).margin(10)
clip2 = VideoFileClip("output/messi_hazlo_volume.mp4").margin(10)
final_clip = clips_array([[clip1, clip2]])
final_clip.write_videofile(sys.argv[2], preset="ultrafast", threads=4)
