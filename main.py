
print("TYPE WHAT YOU WANT")
lst=['Audio Book','Audio Extracter','Calculator','AutoLoop Message','YT Video Downloader','Voice Recorder','Instagram Profile Downloader','Screen Sharing']

print(lst)
def audiobook():
    import pyttsx3
    a=input("Enter The Location Or The Same Directory")
    book=open(f"{a}")
    text=book.readlines()
    engine=pyttsx3.init()
    for i in text:
        engine.say(i)
        engine.runAndWait()

def audioextracter():
    import moviepy
    import moviepy.editor
    a=input("Enter The Location OR The Song Name In Same Directory")
    video=moviepy.editor.VideoFileClip(a)
    audio=video.audio
    print("EXTRACTER")
def calculator():
    def add(a,b):
        return(a+b)
    def sub(a,b):
        return(a-b)
    def prod(a,b):
        return(a*b)
    def div(a,b):
        return(a/b)


    num1=int(input("Enter The First Number"))
    choices=input("Enter The Sign")
    num2=int(input("Enter The Second Number"))
    if choices == '+':
        input("For Continue Press ENTER")
        print("The Result Is",add(num1,num2))
    elif choices == '-':
        input("For Continue Press ENTER")
        print("The Result Is",sub(num1,num2))
    elif choices == '*':
        input("For Continue Press ENTER")
        print("The Result Is",prod(num1,num2))
    elif choices == '/':
        input("For Continue Press ENTER")
        print("The Result Is",div(num1,num2))
    else:
        print(choices,"Is A Invalid Input.We Suggest(+,-,*,/)")
def automsg():
    def loop():
        import pyautogui as pg
        import time
        r=int(input("Enter The Sleep Time  "))
        s=int(input("Enter The Limit  "))
        u=input("Enter The Message  ")
        time.sleep(r)
        for i in range(s+1):
            pg.write(u)
            pg.press("Enter")
    def bot():
        import pywhatkit as kit
        number=input("Enter The Phone Number With Country Code")
        hour=int(input("Enter The Hour For Limit  "))
        minute=int(input("Enter The Minute For Limit  "))
        msg=input("Enter The Message")
        kit.sendwhatmsg(
            number,
            msg, hour,minute
            )
    a=input("Loop Or Bot       ")
    if(a=="Loop"):
        loop()
    elif(a=="Bot"):
        bot()
    else:
        print("Must Type   Loop  ,  Bot")
def yt():
    from pytube import YouTube
    link=input("Enter The Link")
    yt=YouTube(link)
    ys=yt.streams.get_highest_resolution()
    print("Downloading")
    ys.download()
    print("Downloaded")
def voice():
    import sounddevice
    from scipy.io.wavfile import write
    fs=44100
    second=int(input("Enter The Time Duration In Seond        "))
    print("RECORDING...")
    record=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    write("out.wav",fs,record)
    print("Finished")
def instadpsaver():
    import instaloader
    app=instaloader.Instaloader()
    username=input("Enter The UserName      ")
    print("Collecting ID ")
    app.download_profile(username, profile_pic_only=True)
    app.showProfile()

def screenshare():
    def client():
        import pyautogui
        import keyboard
        import socket
        import json
        import os
        import threading
        from win32api import GetSystemMetrics
        import sys
        from tkinter import Label, Tk, Canvas, NW
        from PIL import Image, ImageFile, ImageTk
        from io import BytesIO

        ImageFile.LOAD_TRUNCATED_IMAGES = True
        s=socket.socket()
        v='0.02'
        purple="\033[0;35m"
        yellow="\033[1;33"
        green="\033[1;36"
        blank="\033[0m"
        appdata=os.getenv('APPDATA')
        configpath="klipy.json"
        res=0
        quality=0
        def write(arg):
            print(" > Writing config")
            config=json.durps(arg)
            try:
                with open(configpath, "w") as f:
                    f.write(str(config))
                    print(" > Succesfully writed to config")
                    pass
            except Exception as e:
                print(f"  > Couldn't write to config{e}")
    def server():
        import pyautogui
        import socket
        import asyncio
        import PIL.Image, PIL.ImageFile, PIL.ImageTk
        import os
        import threading
        from io import BytesIO
        from win32api import GetSystemMetrics, NameDisplay

        s=socket.socket()
        print("Starting Server")
        resx=int(GetSystemMetrics(0) / 2)
        resy=int(GetSystemMetrics(1) / 2)
        print(f'> Using display with resolution {GetSystemMetrics(0)}')
        port=22371
        s.bind(('', port))
        print(f' > Server running at {port}')
        print(' > Listening for connection...')
        s.listen(1)

        c, addr=s.accept()
        print(f' > Got connection from {addr}')
        class server:
            size=102400
        def key(self):
                while True:
                    try:
                        key=c.recv(512).decode()
                        print(key)
                        pyautogui.write(key)
                    except Exception as e:
                        pass
    naj=input("Client OR Server")
    if(naj=="Client"):
        client()
    elif(naj=="Server"):
        server()
    else:
        print("Invalid Input")
        print("Type Exactly   Client / Server")
    










ask=input("Enter The Name Of One Of These")
if(ask=="Audio Book"):
    audiobook()
elif(ask=="Audio Extracter"):
    audioextracter()
elif(ask=="Calculator"):
    calculator()
elif(ask=="AutoLoop Message"):
    automsg()
elif(ask=="YT Video Downloader"):
    yt()
elif(ask=="Voice Recorder"):
    voice()
elif(ask=="Instagram Profile Downloader"):
    instadpsaver()
elif(ask=="Screen Sharing"):
    screenshare()
else:
    print("INVALID INPUT")
    print("Please Enter Input Exactly",lst)



