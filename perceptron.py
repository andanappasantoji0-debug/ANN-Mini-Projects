import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0

        for epoch in range(self.epochs):
            for i in range(len(X)):
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_pred = 1 if linear_output >= 0 else 0

                self.weights += self.lr * (y[i] - y_pred) * X[i]
                self.bias += self.lr * (y[i] - y_pred)

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([1 if i >= 0 else 0 for i in linear_output])


if __name__ == "__main__":
    X = np.array([[0,0],[0,1],[1,0],[1,1]])
    y = np.array([0,0,0,1])

    model = Perceptron()
    model.fit(X, y)

    predictions = model.predict(X)

    print("Input:\n", X)
    print("Predicted Output:", predictions)
    print("Actual Output:", y)
