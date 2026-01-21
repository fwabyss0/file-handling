#q.4
'''def extract_firstwords(f):
    first_words = []
    
    with open(f, 'r') as file:
        for line in file:
            words = line.strip().split()
            if words:                
                first_words.append(words[0])
    
    return first_words
result = extract_firstwords('sample.txt')
print(result)'''

#q.2
'''def copy_file(f):
    with open(f, "r") as f1, open("b.txt", "w") as f2:
          for line in f1:
                 f2.write(line)
copy_file('a.txt')
print("File copied successfully.")'''

#q.3
'''def count_line(f):
   with open(f, "r") as file:
       line_number = 1  
       for line in file:
            words = line.split()         
            word_count = len(words)  
            print(f"Line {line_number}: {word_count} words")
            line_number += 1  
count_line("sample.txt")     '''      





