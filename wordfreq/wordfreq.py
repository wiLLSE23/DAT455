"""wordfreq
This script allows the user to count the frequency of words, numbers, or symbols
in a list of strings. It is assumed that the input is a list of strings.

This file can also be imported as a module and contains the following
functions:

    * tokenize - returns a list of all the words, numbers, or symbols in a list of strings
    * process_line returns a list of the words, numbers, or symbols in a string
    * count_words - counts the frequency of all words in words input, except those sepcified in stopWords
    * print_top_most - prints the top most n words in a dictionary of frequencies
    * main - the main function of the script that runs some instances of the code
"""

def tokenize(lines):
    """Builds a list of all the words, numbers, or symbols in a list of strings

    Parameters
    ----------
    lines : list
        a list of strings

    Returns
    -------
    list
        a list of words, numbers, or symbols
    """
    all_tokens = []
    for line in lines:
        all_tokens.extend(process_line(line))
    return all_tokens

def process_line(line):
    """Builds a list of all the words, numbers, or symbols in a string

    Parameters
    ----------
    line : str
        a string of text

    Returns
    -------
    list
        a list of words, numbers, or symbols
    """
    line_tokens = []
    word = []
    i = 0
    while i < len(line):
        if line[i].isalpha(): #is letter
            while line[i].isalpha(): #iterates over word (until next char is not a letter)
                word.append(line[i].lower())
                i+=1
                if i >= len(line): #breaks loop if string ends with letter and not symbol
                    break
            line_tokens.append("".join(word))
            word.clear()
        elif line[i].isdigit(): #is digit
            while line[i].isdigit() and i < len(line): #iterates until next char is not a digit
                word.append(line[i])
                i+=1
                if i >= len(line): #breaks loop if string ends with digit and not symbol
                    break
            line_tokens.append("".join(word))
            word.clear()
        elif not line[i].isspace(): #is symbol (symbols everthing neither digit, letter, blankspace)
            line_tokens.append(line[i])
            i+=1
        else: #char is blankspace
            i+=1
    return line_tokens

def count_words(words, stop_words):
    """counts the frequency of all words in words input, except those sepcified in stopWords

    Parameters
    ----------
    words : list
        a list if words
    stopWords: list
        a list of words to be ignored whilst counting

    Returns
    -------
    dict
        a dictionary of all words in words but not in stopwords and their frequency in words
    """
    word_freq = {}
    for word in words:
        if not word in stop_words: #exclude words in stopWords
            if word in word_freq: #if entry exists increment
                word_freq[word] += 1
            else:                  #otherwise add entry with freq 1
                word_freq.setdefault(word, 1)
    return word_freq

def print_top_most(frequencies,number_of_words):
    """which takes a dictionary of frequencies and prints the top most n words

    Parameters
    ----------
    frequencies : dict
        a dictionary of words (str) with values corrresponding to their frequency (int)
    n: int
        how many of the values to be included, includes n values with the highest frequencies

    Returns
    -------
    dict
        a dictionary of all words in words but not in stopwords and their frequency in words
    """
    sorted_word_list = []
    i = 0
    for word,freq in frequencies.items():
        sorted_word_list.append((word, freq))
    for (word,freq) in sorted(sorted_word_list, key=lambda word: -word[1]):
        if i>=number_of_words:
            break
        print(word.ljust(20) + str(freq).rjust(5))
        i+=1

def main():
    """Runs a test intance of each of the functions in this module
    """
    #Testing tokenize
    test_string = ['this is  . a a a simple  sentence.', 'this is a simple sentence.']
    print('input: ' + str(test_string)  + ' ', '=>',  tokenize(test_string))

    #Tesing countWords
    stop_words = ['.']
    word_dict = count_words(tokenize(test_string), stop_words)
    print('input: ' + str(word_dict) + ' igonoring all: ' + str(stop_words))

    #Testing printTopMost

    print_top_most(word_dict, 2)

if __name__ == "__main__":
    main()

