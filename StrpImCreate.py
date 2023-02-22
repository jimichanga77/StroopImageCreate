from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
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



    
