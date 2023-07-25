```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

class DeepLearningModel:
    def __init__(self):
        self.model = Sequential()

    def create_model(self, input_shape):
        self.model.add(LSTM(128, input_shape=(input_shape), activation='relu', return_sequences=True))
        self.model.add(Dropout(0.2))

        self.model.add(LSTM(128, activation='relu'))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(10, activation='softmax'))

    def compile_model(self):
        self.model.compile(loss='sparse_categorical_crossentropy',
                           optimizer='adam',
                           metrics=['accuracy'])

    def train_model(self, x_train, y_train, epochs, validation_data):
        self.model.fit(x_train, y_train, epochs=epochs, validation_data=validation_data)

    def evaluate_model(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test)

    def predict(self, data):
        return self.model.predict(data)

dl_model = DeepLearningModel()
```