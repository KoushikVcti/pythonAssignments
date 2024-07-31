# studentRecord.py
import csv

class studentScore:
   
   
    def __init__(self, csv_file):
        self.csv_file = csv_file



   
   
    def RetriveStudentScore(self, Rollno):
            with open(self.csv_file, mode='r', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for key in csv_reader:
                    if key['Rollno'] == str(Rollno):
                        return key
            return f"No records found for rollno {Rollno}"
    
    
   
   

def main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Retrieve Student Score")
            print("2. Store Student Score")
            print("3. Calculate and Update Average Scores")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                rollno_to_search = input("Enter RollNo to search: ").strip()
                result = self.RetriveStudentScore(rollno_to_search)
                print(result)
            elif choice == '2':
                self.store_student_score()
            elif choice == '3':
                self.calculate_average_scores()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")


def store_student_score(self):
        student_data = {
            'Rollno': '',
            'Name': '',
            'English': '',
            'Maths': '',
            'Science': ''
        }

        while True:
            print("\nStore Student Score Menu")
            print("a. Enter RollNo")
            print("b. Enter student name")
            print("c. Enter English score")
            print("d. Enter Maths score")
            print("e. Enter Science score")
            print("f. Save")
            print("g. Back")
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'a':
                student_data['Rollno'] = input("Enter RollNo: ").strip()
            elif choice == 'b':
                student_data['Name'] = input("Enter student name: ").strip()
            elif choice == 'c':
                student_data['English'] = input("Enter English score: ").strip()
            elif choice == 'd':
                student_data['Maths'] = input("Enter Maths score: ").strip()
            elif choice == 'e':
                student_data['Science'] = input("Enter Science score: ").strip()
            elif choice == 'f':
                missing_fields = [key for key, value in student_data.items() if not value]
                if missing_fields:
                    print(f"Failed to store data, following parameters missing: {', '.join(missing_fields)}")
                else:
                    try:
                        with open(self.csv_file, mode='a', encoding='utf-8-sig', newline='') as file:
                            csv_writer = csv.DictWriter(file, fieldnames=student_data.keys())
                            csv_writer.writerow(student_data)
                        print("Student data stored successfully")
                        break  
                    except Exception as e:
                        print(f"An error occurred while storing data: {e}")
            elif choice == 'g':
                break  
            else:
                print("Invalid choice, please try again.")

    