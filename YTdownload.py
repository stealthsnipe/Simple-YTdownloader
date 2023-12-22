import os
from tkinter import *
from pytube import YouTube
from sys import argv

class YouTubeDownloader:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Downloader")

        self.label = Label(master, text="Enter YouTube Link:")
        self.label.pack()

        self.link_entry = Entry(master)
        self.link_entry.pack()

        self.download_button = Button(master, text="Download", command=self.download_video)
        self.download_button.pack()

    def download_video(self):
        link = self.link_entry.get()
        yt = YouTube(link)
        path = os.path.dirname(os.path.realpath(__file__))

        print("\n" + "downloading..." + "\n")

        print("Title: ", yt.title)

        print("\n")

        yd = yt.streams.get_highest_resolution()

        yd.download(path)

        print("downloaded: " + yt.title)

root = Tk()
my_gui = YouTubeDownloader(root)
root.mainloop()
