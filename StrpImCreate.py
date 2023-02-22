from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import csv
import os

# open dialogue to select a file
from tkinter.filedialog import askopenfilename
fileToOpen = askopenfilename()
print(fileToOpen)

dirname, filename = os.path.split(fileToOpen)

print(dirname)

### select a location for saving files
##import tkinter as tk
##from tkinter import filedialog
##
##root = tk.Tk()
##root.withdraw()
### file_path = filedialog.askopenfilename()
##file_path = filedialog.askdirectory()

width, height = 100, 100

directory = os.path.join(dirname+"/")
PATH = os.path.join(dirname+"/converted")
if not os.path.exists(PATH):
    os.mkdir(PATH)
    print("done")
# os.mkdir(dirname + "/converted")
print(directory)

with open(fileToOpen) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')



    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}') # prints the column names for reference
            line_count += 1
        else:
            word = row[1] # prints the word to the console
            colour = row[2] # prints the colour to the console
            print(word)
            print(colour)
            #FOLLOWING CREATES THE IMAGE
            img = np.zeros([width,height,3],dtype=np.uint8) # start creating an image (i.e. white image)
            img.fill(255) # numpy array!
            im = Image.fromarray(img) #convert numpy array to image
            I1 = ImageDraw.Draw(im)
            # Custom font style and font size
            myFont = ImageFont.truetype("arial.ttf", int(width/4)) # specifies font and font size for words. Font size is reliant on width size now (e.g. width/4)
            # Add Text to an image, the first numbers are the location
            I1.text(((width)/2, (height)/2), word,font=myFont, fill=colour,anchor="mm", align='center')
            # Display edited image
            # im.show() # do not include this if you have a large list as it will create and show each image
            fnlist = [word.upper(),colour]
            fname="".join(fnlist)
            print(fname)
            im.save(directory+"converted/"+fname+".jpg") # save to a directory (should work)
            #im.save(f"{file_path}\%s.jpg" % fname) # removed for now while checking
            line_count += 1
            





    
