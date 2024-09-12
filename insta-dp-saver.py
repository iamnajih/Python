import instaloader
app=instaloader.Instaloader()
username=input("Enter The UserName      ")
print("Collecting ID ")
app.download_profile(username, profile_pic_only=True)
app.showProfile()
