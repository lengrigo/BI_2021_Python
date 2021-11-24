import re
import matplotlib.pyplot as plt

# Task 1

# ftp links
ftp_pattern = re.compile(r'ftp[^;\s]+')
with open('references.txt', mode='r') as file:
    ftp_file = file.read()
    ftp = ftp_pattern.finditer(ftp_file)
    ftp_lst = []
    for i in ftp:
        ftp_lst.append(i.group())
with open('ftps.txt', mode='w') as ftps:
    ftps.write('\n'.join(ftp_lst))

# Tasks 2-5

# pattern for all numbers
all_numbers_pattern = re.compile(r'\d+[\.]*\d*')

# pattern for all words with a
a_letters_pattern = re.compile(r'\w*[a]\w*', re.IGNORECASE)

# pattern for exclamation sentences
exclamation_sentences_pattern = re.compile(r'\b[^.!?]+[!]')

# pattern for all words for histogram
hist_pattern = re.compile(r'\b\w+\b', re.IGNORECASE)

with open('2430AD.txt', mode='r') as ad_file:
    x = ad_file.read()

    # Task 2 - looking for all numbers
    numbers = all_numbers_pattern.finditer(x)
    all_numbers_answer = []  # list for saving numbers
    for i in numbers:
        all_numbers_answer.append(i.group())
    # print(all_numbers_answer)

    # Task 3 - looking for words with a
    words = a_letters_pattern.finditer(x)
    a_letters_answer = []  # list for saving words
    for i in words:
        a_letters_answer.append(i.group())
    # print(a_letters_answer)

    # Task 4 - looking for exclamation sentences
    sentences = exclamation_sentences_pattern.finditer(x)
    exclamation_sentences_answer = []  # list for saving sentences
    for i in sentences:
        exclamation_sentences_answer.append(i.group())
    # print(exclamation_sentences_answer)

    # Task 5 - histogram for the length of unique words
    all_words = hist_pattern.finditer(x)
    length_dict = {}
    for i in all_words:
        length_dict[i.group()] = len(i.group())
        length_lst = [i for i in length_dict.values()]
    # making histogram
    plt.hist(length_lst)
    plt.xticks(range(min(length_lst), max(length_lst), 1))
    plt.xlabel("Word length")
    plt.ylabel("Amount of words")
    # plt.show()
