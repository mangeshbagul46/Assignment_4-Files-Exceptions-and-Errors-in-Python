# ASSIGNMENT 4:
# Module 5: Files, Exceptions, and Errors in Python


# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

file_1 = open("sample.txt", "r")
read_line = file_1.read()
print(read_line)
file_1.close()

# # Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


user_input = input("Enter text to write to the file")

file = open("output.txt","w")
file.write(user_input + "\n")
print("Data succesfully writen to the output.txt")

additional_input = input("Enter additional input to append")
file = open("output.txt", "a")
file.write(additional_input + "\n")
print("Data succesfully append")

print("Final content of output.txt")
file = open("output.txt", "r")
reading_file = file.read()
print(reading_file)
file.close()