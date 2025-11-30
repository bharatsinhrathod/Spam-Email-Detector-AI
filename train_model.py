import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# 1. Create a dummy dataset (Or load your own CSV here)
# Format: 1 = Spam, 0 = Not Spam
data = {
    'message': [
        'Free money!!! Click here now!', 
        'Hi, how are you doing today?', 
        'Win a free iPhone instantly', 
        'Meeting scheduled for tomorrow', 
        'URGENT! You have won a lottery', 
        'Can we grab lunch later?',
        'Limited time offer! Buy now!',
        'Please review the attached report'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0] 
}

df = pd.DataFrame(data)

# 2. Preprocess and Vectorize
X = df['message']
y = df['label']

cv = CountVectorizer()
X_vectorized = cv.fit_transform(X)

# 3. Train the Model
model = MultinomialNB()
model.fit(X_vectorized, y)

# 4. Save the Model and Vectorizer
joblib.dump(model, 'spam_model.pkl')
joblib.dump(cv, 'vectorizer.pkl')

print("Success! Model and Vectorizer saved.")