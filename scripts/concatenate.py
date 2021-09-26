import sys
import moviepy.editor as mpy

main = mpy.VideoFileClip("output/video_array.mp4")
credits = mpy.VideoFileClip("input/credits.mp4")
final = mpy.concatenate_videoclips([main,credits])
final.write_videofile(sys.argv[2])
