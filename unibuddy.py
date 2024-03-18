# UniBuddy is a chatbot built to answer questions most commonly
# asked by new students at Imaginary University

# Define function to answer chosen question (6 input options)
def user_question(question_no):
    # If question 1 chosen:
    if question_no == '1':
        # String answer (no variations)
        answer = ("You can find your timetable online by visiting "
                  "www.imaginaryuni.com/my_timetable and entering "
                  "your student ID.")
    # If question 2 chosen:
    elif question_no == '2':
        # Dict. containing professors for each course
        tutor_dict = {'medicine': 'Professor Smith',
                      'law': 'Professor Wang',
                      'engineering': 'Professor Kim',
                      'fine art': 'Professor Devi',
                      'psychology': 'Professor Müller'
                      }
        # String answer using user input with info from dict. 
        answer = (f"Your course tutor for {course.capitalize()} "
                  f"is {tutor_dict[course]}.")
    # If question 3 chosen:
    elif question_no == '3':
        # String answer (no variations)
        answer = ("You can submit your work to be graded by visiting "
                  "www.imaginaryuni.com/submit_work and entering your "
                  "student ID.")
    # If question 4 chosen:
    elif question_no == '4':
        # Create student email using user input name and surname
        student_email = f"{student_surname}{student_name}@imaginaryuni.com"
        # String answer with email and ID
        answer = (f"Your email address is {student_email} and your temporary "
                  f"password is {student_id}.")
    # If question 5 chosen:
    elif question_no == '5':
        # Dict. containing recommended clubs based on user input for course
        clubs_dict = {'medicine': 'Innovation in Medicine Society',
                      'law': 'Lawyers Without Borders Society',
                      'engineering': 'Design Engineering Society',
                      'fine art': 'Filmmaking and Photography Society',
                      'psychology': 'Human Rights Society'
                      }
        # String answer using user input with info from dict.
        answer = (f"A full list of clubs is available at www.imaginaryuni.com"
                  f"/clubs. Many {course.capitalize()} students choose to join "
                  f"the {clubs_dict[course]}. Maybe give it a try!")
    # If question 6 chosen:
    elif question_no == '6':
        # String answer (no variations)
        answer = ("If you have any further questions please email "
                  "support@imaginaryuni.com and you will receive a "
                  "response within 48hrs.")
    return answer


# Welcome message and request student info before answering q's
print("\nHello, welcome to Imaginary University! I'm UniBuddy!")
print("I'm here to help answer your questions.")
print("But before we get started, I have a few questions to ask you.\n")

# Request student name and surname from user
while True:
    student_name = input("Please enter your first name: ").lower()
    if 2 < len(student_name) < 31 and student_name.isalpha():
        break
    else:
        print("ERROR: Invalid Input. Please check that you have entered "
              "only alphabetical characters and between 3 and 30 characters.")
        continue

while True:
    student_surname = input("Please enter your surname: ").lower()
    if 2 < len(student_surname) < 31 and student_surname.isalpha():
        break
    else:
        print("ERROR: Invalid Input. Please check that you have entered "
              "only alphabetical characters and between 3 and 30 characters.")
        continue

print(f"\nHello {student_name.capitalize()}! It's a pleasure to meet you!\n")

# Request student birth year from user
while True:
    dob_year = input("Next, please enter the year you were born (YYYY): ")
    if dob_year.isnumeric() is False:
        print("ERROR: Invalid Input. Please enter a number between 1920 "
              "and 2015.")
        continue
    elif int(dob_year) < 1920 or int(dob_year) > 2015:
        print("ERROR: Invalid Input. Please enter a number between 1920 "
              "and 2015.")
        continue
    else:
        break

# Message to user - dependent on user age  
if int(dob_year) <= 1997:
    print("\nIt's great to see you're entering university a little later "
          "in life. It's never too late to follow your dreams!")
elif int(dob_year) >= 2006:
    print("\nCongratulations on entering university at such a young age!")
else: 
    print("\nIt looks like you're a similar age to most students on your "
          "course. That's great!")

# Request students course from user
# From list of 5 courses offered by the university
courses_offered = ['medicine', 'law', 'engineering', 'fine art', 'psychology']
print("\nOne more question...")
print("At Imaginary University we offer five courses: \nMedicine, Law, "
      "Engineering, Fine Art and Psychology.")

while True:
    course = input("\nPlease enter the course you are studying: ").lower()
    if course in courses_offered:
        break
    else:
        print("ERROR: Invalid Input. Please check your spelling and "
              "try again.")
        continue

# Output student ID
# ID formed from student info (name and birth year)
print("\nThank you for taking the time to answer my questions.")
student_id = (f"iu{student_surname[-3:-1]}{student_name[0:2]}"
              f"{student_surname[0:2]}0{dob_year[2:]}0")
print(f"\nYour student ID is: {student_id}")
print("You will need to use your student ID throughout your course so "
      "please make a note of it!")

# Output list of most common questions to allow user to choose
print("\nNow it's time for me to answer your questions!"
      "\nPlease see the below list of questions I can answer.")
print("\n1. Where can I find my timetable?\
      \n2. Who is my course tutor?\
      \n3. How do I submit my work to be graded?\
      \n4. What is my student email address?\
      \n5. What extracurricular clubs can I join?\
      \n6. Other...")

# Request user select question number (1-6) and provide answer
# Any more questions? Enter number (1-6) or 'stop' to end
while True:
    question_no = (input("\nPlease select a question from the list above by "
                         "entering a number from 1 to 6, or enter 'stop' to "
                         "stop asking questions: \n")).lower()
    question_list = ['1', '2', '3', '4', '5', '6']
    
    if question_no in question_list:
        print(user_question(question_no))
        continue
    elif question_no == 'stop':
        break
    else:
        print("\nERROR: Invalid Input. Please only enter a number from 1 to 6,"
              " or enter 'stop' to stop asking questions.")
        continue

# Goodbye and thank you message 
print(f"\nThank you for using UniBuddy, {student_name.capitalize()}!")
print("Please come back any time, and I hope you enjoy your studies at "
      "Imaginary University!\n")