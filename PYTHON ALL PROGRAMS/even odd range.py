a = range(1,20)
Even = []
Odd = []
for i in a:
    if(i%2==0):
        Even.append(i)
    else:
        Odd.append(i)
print("Even number",Even)
print("Odd number",Odd)
