from sketchpy import library,canvas


def PreSketch():
    print("1.ajp\
    2.rdj\
    3.gojo\
    4.vijay\
    5.tom_holland\
    6.flag\
    7.ironman_ascii\
    8.Bts")
    b=int(input("Enter the choice (from number) "))

    if (b==1):
        obj=library.apj()
        obj.draw()
    elif (b==2):
        obj=library.rdj()
        obj.draw()
    elif (b==3):
        obj=library.gojo()
        obj.draw()
    elif (b==4):
        obj=library.vijay()
        obj.draw()
    elif (b==5):
        obj=library.tom_holland()
        obj.draw()
    elif (b==6):
        obj=library.flag()
        obj.draw()
    elif (b==7):
        c=input("This will take more time arount 10 minutes+ . Are you wish to be continue(y/n)?")
        if (c=="y" or "Y"):
            obj=library.ironman_ascii()
            obj.draw()
        else:
            print("Exited")
    elif (b==8):
        obj=library.bts()
        obj.draw()
    else:
        print("Invalid choice : Choose a number from 1 to 7")


def SketchFromImage():
    img_path=input("Enter the image path ")
    if "\\" in img_path:
        img_path=img_path.replace("\\", "/")
    obj = canvas.sketch_from_image(img_path)
    obj.draw(threshold = 127)

def SketchFromSVG():
    svg_path=input("Enter the svg path ")
    if "\\" in svg_path:
        svg_path=svg_path.replace("\\", "/")
    obj = canvas.sketch_from_svg(svg_path)
    obj.draw()

print("1.Presketch \
2.Sketch from image\
3.Sketch from SVG\
")
sketch_choice=int(input("Enter the Choice : "))

if (sketch_choice==1):
    PreSketch()
elif (sketch_choice==2):
    SketchFromImage()
elif (sketch_choice==3):
    SketchFromSVG()
else:
    print("Invalid choice : Choose a number from 1 to 3")




