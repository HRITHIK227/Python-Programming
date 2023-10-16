list1=[[1,2,3,4],#-----0
       [5,6,7,8],#-----1
       [9,10,11,12],#--2
       [13,14,15,16]]
a=0
#for r in list1:
 #   for c,e in enumerate(r):
  #         a+=e
#print(a)

sum=0
for r in range(0,len(list1)):
    for c in range(0,len(list1[r])):
        if(r==c):
            sum+=list1[r][c]
print(sum)

