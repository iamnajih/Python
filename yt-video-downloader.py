from pytube import YouTube
link=input("Enter The Link")
yt=YouTube(link)
ys=yt.streams.get_highest_resolution()
print("Downloading")
ys.download()
print("Downloaded")
