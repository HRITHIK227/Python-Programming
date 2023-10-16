mylist=[1,3,6,8,10,13,15]
length=len(mylist)
x=int(input("set target"))
for i in range(length):
    if mylist[i]==x: 
        print(i)
