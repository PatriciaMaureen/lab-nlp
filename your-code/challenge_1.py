def clean_up(s):
    """
    Cleans up numbers, URLs, and special characters from a string.

    Args:
        s: The string to be cleaned up.

    Returns:
        A string that has been cleaned up.
    """
    
    import re
    #https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
    if isinstance(s, str):
        # Clean up URLs
        s = re.sub(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', '', s)
        # Remove non-alphabetical characters
        s = re.sub('[^a-zA-Z \n\.]', " ", s)
        # Convert to lowercase
        s = s.lower()
    return s
    
    
def tokenize(s):
    """
    Tokenize a string.

    Args:
        s: String to be tokenized.

    Returns:
        A list of words as the result of tokenization.
    """
    from nltk.tokenize import word_tokenize
    s = word_tokenize(s)
    return s


def stem_and_lemmatize(l):
    """
    Perform stemming and lemmatization on a list of words.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after being stemmed and lemmatized.
    """
    from nltk.stem import PorterStemmer

    ps = PorterStemmer()
    stemmed = [ps.stem(w) for w in l]
 
    from nltk.stem import WordNetLemmatizer 
    from nltk.corpus import wordnet

    lemmatizer = WordNetLemmatizer() 
    stemmed_lemmatized = [lemmatizer.lemmatize(word) for word in stemmed]
    return stemmed_lemmatized
    
    
def remove_stopwords(l):
    """
    Remove English stopwords from a list of strings.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after stop words are removed.
    """
    import nltk
    from nltk.corpus import stopwords
       
    stop_words = set(stopwords.words('english'))
    without_sw = [word for word in l if word not in stop_words]
    return without_sw
    
