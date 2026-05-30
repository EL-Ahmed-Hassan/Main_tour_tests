# The math formula for area and cricumference of a circle is A = pi * r^2 and C = 2 * pi * r respectively.
# The math formula for the factorial of a number is n! = n * (n-1) * (n-2) * ... * 1.
# The math formula for the number of permutations of a set of n objects is P(n) = n!.
# The math formula for the number of combinations of a set of n objects taken r at a time is C(n, r) = n! / (r! * (n-r)!).
# The math formula for the number of arrangements of a set of n objects is A(n) = n!.
# The math formula for the number of arrangements of a set of n objects taken r at a time is A(n, r) = n! / (n-r)!.
# The math formula for the number of arrangements of a set of n objects taken r at a time with repetition is A(n, r) = n^r.
# The math formula for the number of arrangements of a set of n objects taken r at a time with repetition is A(n, r) = n^r.
# The math formula for the number of arrangements of a set of n objects taken r at a time with repetition is A(n, r) = n^r.
# The math formula for the number of arrangements of a set of n objects taken r at a time with repetition is A(n, r) = n^r.
# import string 
# import random
# import math
# import os
# from unittest import result
# sentence = input("Enter a sentence: ")
# clean_sentence = '\n'.join(sentence.split(' ')).upper()
# print(clean_sentence)

# # find the circumference of the circle
# r = float(input("Enter the radius of the circle: "))
# #Remember that the formula for the circumference of a circle is C = 2 * pi * r
# C = 2 * math.pi * r
# print("The circumference of the circle is: ", C)

# # guess a Number
# number =random.randint(0, 10)
# guess = int(input("Guess a number between 0 and 10: "))
# while guess != number:
#     guess = int(input("Try again: "))
# print("Congratulations! You guessed the number.")

# r = random.randint(1, 100)
# area = float(math.ceil(math.pi * r**2))
# print("The area of the circle is: ", area)

# list = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.sample(list, 8))
# factorial = math.factorial(len(password))
# print("Your password is: ", password)
# print("The factorial of the password length is: ", factorial)

# #login system
# username = input("Enter your name: ")
# password = input("Enter your password: ")
# while username != "admin" or password != "password":
#     print("Invalid username or password.")
#     username = input("Enter your name: ")
#     password = input("Enter your password: ")
# print("Welcome, admin!")

# #sign up system
# new_username = input('Enter a new username: ')
# generate_password = input("Do you want to generate a strong password? (y/n): ").lower()
# if generate_password == 'y':
#     new_password = ''.join(random.sample(list, 12))
#     print("Your new username is: ", new_username)
#     print("Your new password is: ", new_password)
# else:
#     new_password = input('Enter a new password: ')
#     print("Your new username is: ", new_username)
#     print("Your new password is: ", new_password)
    
# # multiplication table
# number = int(input("Enter the number that you want to multiply: "))
# for i in range(1, 21):
#     result = number * i
#     print(f"{number} x {i} = {result}") 

# prime number checker
# number = int(input("Enter a number: "))
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")  

# caesar cipher
# def encrypt(text, shift):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if char.isupper():
#             result += chr((ord(char) + shift - 65) % 26 + 65)
#         elif char.islower():
#             result += chr((ord(char) + shift - 97) % 26 + 97)
#         else:
#             result += char
#     return result
#     print

# text = input("Enter a message to encrypt: ")
# shift = int(input("Enter the shift value: "))
# encrypted_text = encrypt(text, shift)
# print("Encrypted message: ", encrypted_text)

# # decryption
# def decrypt(text, shift):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if char.isupper():
#             result += chr((ord(char) - shift - 65) % 26 + 65)
#         elif char.islower():
#             result += chr((ord(char) - shift - 97) % 26 + 97)
#         else:
#             result += char
#     return result
# encrypted_text = input("Enter a message to decrypt: ")
# shift = int(input("Enter the shift value: "))
# decrypted_text = decrypt(encrypted_text, shift)
# print("Decrypted message: ", decrypted_text)

# # fibonacci sequence
# def fibonacci(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# fib_sequence = fibonacci(n)
# print("Fibonacci sequence: ", fib_sequence)

