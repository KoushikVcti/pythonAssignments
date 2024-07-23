# main.py
from studentRecord import studentScore

# Create an instance of studentScore
student_record = studentScore('Student_details.csv')

# Example roll number to retrieve
rollno_to_search = 6

# Retrieve student score
result = student_record.RetriveStudentScore(rollno_to_search)

# Print the result
print(result)
