```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLPProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def process_language(self, text):
        # Tokenization
        tokens = word_tokenize(text)

        # Removing Stop Words
        filtered_tokens = [token for token in tokens if token not in self.stop_words]

        # Lemmatization
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in filtered_tokens]

        return lemmatized_tokens

nlp_model = NLPProcessor()
```