# oprations on dictionary
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# # add a new key-value pair
# my_dict["country"] = "USA"
# # update an existing key-value pair
# my_dict["age"] = 31
# # delete a key-value pair
# del my_dict["city"]
# # access a value by key
# name = my_dict["name"]
# print("Name: ", name)
# # print the entire dictionary
# print("Dictionary: ", my_dict)

# math modules
#from numpy import info
# num = 12.3
# number = float(input("Enter a number: "))
# print(f"\n\nMath operations on {number}:\n")
# print("Square root: ", math.sqrt(number))
# print("Sine: ", math.sin(number))
# print("Cosine: ", math.cos(number))
# print("Tangent: ", math.tan(number))
# print("Logarithm: ", math.log(number))
# print("Exponential: ", math.exp(number))
# print("Pi: ", math.pi)
# print("Euler's number: ", math.e)
# print("Factorial: ", math.factorial(int(number)))
# print("Greatest common divisor: ", math.gcd(int(number), int(num)))
# print("Least common multiple: ", math.lcm(int(number), int(num)))
# print("Degrees to radians: ", math.radians(number))
# print("Radians to degrees: ", math.degrees(number))
# print("Hypotenuse: ", math.hypot(number, num))
# print("Combination: ", math.comb(int(number), int(num)))
# print("Permutation: ", math.perm(int(number), int(num)))
# print("Is finite: ", math.isfinite(number))
# print("Is infinite: ", math.isinf(number))
# print("Is NaN: ", math.isnan(number))
# print("Trigonometric functions: ", math.sin(number), math.cos(number), math.tan(number))
# print(f"\n\nOther math operations on {number}:\n")


# لعبة حجرة ورقة مقص 
# sel = ["حجرة", "ورقة", "مقص"]
# print(f"*********مرحبا بكم في لعبة حجرة ورقة مقص**********\n")
# com_choice = random.choice(sel)
# user_choice = input("اختر: (حجرة) (ورقة) (مقص)  ")
# if user_choice == com_choice:
#     print(f"الكمبيوتر اختار {com_choice}, إنه تعادل")
# elif user_choice == "حجرة" and com_choice == "مقص" or user_choice == "مقص" and com_choice == "ورقة" or user_choice == "ورقة"  and com_choice == "حجرة":
#   print(f"الكمبيوتر اختار  ({com_choice}) , تهاني لقد فزت")
# elif user_choice == "حجرة" and com_choice == "ورقة" or user_choice == "ورقة"  and com_choice == "مقص" or user_choice == "مقص" and com_choice == "حجرة":
#     print(f"الكمبيوتر اختار ({com_choice}) , أسف لقد خسرت")

#school system
# students = {"name": ["mohsen", "ahmed", "sara"],
#             "age": [20, 22, 21],
#             "grade": ["A", "B", "A"],
#             "subjects": [["math", "science", "english"], ["math", "science", "history"], ["math", "science", "geography"]],
#             "attendance": [90, 85, 95]}
# for i in range(len(students["name"])):
#     print("----------------------------------- ")
#     print(f"Student Name: {students['name'][i]}")
#     print(f"Age: {students['age'][i]}")
#     print(f"Grade: {students['grade'][i]}")
#     print(f"Subjects: {', '.join(students['subjects'][i])}")
#     print(f"Attendance: {students['attendance'][i]}%\n")
#     print("-------------------------------------")

