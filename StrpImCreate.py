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

###================Edit these parts for different sizes and image formats ====================================
#Edit the width, height or extension details as needed
width, height = 400, 400 #pop in some values for width and height of images
ext = ".jpg" #can be .jpg, .png, etc
###===========================================================================================================

# FOLLOWING GETS THE DIRECTORY TO SAVE TO BASED ON THE LOCATION OF THE CSV FILE AND CREATES A FOLDER CALLED 'StimCreated' to store new stimuli (if one already exists it won't create one again)
directory = os.path.join(dirname+"/")
PATH = os.path.join(dirname+"/StimCreated")
if not os.path.exists(PATH):
    os.mkdir(PATH)
    print("done")
# os.mkdir(dirname + "/converted")
print(directory)

with open(fileToOpen) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# The following creates the images for each word in the csv file and adds in the colour as specified in another column
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}') # prints the column names for reference
            line_count += 1
            row.append("image")
            with open(r'StimCreated/trialsUpdated.csv','w') as f1: # need "a" and not w to append to a file, if not will overwrite
                writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
                writer.writerow(row)
        else:
            check = row[4-1]
            print(check)
            word = row[1] # prints the word to the console (NEED TO CHANGE THIS BASED ON COLUMNS IN CSV FILE)
            colour = row[2] # prints the colour to the console (NEED TO CHANGE THIS BASED ON COLUMNS IN CSV FILE)
            print(word)
            print(colour)
            print(row)
            #FOLLOWING CREATES THE IMAGE
            img = np.zeros([width,height,3],dtype=np.uint8) # start creating an image (i.e. white image)
            img.fill(255) # numpy array create
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
            fnameFull = fname + ext
            print(fname)
            print(fnameFull)
            row.append(fnameFull)
            print(row)
            with open(r'StimCreated/trialsUpdated.csv','a') as f1: # need "a" and not w to append to a file, if not will overwrite
                writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
                writer.writerow(row)
            im.save(directory+"StimCreated/"+fname+ext) # save to a directory 
            line_count += 1

    





    
