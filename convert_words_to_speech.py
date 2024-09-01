from gtts import gTTS

import vlc
myobj = gTTS ( text= ' صباح النور يا وردة'  ,lang = 'ar', slow=False)

# Saving the converted audio in a mp3 file named
myobj.save("welcome.mp4")

# Playing the converted file
p = vlc.MediaPlayer("./welcome.mp4")
p.play()

while True:
    pass