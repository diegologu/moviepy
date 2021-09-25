import sys
import moviepy.editor as mpy
clip = mpy.VideoFileClip(sys.argv[1]).subclip(2, 4)
clip.write_videofile(sys.argv[2])
