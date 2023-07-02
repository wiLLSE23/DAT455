import sys
sys.path.append('/Users/wille/Code/Sommarprogg/Labb1/wordfreq')
import wordfreq
import urllib.request
import ssl

"""topmost
This script allows the user to count the frequency of words, numbers, or symbols in a file given as argument in terminal
It is assumed that the input is a .txt file
"""

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
    txt_file = open(path)
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
    file = open(path)
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
    response = urllib.request.urlopen(url)
    return response.read().decode("utf8").splitlines()

def main():
    """takes a file of sentences, one of words and a number and prints the fruequency of the x most common words in text except those specified in the words file

    Parameters
    ----------
    sys[1] : str
        the path of stopwords file
    sys[2] : str
        the path of text file
    sys[3] : int
        the number of words to be printed
    """  
     
    stop_words = open_stripped_file(sys.argv[1])
    
    if(sys.argv[2].startswith('http://') or sys.argv[2].startswith('https://')):
        text = open_url(sys.argv[2])
    else:
        text = open_file(sys.argv[2])

    wordList = wordfreq.tokenize(text)
    word_freq = wordfreq.countWords(wordList, stop_words)
    wordfreq.printTopMost(word_freq, sys.argv[3])

if __name__ == "__main__":
    main()