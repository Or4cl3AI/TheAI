```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class PredictiveAnalytics:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = RandomForestClassifier()

    def load_data(self):
        self.data = pd.read_csv(self.data_path)
        self.features = self.data.drop('threat', axis=1)
        self.labels = self.data['threat']

    def split_data(self):
        self.features_train, self.features_test, self.labels_train, self.labels_test = train_test_split(
            self.features, self.labels, test_size=0.2, random_state=42)

    def train_model(self):
        self.model.fit(self.features_train, self.labels_train)

    def predict_threat(self):
        self.predictions = self.model.predict(self.features_test)
        return self.predictions

    def evaluate_model(self):
        accuracy = accuracy_score(self.labels_test, self.predictions)
        return accuracy

    def save_model(self, model_path):
        with open(model_path, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, model_path):
        with open(model_path, 'rb') as file:
            self.model = pickle.load(file)

if __name__ == "__main__":
    analytics = PredictiveAnalytics('data.csv')
    analytics.load_data()
    analytics.split_data()
    analytics.train_model()
    predictions = analytics.predict_threat()
    accuracy = analytics.evaluate_model()
    print(f"Model Accuracy: {accuracy}")
    analytics.save_model('threat_prediction_model.pkl')
```
