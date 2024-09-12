print("Please wait this may take a few seconds...")
from rembg import remove
from PIL import Image
img=input("Enter the path of image")
final=input("Enter the output image name")
finalsave=final+".png"
x=Image.open(img)
res=remove(x)
res.save(finalsave)
print("Finished Have A Look On It")
