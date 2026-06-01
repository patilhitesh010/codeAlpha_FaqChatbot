import json
import re
import os  # New import to handle file paths
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQChatbot:
    def __init__(self, faq_file='faqs.json'):
        # This line finds the exact folder where this script is saved
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # This joins the folder path with the filename
        faq_path = os.path.join(script_dir, faq_file)
        
        # Open the file using the full path
        with open(faq_path, 'r', encoding='utf-8') as f:
            self.faqs = json.load(f)
        
        self.questions = [faq['question'] for faq in self.faqs]
        self.answers = [faq['answer'] for faq in self.faqs]
        
        self.stop_words = {'a', 'an', 'the', 'is', 'are', 'was', 'were', 'to', 'for', 'in', 'on', 'at', 'by', 'of', 'and', 'or', 'do', 'how', 'what', 'can', 'i'}
        
        self.preprocessed_questions = [self.preprocess(q) for q in self.questions]
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.preprocessed_questions)

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = text.split()
        cleaned_tokens = [word for word in tokens if word not in self.stop_words]
        return " ".join(cleaned_tokens)

    def get_response(self, user_input, threshold=0.25):
        processed_input = self.preprocess(user_input)
        if not processed_input:
            return {"matched_question": None, "answer": "I didn't quite catch that.", "score": 0.0}
            
        user_tfidf = self.vectorizer.transform([processed_input])
        similarities = cosine_similarity(user_tfidf, self.tfidf_matrix).flatten()
        best_match_idx = similarities.argsort()[-1]
        max_similarity = similarities[best_match_idx]
        
        if max_similarity < threshold:
            return {"matched_question": None, "answer": "Sorry, I couldn't find a relevant answer.", "score": round(float(max_similarity), 2)}
        
        return {"matched_question": self.questions[best_match_idx], "answer": self.answers[best_match_idx], "score": round(float(max_similarity), 2)}
