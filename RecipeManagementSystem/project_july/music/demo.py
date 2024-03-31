from gtts import gTTS #convert text into mp3 file
import playsound #to play in pycharm
import os #to handle files example delete

lst = os.listdir('.')  #syntax= . for coming out of current file / tp come back to the file and then file name
if 'hello.mp3' in lst:
     os.remove('hello.mp3')

obj = gTTS(text="Hello", lang='en')

obj.save("hello.mp3")

playsound.playsound("hello.mp3")

os.remove('hello.mp3')
