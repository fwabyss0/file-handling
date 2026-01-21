#q.1
def extract_firstwords(f):
    first_words = []
    
    with open(f, 'r') as file:
        for line in file:
            words = line.strip().split()
            if words:                
                first_words.append(words[0])
    
    return first_words
result = extract_firstwords('sample.txt')
print(result)

#q.2
def copy_file(f):
    with open(f, "r") as f1, open("b.txt", "w") as f2:
          for line in f1:
                 f2.write(line)
copy_file('a.txt')
print("File copied successfully.")

#q.3
def count_line(f):
   with open(f, "r") as file:
       line_number = 1  
       for line in file:
            words = line.split()         
            word_count = len(words)  
            print(f"Line {line_number}: {word_count} words")
            line_number += 1  
count_line("sample.txt")     
   
#q.4
def count_line(f):
    with open(f, "r") as file:
        line_counts=0
        for line in file:
            line_counts += 1
            print("Total number of lines in story:", line_counts)
count_line("sample.txt")

#q.5
def copy_python_lines(f):
    with open(f, "r") as source, open("management.txt", "w") as destination:
        for line in source:
            if "Python" in line:
                destination.write(line)
copy_python_lines("employee.txt")
print("File copied successfully.")

#q.6
def write_squares(f):
    with open(f, "r") as source, open("squared.txt", "w") as destination:
        for line in source:
            number = int(line.strip())
            square = number * number
            destination.write(str(square) + "\n")
write_squares("numbers.txt")

#q.7
def add_to_history():
    message = input("Enter a message: ")
    with open("history.log", "a") as file:
        file.write(message + "\n")

add_to_history()

#q.8
def capitalize_file(f):
    with open(f, "r") as source, open("output.txt", "w") as destination:
        for line in source:
            destination.write(line.upper())

capitalize_file("input.txt")





