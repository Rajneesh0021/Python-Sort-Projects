from pytube import YouTube, Playlist
playORvid=input("playlist or video?")


# ***********video download****************

def download_onevideo():
  link=input('paste youtube video link: ')
  vid_aud=input("only audio? yes / no : ")
  yt_1=YouTube(link)

  if vid_aud=='yes':
    videos=yt_1.streams.filter(only_audio=True) 
  if vid_aud=='no':
    videos=yt_1.streams.all()

  vid=list(enumerate(videos))
  for i in vid:
    print(i)

  print()
  strm =int(input("enter stream number : "))
  videos[strm].download()
  print("title: ", yt_1.title)
  print("Thumbnail_url: ",yt_1.thumbnail_url)
  print("successfully")



# ******************playlist Download*******************

def download_playlist():
    link=input('paste youtube video playlist link: ')
    py =Playlist(link)
    print(f'Downloading : {py.title}')
    for video in py.videos:
        video.streams.first().download()



if playORvid=="video":
 download_onevideo()
if playORvid=="playlist":
  download_playlist()