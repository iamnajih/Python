import moviepy
import moviepy.editor
a=input("Enter The Song Name")
video=moviepy.editor.VideoFileClip(a)
audio=video.audio
print("EXTRACTED")
