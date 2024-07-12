import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
import numpy as np

nltk.download('punkt')

def preprocess(code):
    return ' '.join(word_tokenize(code.lower()))

def sequence_similarity(code1, code2):
    return difflib.SequenceMatcher(None, code1, code2).ratio()

def tfidf_similarity(code1, code2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([code1, code2])
    return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

def word2vec_similarity(code1, code2):
    tokenized_code1 = word_tokenize(code1.lower())
    tokenized_code2 = word_tokenize(code2.lower())
    
    model = Word2Vec([tokenized_code1, tokenized_code2], min_count=1)
    
    vec1 = np.mean([model.wv[word] for word in tokenized_code1], axis=0)
    vec2 = np.mean([model.wv[word] for word in tokenized_code2], axis=0)
    
    return cosine_similarity([vec1], [vec2])[0][0]

def calculate_plagiarism_score(code1, code2):
    preprocessed_code1 = preprocess(code1)
    preprocessed_code2 = preprocess(code2)
    
    seq_sim = sequence_similarity(preprocessed_code1, preprocessed_code2)
    tfidf_sim = tfidf_similarity(preprocessed_code1, preprocessed_code2)
    w2v_sim = word2vec_similarity(preprocessed_code1, preprocessed_code2)
    
    weights = [0.3, 0.4, 0.3]
    final_score = (seq_sim * weights[0] + tfidf_sim * weights[1] + w2v_sim * weights[2]) * 100
    
    return round(final_score, 2)