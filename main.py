def copy_students():
    with open('Students.txt', 'r') as source_file:
        students = source_file.readlines()  
    with open('Students_copy.txt', 'w') as target_file:
        target_file.writelines(students)  

def search_student():
    student_name = input("Ism-familiya kiriting: ")
    
    with open('Students_copy.txt', 'r') as file:
        students = file.readlines()  
    
    if student_name + '\n' in students:
        print(student_name) 
    else:
        print("Bunday student mavjud emas") 

copy_students()

search_student()