# contact management system
# contacts = {}
# print(f"*************Welcome to the Contact Management System************\n")
# while True:
#     print("1. Add a contact")
#     print("2. View contacts")
#     print("3. Search for a contact")
#     print("4. Edit a contact")
#     print("5. Delete a contact")
#     print("6. Exit")
#     print("---------------------------------------------")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         name = input("Enter the contact's name: ")
#         phone = input("Enter the contact's phone number: ")
#         email = input("Enter the contact's email address: ")
#         contacts[name] = {"phone": phone, "email": email}
#         print(f"Contact {name} added successfully!\n")
#     elif choice == "2":
#         if not contacts:
#             print("No contacts found.\n")
#         else:
#             print("Contacts:")
#             for name, info in contacts.items():
#                 print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
#             print()
#     elif choice == "3":
#         search_name = input("Enter the name of the contact to search for: ")
#         if search_name in contacts:
#             print(f"Contact found: Name: {search_name}, Phone: {contacts[search_name]['phone']}, Email: {contacts[search_name]['email']}\n")
#         else:
#             print("Contact not found.\n")
#     elif choice == "4":
#         edit_name = input("Enter the name of the contact to edit: ")
#         if edit_name in contacts:
#             print(f"Editing contact: Name: {edit_name}, Phone: {contacts[edit_name]['phone']}, Email: {contacts[edit_name]['email']}")
#             new_phone = input("Enter the new phone number (or press Enter to keep the current one): ")
#             new_email = input("Enter the new email address (or press Enter to keep the current one): ")
#             if new_phone:
#                 contacts[edit_name]['phone'] = new_phone
#             if new_email:
#                 contacts[edit_name]['email'] = new_email
#             print(f"Contact {edit_name} updated successfully!\n")
#         else:
#             print("Contact not found.\n")
#     elif choice == "5":
#         delete_name = input("Enter the name of the contact to delete: ")
#         if delete_name in contacts:
#             del contacts[delete_name]
#             print(f"Contact {delete_name} deleted successfully!\n")
#         else:
#             print("Contact not found.\n")
#     elif choice == "6":
#         print("Exiting the Contact Management System. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.\n")

# tic-tac-toe game
# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9) 
# def check_winner(board, player):
#     for row in board:
#         if all(s == player for s in row):
#             return True
#     for col in range(3):
#         if all(board[row][col] == player for row in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)):
#         return True
#     if all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False
# def tic_tac_toe():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"
#     while True:
#         print_board(board)
#         row = int(input(f"Player {current_player}, enter the row (0-2): "))
#         col = int(input(f"Player {current_player}, enter the column (0-2): "))
#         if board[row][col] == " ":
#             board[row][col] = current_player
#             if check_winner(board, current_player):
#                 print_board(board)
#                 print(f"Congratulations! Player {current_player} wins!")
#                 break
#             current_player = "O" if current_player == "X" else "X"
#         else:
#             print("That cell is already occupied. Please try again.")
# tic_tac_toe()

# guess game
# print(f"****** Welcome To Guess words Letter Game *******\n")
# words = ["Agouna", "Lion", "Banda", "Monkey"]
# computer_guess = random.choice(words)
# # make spaces for the letters
# display = ["_" for _ in computer_guess]
# print(" ".join(display))
# while "_" in display:
#     user_guess = input("Guess a letter: ").lower()
#     for i in range(len(computer_guess)):
#         if computer_guess[i].lower() == user_guess:
#             display[i] = computer_guess[i]
#     print(" ".join(display))
# print(f"congratulations! You guessed the word: {computer_guess}")

# calculator
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     if y == 0:
#         return "Error: Division by zero is not allowed."
#     return x / y
# print(f"********* Welcome To Simple Calculator **********\n")
# while True:
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#     choice = input("Enter your choice (1-5): ")
#     if choice == "5":
#         print("Exiting the calculator. Goodbye!")
#         break
#     if choice in ["1", "2", "3", "4"]:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         if choice == "1":
#             print(f"{num1} + {num2} = {add(num1, num2)}\n")
#         elif choice == "2":
#             print(f"{num1} - {num2} = {subtract(num1, num2)}\n")
#         elif choice == "3":
#             print(f"{num1} * {num2} = {multiply(num1, num2)}\n")
#         elif choice == "4":
#             result = divide(num1, num2)
#             if isinstance(result, str):
#                 print(result + "\n")
#             else:
#                 print(f"{num1} / {num2} = {result}\n")
#     else:
#         print("Invalid choice. Please try again.\n")

# Task manager
# tasks = []
# def add_task(task):
#     tasks.append(task)
#     print(f"Task '{task}' added successfully!\n")
# def view_tasks():
#     if not tasks:
#         print("No tasks found.\n")
#     else:
#         print("Tasks:")
#         for i, task in enumerate(tasks, 1):
#             print(f"{i}. {task}")
#         print()
# def delete_task(task_number):
#     if 0 < task_number <= len(tasks):
#         removed_task = tasks.pop(task_number - 1)
#         print(f"Task '{removed_task}' deleted successfully!\n")
#     else:
#         print("Invalid task number. Please try again.\n")
# print(f"********* Welcome To Task Manager **********\n")
# while True:
#     print("1. Add a task")
#     print("2. View tasks")
#     print("3. Delete a task")
#     print("4. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         task = input("Enter the task description: ")
#         add_task(task)
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         view_tasks()
#         task_number = int(input("Enter the task number to delete: "))
#         delete_task(task_number)
#     elif choice == "4":
#         print("Exiting the Task Manager. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.\n")
        
