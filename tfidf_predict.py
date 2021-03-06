# -*- coding: utf-8 -*-
"""tfidf_predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S2f7YCMwFQETdS-8se8FkLibtM63lxRz
"""

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import joblib
import re
import jieba
import pickle

"""# Import testing lyric and preprocess"""

def remove_punctuation(line):
    stopwords = [line.strip() for line in open('./categories/TF-IDF/data/stopwords.txt', 'r', encoding='utf-8').readlines()]
    line = str(line)
    if line.strip() == '':
        return ''
    re_han = re.compile(u"[^a-zA-Z0-9\u4E00-\u9FA5]")
    line = re_han.sub('', line)
    cut = [w for w in list(jieba.cut(line)) if w not in stopwords]
    res = " ".join(cut)
    return res

def categorize(lyrics):
    test_lyric = lyrics
    test_lyric_seg = remove_punctuation(test_lyric)

    """## Load TfidfVectorizer and transform lyric to vector"""

    with open('./categories/TF-IDF/model/vectorizer.pickle', 'rb') as f:
        vectorizer = pickle.load(f)

    tmp = []
    tmp.append(test_lyric_seg)
    test_lyric_vec = vectorizer.transform(tmp)

    """# Load Logistic Regression Model"""

    LR_model = joblib.load('./categories/TF-IDF/model/LR_model')


    predictions = LR_model.predict(test_lyric_vec)

    return predictions[0]

