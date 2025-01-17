import pandas as pd

# Load the dataset
spam_file_path = '/content/spam.csv'
spam_df = pd.read_csv(spam_file_path, encoding='latin-1')

# Display the first few rows of the dataset
spam_df.head(), spam_df.info(), spam_df.describe()

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Drop unnecessary columns
spam_df = spam_df[['v1', 'v2']]

# Rename columns
spam_df.columns = ['label', 'message']

# Encode labels
spam_df['label'] = spam_df['label'].map({'ham': 0, 'spam': 1})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(spam_df['message'], spam_df['label'], test_size=0.2, random_state=42)

# Create a pipeline with CountVectorizer and MultinomialNB
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

accuracy, conf_matrix, class_report
