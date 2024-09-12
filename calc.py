def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def prod(a,b):
    return(a*b)
def div(a,b):
    return(a/b)


num1=int(input("Enter The First Number"))
choices=input("Enter The Sign")
num2=int(input("Enter The Second Number"))
if choices == '+':
    input("For Continue Press ENTER")
    print("The Result Is",add(num1,num2))
elif choices == '-':
    input("For Continue Press ENTER")
    print("The Result Is",sub(num1,num2))
elif choices == '*':
    input("For Continue Press ENTER")
    print("The Result Is",prod(num1,num2))
elif choices == '/':
    input("For Continue Press ENTER")
    print("The Result Is",div(num1,num2))
else:
    print(choices,"Is A Invalid Input.We Suggest(+,-,*,/)")


