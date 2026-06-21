import numpy as np
import json

students = []

def save_marks():
    with open("marks.json" , "w") as file:
        json.dump(students , file , indent=4)

def load_marks():
    global students
    try:
        with open("marks.json" , "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


def add_student():
    name = input("Enter the name of the student: ")
    english = int(input("Enter the marks of english subject: "))
    maths = int(input("Enter the marks of maths subject: "))
    science = int(input("Enter the marks of science subject: "))

    marks = np.array([english , maths , science])

    student = {
        "id": len(students)+1,
        "name": name,
        "marks": marks.tolist()
    }
    students.append(student)
    
    print(f"{name} student added successfully")
    save_marks()

def display_students():
    if not students:
        print("No student found")
        return
    print("\n====Students Record====")

    for student in students:
        total = np.sum(student['marks'])
        average = np.mean(student['marks'])

        print("=" * 30)
        print(f"Id: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"English: {student['marks'][0]}")
        print(f"Maths: {student['marks'][1]}")
        print(f"Science: {student['marks'][2]}")
        print(f"Total Marks: {total}")
        print(f"Average marks: {average:.2f}")
        print("=" * 30)

def search_student():
    search_id = int(input("Enter the student id: "))

    for student in students:
        if student['id'] == search_id:
            total = np.sum(student['marks'])
            average = np.mean(student['marks'])

            print("=" * 30)
            print(f"Id: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"English: {student['marks'][0]}")
            print(f"Maths: {student['marks'][1]}")
            print(f"Science: {student['marks'][2]}")
            print(f"Total Marks: {total}")
            print(f"Average marks: {average:.2f}")
            print("=" * 30)
            return
        
    print("No student found")
                 
def update_marks():
    update_id = int(input("Enter the student id to update: "))

    for student in students:
        if student['id'] == update_id:
            new_english_marks = int(input("Enter the marks of english subject: "))
            new_maths_marks = int(input("Enter the marks of maths subject: "))
            new_science_marks = int(input("Enter the marks of science subject: "))

            updated_marks = np.array([new_english_marks , new_maths_marks , new_science_marks ])
            student['marks'] = updated_marks.tolist()
            save_marks()
            print("Marks updated successfully")
            return
        
    print("No student found")
   
def delete_student():
    delete_id = int(input("Enter the student id to delete: "))

    for student in students:
        if student['id'] == delete_id:
            students.remove(student)
            save_marks()
            print("The student deleted successfully")
            return
        
    print("No student found")
        
def student_report():
    report_id = int(input("Enter the id of the student: "))
    
    for student in students:
        if student['id'] == report_id:
            total = np.sum(student['marks'])
            average = np.mean(student['marks'])
            highest = np.max(student['marks'])
            lowest = np.min(student['marks'])

            if average >= 90:
                grade = "A"
            elif average >= 75:
                grade = "B"
            elif average >= 60:
                grade = "C"
            else:
                grade = "D"

            percentage = (total/300) * 100

            if all(mark >= 35 for mark in student['marks']):
                status = "Pass"
            else:
                status = "Fail"

            print("\n====STUDENTS RECORD====")
            print(f"Id: {student['id']}")
            print(f"Name: {student['name']} ")
            print(f"English: {student['marks'][0]}")
            print(f"Maths: {student['marks'][1]}")
            print(f"Science: {student['marks'][2]}")
            print(f"Total Marks: {total}")
            print(f"Average Marks: {average:.2f}")
            print(f"Highest Marks: {highest}")
            print(f"Lowest marks: {lowest}")
            print(f"Grade: {grade}")
            print(f"Percentage: {percentage:.2f}%")
            print(f"Status: {status}")
            print("=" *30)
            return
        
    print("No student found")
          
def find_topper():
    if not students:
        print("No student found")
        return
    
    total_topper = 0
    topper = None
    for student in students:
        total = np.sum(student['marks'])
        if total > total_topper:
            total_topper = total
            topper = student

    print(f"Topper: {topper['name']}")
    print(f"Id: {topper['id']}")
    print(f"Marks: {topper['marks']}")
    print(f"Total marks: {total_topper}")

def class_statistics():
    if not students:
        print("No student found")
        return
    totals = []
    for student in students:
        total = np.sum(student['marks'])
        totals.append(total)

    totals = np.array(totals)
    class_average = np.mean(totals)
    highest = np.max(totals)
    lowest = np.min(totals)
       

    print("\n====CLASS STATISTICS====")
    print(f"Total students: {len(students)}")
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest Total: {highest}")
    print(f"Lowest Total: {lowest}")

def subject_wise_analysis():
    if not students:
        print("No student found")
        return
    analysis_marks = []
    for student in students:
        analysis_marks.append(student['marks'])

    average = np.mean(analysis_marks , axis = 0)
    highest = np.max(analysis_marks , axis = 0)
    lowest = np.min(analysis_marks , axis = 0)

     
    print(f"\n====SUBJECT ANALYSIS====")
    print(f"English Average: {average[0]:.2f}")
    print(f"Maths Average: {average[1]:.2f}")
    print(f"Science Average: {average[2]:.2f}")
    print(f"Highest English Marks: {highest[0]}")
    print(f"Highest Maths Marks: {highest[1]}")
    print(f"Highest Science Marks: {highest[2]}")
    print(f"Lowest English Marks: {lowest[0]}")
    print(f"Lowest Maths Marks: {lowest[1]}")
    print(f"Lowest Science Marks: {lowest[2]}")

def main():
    load_marks()

    while True:
        print("\n====Students Marks Analyzer====")
        print("1. Add the student: ")
        print("2. Dispaly all the students: ")
        print("3. Search students: ")
        print("4. Update marks of students: ")
        print("5. Delete students: ")
        print("6. Student Report: ")
        print("7. The topper of class: ")
        print("8. Class statistics: ")
        print("9. Subject wise analysis: ")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter the valid number")
            continue

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_marks()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            student_report()

        elif choice == 7:
            find_topper()

        elif choice == 8:
            class_statistics()

        elif choice == 9:
            subject_wise_analysis()

        elif choice == 10:
            print("Closing the program")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




        
    