# a math practice program
#def math_practice():
#    print(f"********* Welcome To Math Practice **********\n")
#    while True:
#        num1 = random.randint(1, 10)
#        num2 = random.randint(1, 10)
#       operation = random.choice(["+", "-", "*", "/", "pow", "ceil", "floor", "gcd", "lcm"])
#       if operation == "+":
#            correct_answer = num1 + num2
#        elif operation == "-":
#            correct_answer = num1 - num2
#        elif operation == "*":
#            correct_answer = num1 * num2
#        elif operation == "/":
#            correct_answer = round(num1 / num2, 2)
#        elif operation == "pow":
#            correct_answer = num1 ** num2
#        elif operation == "ceil":
#            correct_answer = math.ceil(num1 / num2)
#        elif operation == "floor":
#            correct_answer = math.floor(num1 / num2)
#       elif operation == "gcd":
#            correct_answer = math.gcd(num1, num2)
#        elif operation == "lcm":
#            correct_answer = math.lcm(num1, num2)
#        user_answer = input(f"What is {num1} {operation} {num2}? ")
#        try:
#            user_answer = float(user_answer)
#            if user_answer == correct_answer:
#                print("Correct! Well done!\n")
#            else:
#               print(f"Incorrect. The correct answer is {correct_answer}.\n")
#       except ValueError:
#           print("Invalid input. Please enter a number.\n")

# user_iput = input("What opratotion do you want to do?, (+), (-), (/), (*), (gcd): ")
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if user_iput == "+":
#     result = num1 + num2
#     print(f"{num1} + {num2} = {result} \n")
# elif user_iput == "-":
#     result = num1 - num2
#     print(f"{num1} - {num2} = {result}")
# elif user_iput == "/":
#     if num2 == 0:
#         print("This oprattion can not done, Enter a number older than 0 please")
#         num2 = int(input("Enter the second number: "))
#     else:
#         result = num1 / num2
#         print(f"{num1} / {num2} = {result}")
# elif user_iput == "*":
#     result = num1 * num2
#     print(f"{num1} * {num2} = {result}")
# elif user_iput == "gcd":
#     result = math.gcd(num1, num2)
#     print(f"the gcd for {num1} and {num2} is {result}")
# else:
#     print("Enter a valid number opration...")

# sugestions for more programs:
# 1. A weather app that fetches and displays the current weather for a given location.
# 2. A to-do list application that allows users to add, view, and delete tasks.
# 3. A currency converter that converts between different currencies using real-time exchange rates.
# 4. A unit converter that converts between different units of measurement (e.g., length, weight, temperature).
# 5. A BMI calculator that calculates and categorizes a person's Body Mass Index based
# on their height and weight.

# comtacts managment
# contacts = {}
# while True:
#     print(f"\n************** Contacts Mangments System ****************\n")
#     print("1. add Contact")
#     print("2. Edit contact")
#     print("3. Veiw all Contacts")
#     print(f"4. Exit\n")
#     user_input = input("what your choice: ")
#     if user_input == "1":
#         contact_id = input("Enter the ID of the contact: ")
#         if contact_id in contacts:
#             print(f"the contact has alrady existed....")
#         else:
#            contact_name = input("Enter the name of the contact: ")
#            contact_phone = input("Enter the number of the contact: ")
#            contacts[contact_id] = {
#             "name": contact_name,
#             "phone": contact_phone,
#             }
#         print(f"{contact_name} was add sucssfully.....")
#     elif user_input == "2":
#       id_to_edit = input("Enter the ID of contact to edit: ")
#       while id_to_edit not in contacts:
#             print(f"{id_to_edit} was not found...")
#             id_to_edit = input("Enter the ID of contact to edit: ")
#       new_name = input("Enter a new name: ")
#       new_phone = input("Enter a new phone: ")
#       contacts[id_to_edit] = {
#           "name": new_name,
#           "phone": new_phone
#       }
#       print(f"{new_name} was edit sucssfully....")
#     elif user_input == "3":
#         print(contacts)
#     elif user_input == "4":
#         print("Exising.......")
#         break
#     else:
#         print(f" {user_input} was not valid..")
    

