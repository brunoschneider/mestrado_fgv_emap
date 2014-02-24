#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import division
from gensim import corpora, models
import logging
import numpy as np


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def lda_from_std_data(vocab_path, corpus_path, num_topics, passes_):
    # preparing the dictionary
    f = open(vocab_path, "r")
    dictionary = {}
    counter = 1
    
    for line in f:
        dictionary[line.strip()] = counter
        counter += 1
    f.close()
    texts = []
    dictionary2 = corpora.Dictionary(texts)
    dictionary2.token2id = dictionary

    ## preparing the corpus
    f2 = open(corpus_path, "r" ) # dataset path
    corpus_temp = []
    list_temp = []
    corpus = []
    row_elements = []
    counter = 1
    t = ()

    for line in f2:
        row_elements = list(line.split(' '))
        corpus_temp.append(row_elements)

    s = len(corpus_temp)

    for n in range(s):
        if n == 0:
            t = (int(corpus_temp[n][1]), int(corpus_temp[n][2].strip()))
            list_temp.append(t)
        elif corpus_temp[n - 1][0] == corpus_temp[n][0]:
            t = (int(corpus_temp[n][1]), int(corpus_temp[n][2].strip()))
            list_temp.append(t)
        elif corpus_temp[n - 1][0] != corpus_temp[n][0]:
            corpus.append(list_temp)
            t = (int(corpus_temp[n][1]), int(corpus_temp[n][2].strip()))
            list_temp = [t]
        
    corpus.append(list_temp)
    f2.close()

    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary2, num_topics=num_topics, update_every=0, passes=passes_)
    return lda, corpus

# Document topic-proportions array
def gen_csv_from_ldamodel(corpus_, model, num_topics, output_path):
    matrix = model[corpus_]

    K = num_topics
    docs_array = np.zeros((K, len(matrix)))

    counter = 0

    for vector in matrix:
        for tup in range(len(vector)):
            docs_array[vector[tup][0]][counter] = vector[tup][1] 
        counter += 1
    np.savetxt(output_path, docs_array, delimiter = ',')
    return docs_array



