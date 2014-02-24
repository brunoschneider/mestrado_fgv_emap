#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import xml.etree.ElementTree as ET
import glob
from gensim import corpora, models, similarities
import string
import nltk
import re
import pandas as pd
import simplejson
from nltk.stem import PorterStemmer

def archives_path(path):
    archives_list = []
    output = []
    for fil in glob.glob(path):
        output.append(fil)
    for element in sorted(output):
        archives_list.append(element)
    return archives_list


def xml_reader(archives_list):
    docs_list = []
    dates_list = []
    for x in range(len(archives_list)):
        tree = ET.parse(archives_list[x])
        root = tree.getroot()
        for document in root.findall('REUTERS'):
            text_ = document.find('TEXT')
            text__ = text_.find('BODY')
            date_ = document.find('DATE').text
            datetime_index_t = pd.to_datetime(date_)
            if text__ is not None:
                if isinstance(datetime_index_t, pd.tslib.Timestamp):
                    text___ = text__.text
                    text___ = text___.encode('utf-8', errors='ignore')
                    docs_list.append(text___.lower())
                    dates_list.append(date_)
            else:
                pass

    f = open('dataset/datetime_index.txt', 'w')
    simplejson.dump(dates_list, f)
    f.close()
    
    return dates_list, docs_list

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def gen_dict_n_corpus(docs_list):
    sw = nltk.corpus.stopwords.words('english') + list (string.punctuation) + ['reuter'] + ['said'] # removing the word 'said' 
    swu = [word.encode('utf8') for word in sw]

    porter = PorterStemmer()

    texts = [[word for word in nltk.wordpunct_tokenize(document) if word not in swu] for document in docs_list] 
    
    texts = []
    text_t = []
    for document in docs_list:
        for word in nltk.wordpunct_tokenize(document):
            if has_numbers(word) == False:
                if word not in swu:
                    if len(word) > 2:
                        text_t.append(porter.stem(word))
            else:
                pass
            
        texts.append(text_t)
        text_t = []

    texts_ = []
    for lis in texts:
        for word in lis:
            texts_.append(word)
    freq = nltk.FreqDist(texts_)
    hapaxes = freq.hapaxes()

    texts__  = []
    for document in texts:
        document = [word for word in document if word not in hapaxes]
        texts__.append(document)

    dictionary = corpora.Dictionary(texts__)
    dictionary.save('dataset/reuters_porter_.dict') # store the dictionary, for future reference

    corpus = [dictionary.doc2bow(text) for text in texts__]
    corpora.MmCorpus.serialize('dataset/reuters_porter_.mm', corpus) # store to disk, for later use
    
    return dictionary, corpus


