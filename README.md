# StroopImageCreate
The code developed in this uses Python to create images for a Stroop task (i.e. colour words in different colours) from a stimuli list (in csv form). It was developed because some experiment developemnt software does not allow you to colour words and so images have to be used. 
 
The script asks you to select a csv file with your stimulil lists in and this needs to have a word-related column and a colour-related column. You specify which columns these are at the start of the script.

The colours I have used so far are Red,  Green, Blue, and Yellow and all work fine, I have not tried other colours yet. 

## Width and height of images and fontsize
You can vary the width and height of the images needed inputting values into the 'width, height = 400, 400' part. The size of the font is set to be a proportion of the width currently width/4, but this can be changed in the 'myFont = ImageFont.truetype("arial.ttf", int(width/4))' part.
 
## If you want stimuli in all the same colour
If you want all words to be the same colour (e.g. if you want lots of images of words for another task without different colours) just specifiy that one colour in the colour column.

## File format when saving
The images are currently set to save as .jpg but you can specify .png if preferred in the 'im.save(directory+"StimCreated/"+fname+".jpg")' 
## Image show on creation
You can add in im.show() in the loop to show all images once created, but this shoudl be avoided if you have lots of words / images which will be produced (it opens up each instance)

I have tested this and works ok on my computer, but I am only beginning in python coding so use at your own risk. 

The new folder created for the images will include an updated trials list (based on the original used) which will contain a new column with the image file names in. 
