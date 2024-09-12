import pyttsx3
a=input("Enter The Location Or The Same Directory")
book=open(f"{a}")
text=book.readlines()
engine=pyttsx3.init()
for i in text:
    engine.say(i)
    engine.runAndWait()
