import sys
import random
import tkinter as tk
from PIL import ImageTk 
from argparse import ArgumentParser
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math
import string
import matplotlib.pyplot as plt
import numpy as np
import re
import collections as co
import itertools as it
import json

"""  Classes for calculating term and document frequency  """

class Words:
    
    def __init__(self, file, stop=False, punc=False):
        self.stop = True if stop is not False else False
        self.punc = True if punc is not False else False     
        self.file = file
        self.total = set()
        self.N = 0
        self.count_docs()

    def open_file(self, all=None):

        with open(self.file, encoding="utf-8") as f:
            for words in enumerate(f, 1):
                if len(words) > 0:
                    yield words

    def count_docs(self):
        
        with open(self.file, encoding="utf-8") as f:
            for words in f:
                self.N += 1
        
        return self.N
    
    def test(self, data, filter=None):

        punc = set(string.punctuation)
        punc.add("”")
        punc.add("’")
        punc.add("“")
        stop_words = set(stopwords.words("english"))
        x = co.deque()

        if filter == "stop":
            for words in data:
                if words not in stop_words:
                    x.append(words)

        elif filter == "punc":
            for words in data:
                if words not in punc:
                    x.append(words)

        else:
            if filter == "both":
                for words in data:
                    if words not in punc and words not in stop_words:
                        x.append(words)

        yield x

    def toke(self):
        
        for doc in self.open_file():
            doc_num = doc[0]
            docs = doc[1].strip()
            toked = nltk.word_tokenize(docs.lower())
        
            if self.stop == True and self.punc == False:
                x = self.test(toked, filter="stop")
                for words in x:
                    yield doc_num, words
                
            elif self.punc == True and self.stop == False:
                x = self.test(toked, filter="punc")
                for words in x:
                    yield doc_num, words
                
            else:
                if self.stop == True and self.punc == True:
                    x = self.test(toked, filter="both")
                    for words in x:
                        yield doc_num, words
                else:
                    yield doc_num, toked

    def df(self, term):
        
        checked = None

        for words in self.toke():
            doc_num = words[0]
            docs = set(words[1])
            if term in docs:
                checked = doc_num, term
                yield checked

    def tf(self, term):

        checked = None

        for words in self.toke():
            doc_num = words[0]
            docs = words[1]
            if term in docs:
                doc_counted = dict(co.Counter(docs))
                checked = doc_num, doc_counted[term]
                yield checked

    def word_check(self, term):
        
        inside = False

        for num in self.toke():
            terms = set(num[1])
            if term in terms:
                inside = True
                return inside

        if inside == False:
            print("'" + term + "'", "NOT FOUND, TRY AGAIN.")

        return inside
    
    def k(self, data):
        
        count = 0
        for freq in data:
            count += 1

        return count
    
    def common(self, n):

        for words in self.toke():
            doc_num = words[0]
            docs = words[1]
            x = co.Counter(docs)
            print(doc_num, x.most_common(n))

    def retrieve(self, doc=None, word=None):

        if doc != None:
            pass
        else:
            word_check = self.word_check(word)

        if word != None and word_check == True:

            termf = self.tf(word)
            docf = self.df(word)
            IDF = co.namedtuple("IDF", ["norm_tf", "N", "k"])
            k = self.k(docf)

            print("WORD:", "'" + word + "'")

            for words in termf:
                docs = words[0]
                raw = words[1]

                norm_tf = round(math.log(raw + 1.0, 10), 6)
                print("DOC#:", docs, end=" ~ ")
                print("TF RAW COUNT:", raw, end=" ~ ")
                print("TF LOG NORMALIZATION:", norm_tf, end=" ~ ")
                idf = IDF(norm_tf, self.N, k)
                idf_comp = round(1.0 + math.log(idf[1]/idf[2], 10), 6)
                tfidf = round(idf[0]*idf_comp, 6)
                print("TF-IDF:", tfidf)

            idf2 = round(1.0 + math.log(idf[1]/idf[2], 10), 6)
            print("DOCUMENT FREQUENCY:", k, end=" ~ ")
            print("INVERSE DOCUMENT FREQUENCY:", idf2)
            print("WORD:", "'" + word + "'")

        else:

            if doc!= None:
                for words in self.open_file():
                    doc_num = words[0]
                    try:
                        if doc == doc_num:
                            print("DOC#:", doc_num)
                            docs = words[1]
                            print(docs)

                    except IndexError:
                        print("DOC NOT FOUND, TRY AGAIN.")
                        continue

def parse_args(arglist):

    parser = ArgumentParser()
    parser.add_argument("file", help="text to be analyzed",
                        type=str)
    args = parser.parse_args(arglist)

    return args

def main(arglist):

    args = parse_args(arglist)
    #w=Words(args.file)
    #y = w.retrieve(word="heart")
    f=Words(args.file)
    for words in f.filter(punc=True):
        print(words)

    return None

if __name__ == "__main__":
    main(sys.argv[1:])