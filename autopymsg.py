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
