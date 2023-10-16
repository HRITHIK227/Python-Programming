a=10;

def change_value(a):
  a=20
  print("Inside function,address:",id(a))
  return a

print("Before Function call,a=",a,"address:",id(a))

a=change_value(a)

print("After function call,a=",a,"address:",id(a))
