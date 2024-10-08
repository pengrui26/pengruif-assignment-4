# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from lsa_model import LSAModel

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize the LSA model
lsa_model = LSAModel()

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'Query is empty'}), 400

    top_doc_ids, top_docs, top_scores = lsa_model.query(query)

    results = []
    for doc_id, doc, score in zip(top_doc_ids, top_docs, top_scores):
        results.append({
            'doc_id': doc_id,       # Include document ID
            'document': doc,
            'score': score
        })

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True, port=8001)
