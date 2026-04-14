'''
1. Write a Python program that iterates over elements as many times as its count.
Sample Output: ['p', 'p', 'p', 'p', 'q', 'q']
'''
list_p = ["p, " * 4]
list_q = ["q, " * 2]
list_p.extend(list_q)
print(list_p)

'''
2. Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]
'''

text = "lkseropewdssafsdfafkpwe"

# Count frequencies using a dictionary
counts = {}
for char in text:
    # plus 1 so that the index starts from 1 not 0
    counts[char] = counts.get(char, 0) + 1
print(counts)

# Convert dictionary to a tuples
items = list(counts.items())

# Sort by count in descending order
def get_count(item):
    return item[1]

items.sort(key=get_count, reverse=True)
print(items)

# 5. Get the top three
result = items[:3]

print("Original string:", text)
print("Most common three characters of the said string:")
print(result)

'''
3. Write a Python program to create a new deque with three items and iterate over the deque's elements.
Scripting Languages. Sample Output:
a
e
i
o
u
'''
thistuple = ("a", "e", "i", "o", "u")
for x in thistuple:
    print(x)

'''
4. Write a Python program to find the occurrences of the 10 most common words in a given text.
Sample Output:
[('Python', 6), ('the', 6), ('and', 5), ('We', 2), ('with', 2),
('The', 1), (' Software', 1), ('Foundation', 1), ('PSF', 1), ('is', 1)]
'''
text = """Python is the the the the the the Python Python
        Python Python Python and and and and and We We with
        with The  Software Foundation PSF is"""

# .split() automatically handles multiple spaces and newlines
words = text.split()

# Count word frequencies using a dictionary
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Convert dictionary to a tuples (word, count)
items = list(word_counts.items())

#Define a simple function to return the count for sorting
def get_frequency(item):
    return item[1]

# Sort the list by frequency in descending order
items.sort(key=get_frequency, reverse=True)

# Slice to get the top 10 most common words
result = items[:10]

print("Most common ten words of the said text:")
print(result)
