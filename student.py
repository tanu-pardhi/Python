print("----WELCOME STUDENT MANEGMENT SYSTEM----")
print("\n1.Add Student")
print("2.Show Student")
print("3.Delete Student")
print("4.Update Student")
print("5.Search Student")
print("0.exit\n")
class Student:
 def add_student(self,name="none",roll="none",marks=0):
    self.name=name
    self.roll=roll
    self.marks=marks
    name=input("Enter name of Student")
    roll=int(input("Enter roll no of the student"))
    marks=int(input("Enter marks of the Student"))
    student={"name":name,"roll":roll,"marks":marks}
    student.append(student)
    print("student added succesfully")
s=Student()
s.add_student()

def delete_student():
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted!")
            return
    print("Student not found!")
a=Student()
a.delete_student() 

