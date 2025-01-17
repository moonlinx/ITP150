"""
Name: Devin Delaney
In this lab, we are going develop an application which will read in a document and produce a word count
representing the frequency of each word within the text. We’ll create a dictionary; where the key will
be a word and the value will be a count of how many times it appears in the text. At the end, we’ll sort
the dictionary so that the highest frequency words are displayed first.

1. Open the file and read in all lines into a List of sentences (Slide 5)
2. Create an empty dictionary
3. For each sentence: (Slide 6)
a. Use strip() to get rid of all preceeding and trailing white spaces and the carriage return
(‘\n’) (Slide 7)
b. Use lower() to convert all words within the sentence to lower case
c. Use replace() to get rid of all puncuation
Note: use sentence.replace(‘,’, ‘’) to remove all commas
d. Finally call split() to convert the sentence into a list of words
A. Traverse the list of words: (Slide 9)
i. Check to see if the word is already in the dictionary. If not, create an
dictionary entry (key = word, value = 1). If the word is in the dictionary,
increment the count.
4. After you have processed all the sentences within the file, you will need to sort the dictionary in
reverse order using the value (counts) as the sorting key. The following command will create a
sorted list of tuples: (key, count)
sortedDict = sorted(wordDictionary.items(),
key=lambda x: x[1],
reverse=True)
The output will be a list of tuples in sorted order:
[ (the, 77), (of, 76), (to, 65), (and, 57) .... ]
5. Open a file to write the output: (use processFile.py in Module 7 as an example on how to open
and write to a file)
6. Traverse of list of tuples
7. Write to the file.
8. Finally, close the file.
"""


def count_words():
    fileHandle = open("example.txt")
    lst: list = list(fileHandle)
    print(lst)

    word_count: dict = {}

    for line in lst:
        line = line.strip()  # removes leading and trailing whitespaces
        line = line.lower()  # make everything lower case
        line = (
            line.replace(".", "").replace(",", "").replace("!", "")
        )  # replace characters
        words = line.split()  # uses a delimeter to create a list

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        for word, count in word_count.items():
            print(f"{word}: {count}")

    sortedDict = sorted(word_count.items(), key=lambda x: x[1], reverse=True)


"""
Multiple methods for strings:
    strip() -> removes leading and trailing whitespaces
    lower() -> make everything lower case
    replace() -> replace characters
    split() -> uses a delimeter to create a list
"""
