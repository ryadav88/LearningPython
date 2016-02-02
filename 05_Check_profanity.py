import urllib


def read_text():

    # open is a built-in function in Python and returns an object of the file type
    quotes = open("/Users/path_to_file/movie_quotes.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()

    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
        print ("This document has no curse words.")
    else:
        print ("Could not scan the document properly.")

    connection.close()

read_text()