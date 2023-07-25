```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

class MachineLearningModel:
    def __init__(self):
        self.ml_model = None

    def train_model(self, data, target):
        """
        Train the machine learning model
        """
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

        # Initialize the model
        self.ml_model = RandomForestClassifier(n_estimators=100)

        # Train the model
        self.ml_model.fit(X_train, y_train)

        # Predict the test set results
        y_pred = self.ml_model.predict(X_test)

        # Calculate the accuracy of the model
        accuracy = accuracy_score(y_test, y_pred)

        # Print the accuracy of the model
        print(f"Model Trained - Accuracy: {round(accuracy, 2)}")

        return self.ml_model

    def predict_threat(self, data):
        """
        Use the trained model to predict the threat
        """
        # Check if the model is trained
        if self.ml_model is None:
            print("Model is not trained. Train the model first.")
            return None

        # Predict the threat
        threat_prediction = self.ml_model.predict(data)

        return threat_prediction
```