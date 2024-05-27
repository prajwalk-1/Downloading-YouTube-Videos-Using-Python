from pytube import YouTube

link = input("Enter a Link :")
yt = YouTube(link)

print("Title :", yt.title) # To print title

print("Publish Date:", yt.publish_date) # to print Publish date

print("Views :", yt.views) # To get number of views

print("Duration :", yt.length) # To get the length of video

print("Description :", yt.description) # To get description

print("Ratings :", yt.rating) # To get ratings


# Download the video in the highest resolution available
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download completed!!")
