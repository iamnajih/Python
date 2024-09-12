import random
a=['1','2','3','4','5','6','7','8','9','0']
password=""
for i in range(4):
    password=password+random.choices(a)[0]
print(password)


