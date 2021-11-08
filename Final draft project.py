import time

print("Welcome to Youssef's Pseudorandom number generator")

method = input("Please choose the method suitable for you TRN, User_input, file: ")

             
def LCG(initVal):
    
    a= 1140671485
    c= 12820163
    m= 2**24
    rando =initVal
    
    for i in range(1,21):
        rando = ((a*rando+c)%m)
        print(rando)
    return rando

if method =="TRN":
    now=int(time.time())
    LCG(now)

elif method=="User_input":
    seed=int(input("Please enter the seed: "))
    LCG(seed)
    
elif method=="file":
    file = input("Please enter your file name with .txt extension: ")
    with open(file) as f:
        file_content = int(f.read())
    LCG(file_content)
else:
    print("Please try again from the available methods")
