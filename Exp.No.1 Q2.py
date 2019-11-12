#Generate n random number and write them in a file(.txt,dat)
import random
x=[]
for i in range(100):
    y = random.randint(1,101)
    x.append(y)
    
f=open("New_text2.txt","w")
f.flush()
f.writelines(["%s \n" % item for item in x])
print("File Written")
f.close()