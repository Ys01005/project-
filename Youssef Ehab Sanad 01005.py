method=str(input("Please choose the method suitable for you TRN,user_input,file: "))
if method =="TRN":
 import time
 a = 1140671485 
 c= 12820163
 m = 2**24
 seed = time.time()
 def LCG(rando):
    seed = int(((a*rando)+c)%m)
    return seed
 print("LCG random numbers generator")
 for X in range(1,21):
    print(X,":",LCG(seed))
    seed = LCG(seed)
elif method =="user_input":
 a = 1140671485 
 c= 12820163
 m = 2**24
 seed = int(input("Seed: "))
 def LCG(rando):
        seed = int(((a*rando)+c)%m)
        return seed
 print("LCG random numbers generator")
 for X in range(1,21):
    print(X,":",LCG(seed))
 seed = LCG(seed)

elif method =="file":
 a = 1140671485 
 c= 12820163
 m = 2**24
 file = open("project.txt","r")
 seed = int(file.read())
 def LCG(rando):
    seed = int(((a*rando)+c)%m)
    return seed

 print("LCG random numbers generator")
 for X in range(1,21):
    print(X,":",LCG(seed))
    seed = LCG(seed)
else:
    print("Please try again from the available method")
   
        

       
   
    
