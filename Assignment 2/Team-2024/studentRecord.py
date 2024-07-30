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
    
    
   
   



