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
   
