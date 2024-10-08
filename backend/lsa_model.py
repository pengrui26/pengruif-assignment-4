# backend/lsa_model.py

import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline

class LSAModel:
    def __init__(self, n_components=100):
        self.n_components = n_components
        self.vectorizer = None
        self.lsa = None
        self.X = None
        self.documents = None
        self.load_data()
        self.train_lsa()

    def load_data(self):
        # Load the dataset
        newsgroups = fetch_20newsgroups(subset='all')
        self.documents = newsgroups.data

    def train_lsa(self):
        # Convert documents to TF-IDF matrix
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
        X_tfidf = self.vectorizer.fit_transform(self.documents)

        # Apply SVD
        svd_model = TruncatedSVD(n_components=self.n_components, random_state=42)
        normalizer = Normalizer(copy=False)
        self.lsa = make_pipeline(svd_model, normalizer)

        self.X = self.lsa.fit_transform(X_tfidf)

    def query(self, text_query, top_n=5):
        # Transform the query into the LSA space
        query_tfidf = self.vectorizer.transform([text_query])
        query_lsa = self.lsa.transform(query_tfidf)

        # Compute cosine similarity
        cosine_similarities = np.dot(self.X, query_lsa.T).flatten()

        # Get top n documents along with their indices
        top_indices = cosine_similarities.argsort()[::-1][:top_n]
        top_scores = cosine_similarities[top_indices]
        top_documents = [self.documents[i] for i in top_indices]
        top_doc_ids = top_indices.tolist()  # Get document IDs

        return top_doc_ids, top_documents, top_scores.tolist()
