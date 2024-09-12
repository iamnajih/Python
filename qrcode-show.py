import qrcode
a=input("Enter The Need To Add QR Code")
img=qrcode.make(
    a
)
ask=input("Show Or Save")
if(ask=="Show"):
    img.show()
elif(ask=="Save"):
    r=input("Enter The Name For QR Code")
    img.save(r + ".png")
else:
    print("Invalid Input")
    print("Verify That You Type Exact The-------Show Or Save")
