from itertools import chain
import database
import getText
import link_mapping
import pandas as pd
from re import sub
import learn_from_pdf
import nltk
from nltk.corpus import stopwords, wordnet
#------------------------------------------------------------------------
from nltk.stem.porter import PorterStemmer
nltk.download("stopwords") # download stopwords
nltk.download("wordnet") # isim-fiil ayristirmasi icin
ps = PorterStemmer() # create a root detect model (kelime yapısını bozduğu için kullanmadım)
#------------------------------------------------------------------------
# ram usage
# import os, psutil
# process = psutil.Process(os.getpid())
# print(process.memory_info().rss)
#------------------------------------------------------------------------

def setting(texts):
    two = []
    # single words
    for i, j in enumerate(texts): # remove whitespaces
        texts[i] = sub(r"\W", " ", j)

    for i, j in enumerate(texts):
        y = []
        for x in j.split():
            x = x.lower()
            if x in stopwords.words("english"):
                continue
            if len(x) < 3:
                continue
            if x.isdigit():
                continue
            y.append(x)
        texts[i] = y

    texts = list(chain.from_iterable(texts)) # 1 dim array
    print("-------", texts)
    single = texts.copy()
    # print(single)
    print("-"*400)

    # two words
    for i in range(len(texts)):
        try:
            tmp = 0
            # remove couple verbs
            for j in texts[i:i+2]:
                # print(i,":", j)
                if wordnet.synsets(j)[0].pos() == "v":
                    tmp += 1
            if tmp == 2:
                continue

            two.append(texts[i] + " " + texts[i+1])
        except IndexError:
            pass
    return single, two

def save(_1, _2, db1, db2):
    for i in _1:
        if len(i) < 15:
            # print(i)
            db1.insert_to_db(i)
    for i in _2:
        if len(i) < 21:
            # print(i)
            db2.insert_to_db(i)

def run(where, ctgry, path=""):
    db1 = database.db(category=ctgry + "_1")
    db2 = database.db(category=ctgry + "_2")
    _1 = ""
    _2 = ""

    if where == "website":
        text = getText.getText(path)
        _1, _2 = setting(text)
        save(_1, _2, db1, db2)

    elif where == "pdf":
        text = learn_from_pdf.txt(path)
        _1, _2 = setting(text)
        save(_1, _2, db1, db2)
