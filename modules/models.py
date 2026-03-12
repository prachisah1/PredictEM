from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class TriageModel:

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.trained = False

    def train(self, X, y):

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model.fit(X_train, y_train)

        preds = self.model.predict(X_test)

        acc = accuracy_score(y_test, preds)

        print("Model Accuracy:", acc)

        self.trained = True

    def predict(self, patient):

        if not self.trained:
            raise Exception("Model not trained!")

        return self.model.predict([patient])[0]