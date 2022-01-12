# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:09:38 2022

@author: Amol
"""

from tkinter import *
from pytube import YouTube

top=Tk()
top.geometry('500x300')
top.resizable(0,0)
top.title('Youtube video downloader')

Label(top,text='Youtube Video Downloader',font ='arial 22 bold').pack()
link = StringVar()
Label(top, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(top, width = 70,textvariable = link).place(x = 30, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(top, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
Button(top,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
top.mainloop()