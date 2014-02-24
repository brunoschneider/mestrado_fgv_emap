#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import division
from gensim import corpora, models, similarities
from scipy.linalg import norm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import operator
import math
import simplejson
import random
import logging
from colorbrewer import * # color palette
from word_cloud import make_wordcloud


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# Load data from a CSV text file
def load_array_from_file(filepath):
    data = np.loadtxt(filepath, dtype=float, delimiter=',')
    return data.T

# Load pandas dataframe archive
def load_dataframe(df_path):
    df = pd.read_pickle(df_path)
    return df

# Kullback-Leibler divergence
def kl(p, q):
    """Kullback-Leibler divergence D(P || Q) for discrete distributions

    Parameters
    ----------
    p, q : array-like, dtype=float, shape=n
        Discrete probability distributions.
    """
    p = np.asarray(p, dtype=np.float)
    q = np.asarray(q, dtype=np.float)

    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

# Load corpus from a file
def load_corpus(corpus_file):
    corpus_ = corpora.MmCorpus(corpus_file)
    return corpus_

# Load dictionary from a file
def load_dictionary(dict_file):
    dictionary = corpora.dictionary.Dictionary.load(dict_file)
    return dictionary

# LDA modeling
def lda(corpus, dictionary, num_topics, passes, lambda_output_path):
    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, update_every=0, passes=passes)
    lambda_ = lda.state.get_lambda()
    np.savetxt(lambda_output_path, lambda_, delimiter = ',')
    return lda

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


# Topics distance matrix
def gen_dist_matrix(array, output_path):
    array_ = array.T
    size = array_.shape
    row_number = size[0]
    column_number = size[1]
    eps = 2**(-52)

    for row in range(row_number): 
        for column in range(column_number):
            array_[row][column] = (array_[row][column] + eps)

    for row in range(row_number): 
        row_sum = array_[row].sum()
        for column in range(column_number):
            array_[row][column] = (array_[row][column]/row_sum)

    dist_matrix = np.zeros((row_number, row_number))

    for row in range(row_number): 
        for column in range(row_number):
            dist_matrix[row][column] = kl(array_[row,:], array_[column,:])

    sym_dist_matrix = np.zeros((row_number, row_number))
    for row in range(row_number): 
        for column in range(row_number):
            sym_dist_matrix[row][column] = 0.5 * (dist_matrix[row][column] + dist_matrix[column][row])

    np.savetxt(output_path, sym_dist_matrix, delimiter = ',') # The MDS was done in KNIME (knime.org) using this output 
    return sym_dist_matrix

# Ordering of topics
def gen_ordering_list_from_mds(mds_path):
    data = np.loadtxt(mds_path, usecols=(2,), skiprows=1, delimiter=',') # The MDS was done using KNIME (knime.org)
    dictionary = {}
    s = len(data)

    for n in range(s):
        dictionary[n] = data[n]

    sorted_dict = sorted(dictionary.iteritems(), key=operator.itemgetter(1))

    ordering_list = []
    for n in range(s):
        ordering_list.append(sorted_dict[n][0])
    return ordering_list

# Time index generator
def gen_random_index(n, initial_date):
    ini = pd.to_datetime(initial_date)
    dates_list = [ini] 
    for element in range(n - 1):
        random_minute = random.randint(1,10)
        minute = pd.tseries.offsets.Minute(random_minute)
        ini += minute
        dates_list.append(ini)
    index = pd.to_datetime(dates_list)
    return index

# Dataframe creation using pandas library (with random time-index)
def create_dataframe_from_csvfile(array, output_path, ordering, ordered=True):
    num_topics = array.shape[1]
    num_docs = array.shape[0]

    index = gen_random_index(num_docs, '1/1/2000')
    columns = [col for col in range(num_topics)]

    if ordered == True:
        array_size = array.shape
        reordered_array = np.zeros(array_size)

        for n in range(array_size[1]):
            reordered_array[:, n] = array[:, ordering[n]] 
        df = pd.DataFrame(reordered_array, index=index, columns=columns)
        df.to_pickle(output_path)

    else:
        df = pd.DataFrame(array, index=index, columns=columns)
        df.to_pickle(output_path)
    return df

# Dataframe creation using pandas library (for Reuters dataset)
def create_dataframe_from_csvfile_reuters(array, timeindex_path, output_path, ordering, ordered=True):
    num_topics = array.shape[1]

    f = open(timeindex_path, 'r')
    datetime_list = simplejson.load(f)
    f.close()
    
    dates_list_ = []
    for element in datetime_list:
        datetime_index_t = pd.to_datetime(element)
        dates_list_.append(datetime_index_t)

    index = pd.to_datetime(dates_list_)

    columns = [col for col in range(num_topics)]

    if ordered == True:
        array_size = array.shape
        reordered_array = np.zeros(array_size)

        for n in range(array_size[1]):
            reordered_array[:, n] = array[:, ordering[n]] 
        df = pd.DataFrame(reordered_array, index=index, columns=columns)
        df.to_pickle(output_path)

    else:
        df = pd.DataFrame(array, index=index, columns=columns)
        df.to_pickle(output_path)
    return df


