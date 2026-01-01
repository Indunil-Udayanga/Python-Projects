Students = [
    {"ID": 1, "Name": "Indunil", "Age": 23, "Course": "Computer Science"},
    {"ID": 2, "Name": "Praveen", "Age": 22, "Course": "Computer Science"},
    {"ID": 3, "Name": "Dinuka", "Age": 21, "Course": "Computer Science"},
    {"ID": 4, "Name": "Nimeh", "Age": 24, "Course": "Computer Science"}
]

def Add_Students(Students,):
    
    ID = int(input("Enter the Student ID :"))
    Name = input("Enter student Name :")
    Age = int(input("Enter the Student Age :"))
    Course = input("Enter student Course :")

    Student = {
               "ID":ID,
               "Name":Name,
               "Age" : Age,
               "Course" : Course
               }
    Students.append(Student)

def View_Students(Student):
    for Student in Students:
        for key,value in Student.items():
            print(f"{key} : {value}")

def Search_Students(Students):
    Search_ID = int(input("Enter ID to Search :"))

    for student in Students:
        if student['ID'] == Search_ID:
            print("Name :",student['Name'])
            print("Age :",student['Age'])
            print("COurse :",student['Course'])

        else:
            print("Student not found!")


def Update_Student(Students):
    Update_id = int(input("Enter ID to Update :"))

    for student in Students:
        if student['ID'] == Update_id:
            student['Name'] =input("Enter student Name :")
            student['Age'] =int(input("Enter student Name :"))
            student['Coursee'] =input("Enter student Course :")
            print("✅ Student updated!")
            
        else:
            print("Student not found!")

def Delete_student(Students):
    delete_id = int(input("Enter ID to delete : "))

    for student in Students:
        if student["ID"] == delete_id:
            Students.remove(student)
            print("Student deleted!")
            return

    print("❌ Student not found")

def Menu():
    print("--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def Main(Students):
    while True:
        Choice = int(input("Enter Choice :"))
        match Choice:
            case 1:
                Add_Students(Students)
            case 2:
                View_Students(Students)
            case 3:
                Search_Students(Students)
            case 5:
                Delete_student(Students)
            case 6:
                print("👋 Exiting program...")
                break
            case _:
                print("Invalid Choice !")

Menu()
Main(Students)