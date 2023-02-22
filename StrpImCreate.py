from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import csv

# open dialogue to select a file
#from tkinter.filedialog import askopenfilename
#filename = askopenfilename()
#print(filename)

with open('StroopTrials.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}') # prints the column names for reference
            line_count += 1
        else:
            word = {row[1]} # prints the word to the console
            colour = {row[2]} # prints the colour to the console
            print(word)
            print(colour)
            line_count += 1


img = np.zeros([300,300,3],dtype=np.uint8)
img.fill(255) # numpy array!
im = Image.fromarray(img) #convert numpy array to image
I1 = ImageDraw.Draw(im)
# Custom font style and font size
myFont = ImageFont.truetype("arial.ttf", 65)
# Add Text to an image, the first numbers are the location
I1.text((110, 110), "red",font=myFont, fill="green")
# Display edited image
im.show()
im.save('REDgreen.jpg')



    
