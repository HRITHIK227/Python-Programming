print(bin(10))
print(bin(15))


print(bool(0))
print(bool(42))
print(bool([]))
print(bool([1,2]))

byte_array = bytearray([65,66,67])
print(byte_array)
byte_array[0] = 88
print(byte_array)

byte_string = bytes([68,69,70])
print(byte_string)

def my_function():
    return 42
print(callable(my_function))
print(callable(42))








