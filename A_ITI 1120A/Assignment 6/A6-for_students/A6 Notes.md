Gen 1

```python
def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    word_dict = {}  # initialize a empty dict to sto
    for line in fp:
        each_line = line.lower()  # 1. Make everything lowercase
        words = each_line.split()  # 2. Split the line into words
        clean_list = []  # 3~4. initialize the list to store without ,.! and others
        for w in words:  # remove ,.!
            cleaned_word = ''
            for char in w:
                if char.isalpha() or char in ["-", "'"]:  # 4. Remove apostrophes and hyphens.
                    cleaned_word += char

            cleaned_word = cleaned_word.replace(",", '').replace("-", '')  # 3. remove punctuation

            if cleaned_word.isalpha():
                clean_list.append(cleaned_word)

        suitable_words = []  # 6. remove the word with less than 2 characters, like "a"
        for word in suitable_words:
            if len(word) >= 2:
                word_dict[word] = word_dict.get(word, 0) + 1  # return the value of the key Textbook P. 171
    return word_dict
```

Gen 2
```python
# Haojian Wang
# 300411829
# ITI 1120
# Assignment 6
import string


def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    while True:
        try:
            file_name = input('Enter the name of the file: ').strip()
            file_object = open(file_name, 'r')
            return file_object
        except FileNotFoundError:
            print('File not found! Please try again.')


def remove_punctuation(word):
    '''str->str
    ADD ON OWN 去除标点符号
    Remove punctuation and return str with punctuation removed'''
    result = ''  # initialize a empty str
    for char in word:
        if char not in string.punctuation:
            result += char
    return result


def is_word(word):
    '''str->bool
    ADD ON OWN 检查是否为字母且长度大于2 否则False
    Check if the word is alphabetic and over 2 characters'''
    return word.isalpha() and len(word) >= 2


def process_lines(ls):
    '''str->list
    ADD ON OWN 将每行转换成list并去除角标与杠
    Process each line and return a list of words'''
    processed_words = []
    for word in ls:
        clean_word = remove_punctuation(word)  # call function remove_punctuation to remove punctuation
        clean_word = clean_word.replace("'", "").replace("-", "")  # 4. Remove apostrophes and hyphens.
        if is_word(clean_word):  # recall function is_word to add longer than 2 words
            processed_words.append(clean_word)
    return processed_words  # list without punctuation, "'", and "-"


def make_a_dict(lsw, line_number, word_dict):
    '''lst[str], int, dict->None
    ADD ON OWN 字符串列表，行号（1开始），字典->无返回值。用于被read_file调用->并在函数内直接修改word_dict（read_file局部变量）
    Make a dictionary for each word in processed words and add the line_number in it'''
    for word in lsw:
        if word in word_dict:
            # dict[key]<这是个集合>.add<set method> line_number into the set of the key[word]
            word_dict[word].add(line_number)
        else:  # if the word isn't in lsw, add them
            word_dict[word] = {line_number}


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    word_dict = {}
    line_number = 1  # line number starts 1

    for line in fp:
        # remove space front/back and lowercase 去除空格并小写
        line = line.strip().lower()

        # Split the line into individual words by spaces 以空格将单词转list
        words = line.split()

        # call->return a list without punctuations/"'"/"-"
        processed_words = process_lines(words)

        # call->return a dictionary{"word": {line_numbers}}
        make_a_dict(processed_words, line_number, word_dict)

        line_number += 1  # next line

    return word_dict


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    processed_query = query.split()  # list
    line_number_list = []

    for word in processed_query:
        if word in D:
            line_number_list.append(D[word])

        if not line_number_list:
            return []

    fn_set = line_number_list[0]
    for s in line_number_list[1:]:
        fn_set = fn_set.intersection(s)

    return sorted(fn_set)

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
flag = True
while flag:
    if query != 'q':
        result = find_coexistance(d,query)
        if result:
            print("The one or more words you entered coexisted in the following lines of the file:")
            for lines in result:
                print(lines, end = ' ')
        else:
            print(f"Word {query} not in the file.")
        print('')
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    elif query == 'q':
        flag = False
        print("Thank you! Good bye!")

# d is a word dict

```

```python
# Haojian Wang
# 300411829
# ITI 1120
# Assignment 6
import string


def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    while True:
        try:
            file_name = input('Enter the name of the file: ').strip()
            file_object = open(file_name, 'r')
            return file_object
        except FileNotFoundError:
            print('File not found! Please try again.')


def remove_punctuation(word):
    '''str->str
    ADD ON OWN 去除标点符号
    Remove punctuation and return str with punctuation removed'''
    result = ''  # initialize a empty str
    for char in word:
        if char not in string.punctuation:
            result += char
    return result


def is_word(word):
    '''str->bool
    ADD ON OWN 检查是否为字母且长度大于2 否则False
    Check if the word is alphabetic and over 2 characters'''
    return word.isalpha() and len(word) >= 2


def process_lines(ls):
    '''str->list
    ADD ON OWN 将每行转换成list并去除角标与杠
    Process each line and return a list of words'''
    processed_words = []
    for word in ls:
        clean_word = remove_punctuation(word)  # call function remove_punctuation to remove punctuation
        clean_word = clean_word.replace("'", "").replace("-", "")  # 4. Remove apostrophes and hyphens.
        if is_word(clean_word):  # recall function is_word to add longer than 2 words
            processed_words.append(clean_word)
    return processed_words  # list without punctuation, "'", and "-"


def make_a_dict(lsw, line_number, word_dict):
    '''lst[str], int, dict->None
    ADD ON OWN 字符串列表，行号（1开始），字典->无返回值。用于被read_file调用->并在函数内直接修改word_dict（read_file局部变量）
    Make a dictionary for each word in processed words and add the line_number in it'''
    for word in lsw:
        if word in word_dict:
            # dict[key]<这是个集合>.add<set method> line_number into the set of the key[word]
            word_dict[word].add(line_number)
        else:  # if the word isn't in lsw, add them
            word_dict[word] = {line_number}


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    word_dict = {}
    line_number = 1  # line number starts 1

    for line in fp:
        # remove space front/back and lowercase 去除空格并小写
        line = line.strip().lower()

        # Split the line into individual words by spaces 以空格将单词转list
        words = line.split()

        # call->return a list without punctuations/"'"/"-"
        processed_words = process_lines(words)

        # call->return a dictionary{"word": {line_numbers}}
        make_a_dict(processed_words, line_number, word_dict)

        line_number += 1  # next line

    return word_dict


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    processed_query = query.split()  # list
    line_number_list = []

    for word in processed_query:
        if word in D:
            line_number_list.append(D[word])

        if not line_number_list:
            return []

    fn_set = line_number_list[0]
    for s in line_number_list[1:]:
        fn_set = fn_set & s

    return sorted(fn_set)

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
flag = True
while flag:
    if query != 'q':
        result = find_coexistance(d,query)
        if result:
            print("The one or more words you entered coexisted in the following lines of the file:")
            for lines in result:
                print(lines, end = ' ')
        else:
            print(f"Word {query} not in the file.")
        print('')
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    elif query == 'q':
        flag = False
        print("Thank you! Good bye!")

# d is a word dict

```













