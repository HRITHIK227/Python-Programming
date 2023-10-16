my_list = [1,2,3,4,5,6]

def change_value(my_list):
    my_list[3] = 30
    print("Value inside the list:",my_list)
    print("Address is:",id(my_list))
    return
print("Before function call,my_list:",my_list)
print("Address:",id(my_list))
change_value(my_list)
print("After function call,my_list:",my_list)
print("Address:",id(my_list))
                                  
