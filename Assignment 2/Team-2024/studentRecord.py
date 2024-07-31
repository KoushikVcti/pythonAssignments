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

