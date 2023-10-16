list1 =[1,2,3,4,5,6,7,8,9,10]
length=len(list1)

mid = 5
target=9
for i in range(length):
    if(mid<target):
        mid+=1
    elif(mid<target):
            mid-=1
    if(mid==target):
        print("target",mid,"found")
    else:
            print("target not found")
