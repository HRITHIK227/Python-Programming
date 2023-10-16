list1=[[1,2,3,4],#-----0
       [5,6,7,8],#-----1
       [9,10,11,12],#--2
       [13,14,15,16]]
a=0     
for c in list1[3]:
    a+=c
print(a)

sum=0
for r in range(0,len(list1)):
    for c in list1[r]:
        if(r==3):
            sum+=c
print(sum)
        #print(c,end=" ")
       
        #if(c%2==0):
            #a+=c
            
