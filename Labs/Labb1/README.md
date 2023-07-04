# Lab 1: Word Counting
This repository contains the code for Lab 1: Word Counting, which is part of the DAT455 course. The #purpose of this lab is to practice basic operations on lists, strings, and dictionaries, as well as fundamental programming concepts such as loops, if statements, and functions. The lab focuses on word counting, which is a fundamental technique used in natural language processing.

## Table of contents
* [Introduction](#Introduction)
* [Tokenization](#Tokenization)
* [Counting](#Counting)
* [Printing](#Printing)
* [Testing](#Testing)
* [Usage](#Usage)

### Introduction
In this lab, we explore the concept of word counting and its importance in natural language processing. We will learn how to tokenize a document, count the frequency of each word, and print the results. The lab consists of four parts:

1. Tokenization - splitting a running text into a sequence of words (tokens).
2. Counting - aggregating statistics for the frequencies of different words.
3. Printing - displaying the final results.
4. Completed Program - assembling a complete program using the above components.

### Tokenization
The first task in this lab is to implement the tokenize function in the wordfreq.py module. The tokenize function takes a complete document as a list of text lines and produces a list of tokens, in the correct order. Tokenization involves splitting the document into individual words based on certain rules.

To start, the tokenize function has been provided with a dummy implementation. Replace the pass statement with your implementation of the tokenize function. The function should follow the specified rules for word extraction, handling punctuation, and case sensitivity. Make sure to remove any existing print statements used for debugging.

### Counting
The next part of the lab is to implement the countWords function in the wordfreq.py module. The countWords function takes a list of words and a list of stop words and counts the frequency of each word, ignoring the stop words.

To implement the countWords function, follow these steps:

1. Initialize an empty dictionary to store the word frequencies.
2. Iterate through each word in the list of words.
3. Check if the word is a stop word. If it is, ignore it and continue to the next word.
4. If the word is not already in the dictionary, add it as a key with a count of 1.
5. If the word is already in the dictionary, increment its count by 1.
6. Finally, return the dictionary containing the word frequencies.

### Printing
The last part of the lab is to implement the printing functionality in the wordfreq.py module. The printTopMost function takes a dictionary of word frequencies and prints the top most frequent words.

To implement the printTopMost function, follow these steps:

1. Sort the dictionary by the word frequencies in descending order.
2. Iterate through the sorted list of word-frequency pairs.
3. Print each word and its frequency.

### Testing
To test your implementation, you can use the provided test.py script. Place the test.py file in the same folder as your `wordfreq

### Usage
This code is free to use as you like with the exception of plagiarism in academic settings.