a = "Welcome to Python WOrld"
c = 0
print("1: Number of alphabets")
print("2: Number is alphanumeric or not")
print("3: to extract Elements")
option = int(input("which operation you want to perform"))
if(option == 1):
  for i in a:
     if i.isalpha():
        c+=1
        print(c)
        
elif(option == 2):
    if(a.isalnum()):
       print("given str is alphanumeric")
    else: 
        print("Given str is not alphanumeric")

elif(option == 3):
    print(a[8:10])



               
    
