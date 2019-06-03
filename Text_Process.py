import pandas as pd
import numpy as np
import nltk
import re
import unicodedata
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from unicodedata import normalize


class Text_Process():
    def __init__(self, *args):
        super(Text_Process, self).__init__(*args)
    
    def process_caractere(self,txt):
        txt=[normalize('NFKD',x).encode('ASCII','ignore').decode('ASCII') for x in txt]
        txt=[re.sub('[^a-z|\ ]','',str.lower(x)) for x in txt]
        return txt
        
    def remove_stop_words(self,txt,stop_words):
        text = CountVectorizer(ngram_range=(1,1),stop_words=stop_words)
        text.fit(txt)
        return text
    
    def process_document(self,doc,metodo=''):
        txt = trata_caracteres(doc)
        try:
            texto = remove_stop_words(txt)
            lista_txt = texto.get_feature_names()
        except:
            lista_txt = txt
        if metodo=='lemma':
            lem = WordNetLemmatizer()
            for part_of_speech in ['a', 's', 'r', 'n', 'v']:
                tms = [lem.lemmatize(a,part_of_speech) for a in lista_txt]
        if metodo == 'stem':
            ps = PorterStemmer()
            tms = [ps.stem(a) for a in lista_txt]
        if metodo == '':
            tms = txt
        return " ".join(tms)

    def processamento_text_stem(self, df):
        return df.apply(lambda elemento: self.process_document([elemento],'stem'))

        
        