# # Guess a number
# computer_choice = random.randint(1, 10)
# def clear():
#     os.system("cls" if os.name == "nt" else "clear")
# while True:
#     clear()
#     guess_num = int(input("Guess a number bettween 1, 10: "))
#     if guess_num == computer_choice:
#         print("congralat, you guess the number!!") 
#         break
#     else:
#         print("wrong guess, try again") 
#         input("press any key to countue.....")

#****************************************************************************************


# budegt calculator
# #first we need to import the os module to clear the screen
# import os

# # we will create a function to clear the screen
# def clear():
#    """تقوم الوظيفة بمسح كل ما هو موجود في الشاشة 
#    سواء كان نظام التشغيل ويندوز او لينكس او ماك
#    """
   
#    os.system("cls" if os.name == "nt" else "clear")
# # we will create a function to calculate the budget
# def calculate_budget(quantity, price_per_item):
#    """
#    تقوم بتمرير متغيرين للوظفية
#    الكمية و سعر المنتج
#    و هي تقوم بضربهما لحساب التكلفة الكلية
#    """
#    return quantity * price_per_item

# # we will create a loop to run the program until the user wants to exit
# while True:
#         clear()
#         print(f"********* Welcome To Budget Calculator **********\n")
#         total_budegt = float(input("Enter your whole budegt: "))
#         item_name = input("Enter your item you want to buy: ")
#         quantity = int(input(f"How many {item_name}s do you want to buy? "))
#         price_per_item = float(input(f"Enter the price of each {item_name}: "))
#         total_cost = calculate_budget(quantity, price_per_item)
#         if total_cost > total_budegt:
#            print(f"sorry, your budgt is {total_budegt}$, but your bill is {total_cost}$")
#         else:
#            print(f"succssfull, you can buy {quantity} {item_name}s for {total_cost}$, and you will have {total_budegt - total_cost}$ left")
#         if  input("Do you want to continue: (y) or (n): ") != "y":
#            clear()
#            print("Exiting the Budget Calculator..... Goodbye!")
#            break


# tax calculator
# def calculate_tax(income):  
#     """تقوم الوظيفة بحساب الضريبة بناءً على الدخل المدخل
#     و تعيد قيمة الضريبة المستحقة
#     """
#     return income * 0.15

# # calculate the final salary after bouns and tax
# def calculate_final_salary(income, bonus):
#     """تقوم الوظيفة بحساب الراتب النهائي بعد خصم الضريبة و البونص
#     و تعيد قيمة الراتب النهائي
#     """
#     tax = calculate_tax(income)
#     final_salary = income + bonus - tax
#     return final_salary 

# # we will create a loop to run the program until the user wants to exit
# while True:
#     print(f"********* Welcome To Tax Calculator **********\n")
#     income = float(input("Enter your income: "))
#     bonus = float(input("Enter your bonus: "))
#     final_salary = calculate_final_salary(income, bonus)
#     print(f"Your final salary after tax and bonus is: {final_salary}$")
#     if input("Do you want to continue: (y) or (n): ") != "y":
#         print("Exiting the Tax Calculator..... Goodbye!")
#         break # final edite 5/30/2026 12:40 pm

# check if email is valid
import time
name = input("Enter your name: ")
email= input("Enter your email: ")
def is_valid_email(email):
    """تقوم الوظيفة بالتحقق من صحة البريد الإلكتروني المدخل
    و تعيد True إذا كان البريد الإلكتروني صالحًا، و False إذا كان غير صالح
    """
    if "@" and "." in email:
        return True
    return False

if is_valid_email(email):
    print("Checking the email validity...")
    time.sleep(2) # simulate checking the email validity
    print("The email is valid.")
else:
    print("Checking the email validity...")
    time.sleep(2) # simulate checking the email validity
    print("The email is not valid.")