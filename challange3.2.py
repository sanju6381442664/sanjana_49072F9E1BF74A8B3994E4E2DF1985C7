'''
implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (cumulative grade point average) in descending order. each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). test the function
with different input lists of students.
'''

class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of student in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_student


  # Example usage:
  students = [
      student("sanjana", "A123", 7.8),
      student("kavitha", "A124", 8.9),
      student("santhosh", "A125", 9.1),
      student("sri madhu", "A126", 9.9),
  ]

  sorted_students = sort_students(students)

  # print the sorted list of students
  for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                       student.roll_number,
                                                            student.cgpa))
  