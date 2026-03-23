import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
data = np.vstack([
    np.random.randn(50,2) + [2,2],
    np.random.randn(50,2) + [-2,-2],
    np.random.randn(50,2) + [2,-2]
])

class CompetitiveNetwork:
    def __init__(self, neurons=3, lr=0.1):
        self.neurons = neurons
        self.lr = lr

    def fit(self, X, epochs=50):
        self.weights = np.random.randn(self.neurons, X.shape[1])

        for _ in range(epochs):
            for x in X:
                distances = np.linalg.norm(self.weights - x, axis=1)
                winner = np.argmin(distances)
                self.weights[winner] += self.lr * (x - self.weights[winner])

    def predict(self, X):
        labels = []
        for x in X:
            distances = np.linalg.norm(self.weights - x, axis=1)
            labels.append(np.argmin(distances))
        return labels


if __name__ == "__main__":
    model = CompetitiveNetwork()
    model.fit(data)

    labels = model.predict(data)

    print("Final Weights (Cluster Centers):")
    print(model.weights)

    plt.scatter(data[:,0], data[:,1], c=labels)
    plt.scatter(model.weights[:,0], model.weights[:,1], marker='x')
    plt.title("Competitive Learning Output")
    plt.savefig("output.png")
    plt.show()
