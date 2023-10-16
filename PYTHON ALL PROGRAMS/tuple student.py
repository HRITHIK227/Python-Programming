students = [
    (101,"Alice",22,"Female",("Math","Physics","Chemistry")),
    (102,"Bob",21,"Male",("Math","History")),
    (103,"Charlie",23,"Male",("English","Biology","Computer Science")),\
    (104,"David",20,"Male",("Math","Physics")),
    (105,"Eve",22,"Female",("History","Biology")),]

def average_age(students):
    total_age = sum(student[2] for student in students)
    return total_age/len(students)
print("Average Age:",average_age(students))
