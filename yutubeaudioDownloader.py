from django.forms import FilePathField
from pytube import YouTube
from pytube import Search
import pafy

search = input("Enter name of song: ")
s = Search(search)

j = 1
for i in s.results:
    title = (i.title).encode('utf8')
    print(j, end = ". ")
    print(title.decode('utf8'))
    if j == 5:
        break
    j += 1

vdo_index = eval(input("Enter index:"))

vdo_id = s.results[vdo_index-1].video_id


p = pafy.new(vdo_id)
ba = p.getbestaudio()
filen = "song2.mp3";
filename = ba.download(filepath = filen)
