import pytube

##import tkinter as tk

link = input('Enter link of the video: ')

done = True

point = pytube.YouTube(link)

file_formats = point.fmt_streams

##fmt = int(input('1. Video \n2. Audio \n'))

sr = 1
for s in file_formats:
    if s.resolution == None or s.subtype == None:
        continue
    if s.type == 'video':
        print(sr, end = '. ')
        print(s.resolution+' '+s.subtype)
        sr += 1
choice = int(input('Enter resolution: '))
choice -= 1
output_path = input('Enter location where video must be downloaded: ')
file_formats[choice].download(output_path)

##elif fmt == 2:
##    sr = 1
##    for s in file_formats:
##        if s.type == 'audio':
##            print(sr, end = '. ')
##            print(s.subtype)
##            sr += 1
##    choice = int(input('Enter quality: '))
##    choice -= 1
##    output_path = input('Enter location where video must be downloaded: ')
##    file_formats[choice].download(output_path)

##else:
##    done = False

if done:
    print('Download completed')


    
