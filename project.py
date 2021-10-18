from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.corpus import words

import re
import csv

class QueryProcessor():
    
    def __init__(self):
        self._stemmer = SnowballStemmer("english")
        self._stop_words = set(stopwords.words('english'))
        self._character_pattern = re.compile('[\W_]+')

    def process(self, query, stem = True):
        # remove capital letters
        query = query.casefold()
        # split sentence into tokens
        query = word_tokenize(query)
        # remove non-alphanumeric characters
        query = [self._character_pattern.sub('',token) for token in query]
        # filter empty tokens
        query = list(filter(None,query))
        # remove stop words
        query = [token for token in query if token not in self._stop_words]
        # stem each word
        if stem:
            query = [self._stemmer.stem(token) for token in query]
        # return processed query as List of unique tokens
        return list(set(query))


class Dataset():
    
    def __init__(self, csv_file, query_processor):
        self._file = csv_file
        self._query_processor = query_processor
        self._titles = []
        self._token_bookids = []
        self._dictionary = words.words()
        
    def load(self):
        # open the CSV file and read every title
        with open(self._file,encoding='utf8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            book_id = 0
            for row in reader:
                title = row[2]
                self._titles.append(title)
                for token in self._query_processor.process(title):
                    self._token_bookids.append((token,book_id))
                book_id += 1
    
    def get_title(self, book_id):
        return self._titles[book_id]
    
    def get_token_bookids(self):
        return self._token_bookids

    def get_dictionary(self):
        return self._dictionary