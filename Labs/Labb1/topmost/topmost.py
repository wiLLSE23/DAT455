import sys
import urllib.request
import ssl
import matplotlib.pyplot as plt
sys.path.append('/Users/wille/Code/Sommarprogg/Labb1/wordfreq')
import wordfreq

"""topmost
This script allows the user to count the frequency of words, numbers, or symbols in a file given as argument in terminal
It is assumed that the input is a .txt file

This file can also be imported as a module and contains the following
functions:
    * zipf_plot - plots the frequency of top n words against zips law
    * open_file - opes a .txt file and returns the rows in a list
    * open_stripped_file - opes a .txt file and returns the strings in a list with stripped elements
    * open_url - opens a url and returns the rows in a list
    * main - runs the code with system arguement 1, 2, 3 [stopwords file, text file, number of words to be printed]
"""


def zipf_plot(counts, number_of_words):
    """takes a dictionary of strings and their frequencies and plots this against zips law (freq(w) ~ 1 / rank(w))
    retrieved from Lecture 05 slide 30
    Parameters
    ----------
    counts : dict
        the dictionary of words and frequencies <str>:<int>
    n : int
        the number of words to be analyzed. cannot exceed length of dictionary
    """
    freqs = sorted(list(counts.items()),
                   key=lambda element: -(element[1]))
    word_list = []
    freq_list = []
    i = 1  # rank of the most frequent item
    for word, freq in freqs[:number_of_words]:
        word_list.append(i)
        freq_list.append(freq)
        i = i+1
    freq_one = [freq_list[0]/word for word in word_list]
    plt.plot(word_list, freq_list, 'ro')
    plt.plot(word_list, freq_one)
    plt.show()


def open_file(path):
    """takes a file of strings, returns a list of those sentences

    Parameters
    ----------
    path : str
        the path of the file to be opened and its lines returned

    Returns
    -------
    list
        a list of the lines in the file
    """
    txt_file = open(path, 'r', encoding='utf-8')
    lines = txt_file.readlines()
    txt_file.close()
    return lines


def open_stripped_file(path):
    """takes a file of strings, returns a list of those string stripped of blank characters

    Parameters
    ----------
    path : str
        the path of the file to be opened and its lines returned

    Returns
    -------
    list
        a list of the lines in the file
    """
    try:
        file = open(path, 'r', encoding='utf-8')
    except:
        raise Exception("invalid path: ", path)
    lines = [line.strip() for line in file.readlines()]
    file.close()
    return lines


def open_url(url):
    """takes a url of a text file with sentences, returns a list of those sentences

    Parameters
    ----------
    url : str
        the path of text file

    Returns
    -------
    list
        a list of the lines in the file
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        response = urllib.request.urlopen(url)
    except:
        print("error opening link: ", url)
    return response.read().decode("utf8").splitlines()


def main():
    """takes a file of sentences, one of words and a number
    and prints the fruequency of the x most common words in text
    except those specified in the words file

    Parameters
    ----------
    arg[1] : str
        the path of stopwords file
    arg[2] : str
        the path of text file
    agr[3] : int
        the number of words to be printed
    """
    if(sys.argv[1].endswith(".txt") and sys.argv[2].endswith(".txt") and sys.argv[3].isdigit()):
        stop_words = open_stripped_file(sys.argv[1])

        if (sys.argv[2].startswith('http://') or sys.argv[2].startswith('https://')):
            text = open_url(sys.argv[2])
        else:
            text = open_file(sys.argv[2])

        word_list = wordfreq.tokenize(text)
        word_freq = wordfreq.count_words(word_list, stop_words)
        # plots the frequencies along with the zipf estimation
        zipf_plot(word_freq, int(sys.argv[3]))
        wordfreq.print_top_most(word_freq, int(sys.argv[3]))
    else:
        raise TypeError("arguments are invalid")
if __name__ == "__main__":
    main()
