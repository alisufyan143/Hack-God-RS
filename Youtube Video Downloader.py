from pytube import YouTube
link=input("Enter Your Youtube Url= ")
yt= YouTube(link)
videos= yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)
print("Enter the desired option to download the format= ")
dn_option = int(input("Enter The Option= "))
dn_video = videos[dn_option]
dn_video.download()
print("Downloaded Successfuly")