## Data aggregation using pandas library 
def aggregate_data(df, period, n, output_path): # period: 'hour', 'day' or 'month'
    if period == 'hour':
        int_ = pd.tseries.offsets.Hour(n)
    if period == 'day':
        int_ = pd.tseries.offsets.Day(n)
    if period == 'month':
        int_ = pd.tseries.offsets.MonthEnd(n)
    df_grouped = df.resample(int_, how='sum')
    df_grouped_filled = df_grouped.fillna(value = 0)
    df_grouped_filled.to_pickle(output_path)
    return df_grouped


# Preparing the data for visualization
def gen_tuples_list_from_dataframe(df, threshold_value, sort=False, exportcsv=False):
    df_max = df.values.max()
    df = df / df_max
    df.values[df.values == 1] = 0.999

    # filtering data
    t = threshold_value 
    df.values[df.values <=t] = 0
    df_col = len(df.columns)
    for v in range(df_col):
        if df[v].sum() == 0:
            del df[v]
    if exportcsv == True:
        filtered_array = df.values
        np.savetxt('d3/array.csv', filtered_array, delimiter=',')
    col_names = df.columns.values.tolist()

    row_size = df.values.shape[0]
    column_size = df.values.shape[1]
    tup_list = []
    tup_list_t = []
    for row in range(row_size):
        for element in range(column_size):
            c = df.iloc[row].index[element]
            tup =  (df.columns.get_loc(c), df.iloc[row][c])
            tup_list_t.append(tup)
        if sort == True:
            tup_list_t.sort(key=lambda tup: tup[1])
        tup_list.append(tup_list_t)
        tup_list_t = []
    return tup_list 

# Main-topic visualization
def main_topic_vis(input_list, w, h, xsize, ysize):
    y_ini = ysize - 50 
    x_ini = 50 # fixed value
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg = 'white') # background color

    for x in range(len(input_list)):
        value = input_list[x][-1][1]
        topic = input_list[x][-1][0]

        map_ = plt.get_cmap(str(topic)) 

        if value == 0.0:
            rect = patches.Rectangle((x_ini, y_ini), w, h, color = '0.96')
            ax.add_patch(rect)
            x_ini += w
        else:
            rect = patches.Rectangle((x_ini, y_ini), w, h, color = map_(value))
            ax.add_patch(rect)
            x_ini += w

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.xlim([0, xsize])
    plt.ylim([0, ysize])
    plt.show()

# Pixel matrix visualization
def pixel_matrix_viewer(input_list, pixel_size, xsize, ysize):
    y_0 = ysize - 50 
    x_ini = 50 # fixed value
    y_ini = y_0
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg = 'white') # background color

    for x in range(len(input_list)):
        for y in range(len(input_list[x])):
            value = input_list[x][y][1]
            topic = input_list[x][y][0]

            map_ = plt.get_cmap(str(topic)) 

            rect = patches.Rectangle((x_ini, y_ini), pixel_size, pixel_size, color = map_(value))
            ax.add_patch(rect)
            y_ini -= pixel_size
        x_ini += pixel_size
        y_ini = y_0

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.xlim([0, xsize])
    plt.ylim([0, ysize])
    plt.show()

# Bubble Timeline visualization
def bubbletimeline_vis(input_list, xsize, ysize, transparency=False):
    y_0 = ysize - 50 
    x_ini = 58 # fixed value
    y_ini = y_0
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg = 'white') # background color

    for x in range(len(input_list)):
        for y in range(len(input_list[x])):
            value = input_list[x][y][1]
            topic = input_list[x][y][0]

            map_ = plt.get_cmap(str(topic)) 

            if transparency == True:
                circ = patches.Circle((x_ini, y_ini), math.sqrt(value * 256), color = map_(0.99), alpha = value)
            else:
                circ = patches.Circle((x_ini, y_ini), math.sqrt(value * 256), color = map_(value))

            ax.add_patch(circ)
            y_ini -= 40 # fixed space between rows
        x_ini += 16 # fixed space between circles
        y_ini = y_0

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.xlim([0, xsize])
    plt.ylim([0, ysize])
    plt.show()


# Wordcloud visualization
def wordcloud(lambda_path, dictionary, topic_n, fill_color, w, h):
    lambda_ = load_array_from_file(lambda_path)
    lam_T = lambda_.T
    print lam_T.shape
    sorted_dict = sorted(dictionary.iteritems())
    t = []
    for element in range(len(sorted_dict)):
        t.append(sorted_dict[element][1])
    words = np.array(t)
    topic_dist = lam_T[topic_n]
    make_wordcloud(words, topic_dist, fill_color, width=w, height=h)




