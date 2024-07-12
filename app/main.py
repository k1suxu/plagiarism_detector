import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
import numpy as np

nltk.download('punkt')

# 小文字に直して単語ごとに空白区切りで分割
def preprocess(code):
    return ' '.join(word_tokenize(code.lower()))

# 類似度を計算
def sequence_similarity(code1, code2):
    return difflib.SequenceMatcher(None, code1, code2).ratio()

# TF-IDFを使って類似度を計算
def tfidf_similarity(code1, code2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([code1, code2])
    # コサイン類似度を計算
    return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

# Word2Vecを使って類似度を計算
def word2vec_similarity(code1, code2):
    # 単語ごとに分割
    tokenized_code1 = word_tokenize(code1.lower())
    tokenized_code2 = word_tokenize(code2.lower())
    
    # Word2Vec モデルを作成
    model = Word2Vec([tokenized_code1, tokenized_code2], min_count=1)
    
    # 各コードのベクトルを計算
    vec1 = np.mean([model.wv[word] for word in tokenized_code1], axis=0)
    vec2 = np.mean([model.wv[word] for word in tokenized_code2], axis=0)
    
    # コサイン類似度を計算
    return cosine_similarity([vec1], [vec2])[0][0]

def calculate_plagiarism_score(code1, code2):
    # 前処理
    preprocessed_code1 = preprocess(code1)
    preprocessed_code2 = preprocess(code2)

    # 類似度を計算    
    seq_sim = sequence_similarity(preprocessed_code1, preprocessed_code2)
    tfidf_sim = tfidf_similarity(preprocessed_code1, preprocessed_code2)
    word2vec_sim = word2vec_similarity(preprocessed_code1, preprocessed_code2)
    
    # 重み付け
    weights = [0.3, 0.4, 0.3]
    final_score = (seq_sim * weights[0] + tfidf_sim * weights[1] + word2vec_sim * weights[2]) * 100
    
    # 小数点第2位までに丸める
    return round(final_score, 2)