import random
name = ["Anna" , "Tom" , "Angela" , "Max"]
do = ["cook" , "eat" , "sleep" , "do homework"]
random.shuffle (name)
random.shuffle (do)
for item in range (1):
    print (name[0] + " " + do[1] + ".")

for item in range (1):
    print (name[1] + " " + do[2] + ".")

for item in range (1):
    print (name[2] + " " + do[3] + ".")

for item in range (1):
    print (name[3] + " " + do[0] + ".")

print ("The end!")