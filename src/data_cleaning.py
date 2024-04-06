# data_cleaning.py

import os
import re
import string
import numpy as np
from itertools import groupby
import nltk
from nltk.corpus import stopwords


def remove_duplicates(text_before):
	"""
	removed words that exist more than 2 times before
	:param text_before:
	:return:
	"""
	my_dict = dict()
	text_after = list()
    for word in text_before.split():
        if word not in my_dict.keys():
            my_dict[word] = 1
		else:
            my_dict[word] = my_dict[word] + 1

    for key, value in my_dict.items():
        if value >= 2:
            text_after.append(key)
		else:
            text_after.append(key)
    return " ".join(text_after)


def denoise_text(text):
	"""
	Change text to lowercase, remove text in square brackets, remove links, remove punctuation
	:param text:
	:return:
	"""
	text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text
