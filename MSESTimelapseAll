'''
Compiles all images from yesterday into a mp4 file.
Should work in both python2 and python3.
'''

import cv2
import os
import datetime

#change these variables
framerate = 10
path = '/Users/administrator/Desktop/AdensFolder/msestimelapseall'
width = 3840
height = 1080
daysBack = 3

#current system date - daysBack variable
date = datetime.datetime.now() - datetime.timedelta(days = daysBack)

#change month and day value because filenames
if date.month < 10:
    month = '0' + str(date.month)
else:
    month = date.month

if date.day < 10:
    day = '0' + str(date.day)
else:
    day = date.day

#output name based on system date
output = 'msestimelapse-daily-{}{}{}.mp4'.format(date.year, month, day)

#make list of all images in path from set date
print('Listing images...')

images = []

for img in os.listdir(path):
    if img.startswith('{}-{}-{}'.format(date.year, month, day)):
        images.append(img)

#Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, framerate, (width, height))

#Make sure images isn't empty
if images == []:
    raise ValueError('No images to compile')

#Create frames
print('Creating frames...')

for image in images:

    image_path = os.path.join(path, image) #os.path.join joins together paths
    frame = cv2.imread(image_path)

    out.write(frame) #write frame to video

    #Create progress indicator


#Release the video!
print('Finishing up...')
out.release()
print('Done!')
