import numpy as np
from imageio.v2 import imread, imwrite
import cv2
print("Image must contain in the same folder of the python  And add extension code of them.It is only required for typing image name")
inp=input("Enter the image name or location")

img=imread(inp)
arr=img+np.array( [0.1, 0.2, 0.5])
arr2=(255*arr/arr.max()).astype(np.uint8)
tst=input("Enter the name for temporary storing an image and end with .png extension")
cv2.imwrite(tst,arr2)
img2=cv2.imread(tst)
gamma=2
gammaimg=np.array(255*(img2/255)**gamma, dtype='uint8')
final=input("Enter the name for the output picture")
cv2.imwrite(f"{final}.png",gammaimg)
print("Conversion Done!")
