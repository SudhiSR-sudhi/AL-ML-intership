"""The main menu program."""


import students
from faculty import add_teacher, get_teacher
import attendence as att
import results as res

def main():
    while True:
        print("\n--- COLLEGE MENU ---")
        print("1. Add Student      2. Find Student      3. Total Students")
        print("4. Add Teacher      5. Find Teacher      6. Add Attendance")
        print("7. Check Exam OK    8. Add Mark          9. Check Grade & Scholarship")
        print("10. Exit")
        
        choice = input("Choose an option (1-10): ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            print(students.add_student(sid, name)) 

        elif choice == "2":
            sid = input("Enter Student ID: ")
            print("Name:", students.get_student(sid)) 

        elif choice == "3":
            print("Total Students:", students.count_students()) 

        elif choice == "4":
            tid = input("Enter Teacher ID: ")
            name = input("Enter Teacher Name: ")
            print(add_teacher(tid, name))

        elif choice == "5":
            tid = input("Enter Teacher ID: ")
            print("Name:", get_teacher(tid)) 

        elif choice == "6":
            sid = input("Enter Student ID: ")
            pct = input("Enter Attendance %: ")
            print(att.add_attendance(sid, pct)) 

        elif choice == "7":
            sid = input("Enter Student ID: ")
            print(att.check_exam_ok(sid)) 

        elif choice == "8":
            sid = input("Enter Student ID: ")
            mark = input("Enter Mark (0-100): ")
            print(res.add_mark(sid, mark))

        elif choice == "9":
            sid = input("Enter Student ID: ")
            print("Status:", res.get_grade(sid)) 
            print("Scholarship:", res.check_scholarship(sid)) 

        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
