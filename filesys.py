import os

path = '/home/sunbeam/Project/CUB_200_2011/CUB_200_2011/images'

folders = []
arr1=[]
birds=[]

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder))

for f in folders:
    arr=(f.split("/"))
    arr1=(arr[-1].split("."))
    bird=(arr1[-1])
    birds.append(bird)
    birds.sort()
    #print(bird)
f = open("birds.txt", "w+")

for bird in birds:
    print(bird)
    f.write(bird + "\n")
f.close()