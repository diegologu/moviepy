import sys
import moviepy.editor as mpy

clip = mpy.VideoFileClip(sys.argv[1])
txt = mpy.TextClip('Messi', font='Courier',
                   fontsize=120, color='white', bg_color='gray35')
txt = txt.set_position(('center', 0.6), relative=True)
txt = txt.set_start((0, 1)) # (min, s)
txt = txt.set_duration(3)
txt = txt.set_opacity(0.5)
txt = txt.crossfadein(0.5)
txt = txt.crossfadeout(0.5)
# composite video
final_clip = mpy.CompositeVideoClip([clip, txt])
# save file
final_clip.write_videofile(sys.argv[2])#, fps=24,
