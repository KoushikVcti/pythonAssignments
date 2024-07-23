# studentRecord.py
import csv

class studentScore:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def RetriveStudentScore(self, Rollno):
            with open(self.csv_file, mode='r', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                # Print the field names to debug column names
                
                for row in csv_reader:
                    # Print each row to debug
                    
                    if row['Rollno'] == str(Rollno):
                        return row
            return f"No records found for rollno {Rollno}"
       