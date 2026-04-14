'''
5. Write a Python program that accepts some words and counts the number of distinct words.
Print the number of distinct words and the number of occurrences of each distinct word
according to their appearance.
Input number of words: 5
Input the words:
Red
Green
Blue
Black
White
5
1 1 1 1 1
'''
# get input for the user
text = input("please enter some 5 words: ")
# since what the user gives as input is a string we use the split function to separate them
words = text.split()
count = {}
total_count = 0
for word in words:
    count[word] = count.get(word, 0) + 1
    total_count = total_count + 1
print(total_count)
x = count.values()
print(x)

'''
6. Write a Python program that accepts the number of subjects, subject names and marks.
Input the number of subjects and then the subject name and marks separated by a space on the next line.
Print the subject name and marks in order of appearance.
Sample Output:
Powered by
Number of subjects: 3
Input Subject name and marks: Bengali 58
Input Subject name and marks: English 62
Input Subject name and marks: Math 68
Bengali 58
English 62
Math 68
'''
n = int(input("Enter the number of entries: "))
d = {input("Enter key: "): input("Enter value: ") for i in range(n)}

print(d)

