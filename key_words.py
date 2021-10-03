# -*- coding: utf-8 -*-

import re

import pymorphy2
from rutermextract import TermExtractor
from sklearn.feature_extraction.text import TfidfVectorizer

with open("C:\Projects\obuch_back\stop_ru.txt", 'r', encoding="u8") as stop_file:
    rus_stops = [word.strip() for word in stop_file.readlines()]  # запишем стослова в список

make_tf_idf = TfidfVectorizer(stop_words=rus_stops)  # Создаем специальный объект-векторайзер
morph = pymorphy2.MorphAnalyzer()
term_extractor = TermExtractor()


def lemmatize_words(input_text: str):
    listed = [re.sub('[!@#$.:;,())\-—1234567890]', '', word) for word in input_text.lower().split()]
    lemmatized = [morph.parse(word)[0].normal_form for word in listed]
    return " ".join(lemmatized)


def produce_tf(single_text, number_of_words):
    make_tf_idf = TfidfVectorizer()
    texts_as_tfidf_vectors = make_tf_idf.fit_transform([single_text])
    id2word = {i: word for i, word in enumerate(single_text.split())}

    for text_row in range(texts_as_tfidf_vectors.shape[0]):
        row_data = texts_as_tfidf_vectors.getrow(text_row)
        words_for_this_text = row_data.toarray().argsort()
        top_words_for_this_text = words_for_this_text[0, :-1 * (number_of_words + 1):-1]
        res = []
        for w in set(id2word[w] for w in top_words_for_this_text):
            if w not in rus_stops:
                res.append(w)
        return res


def extract_terms(text):
    main_terms = []
    for term in term_extractor(text)[:10]:
        main_terms.append(str(term))

    return main_terms


def find_keys(phraze):
    return " ".join(produce_tf(lemmatize_words(phraze), 20)), " ".join(extract_terms(phraze))
