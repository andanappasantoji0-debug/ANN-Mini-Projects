# ANN Mini Projects

This repository contains implementations of three fundamental Artificial Neural Network (ANN) models developed as part of a mini-project. The goal of this project is to understand neural network concepts through hands-on implementation and experimentation.

---

## Project Structure

ANN-Mini-Projects/
│
├── perceptron/
│   └── perceptron.py
│
├── competitive_learning/
│   └── competitive.py
│
├── feedforward_nn/
│   └── ffnn.py
│
└── README.md

---

## 1. Perceptron Model

### Objective
To implement a single-layer perceptron from scratch and use it for binary classification.

### Description
The perceptron is one of the earliest neural network models and is used to classify linearly separable data. In this project, the perceptron is trained on the AND logic gate dataset.

### Dataset Used

| Input 1 | Input 2 | Output |
|--------|--------|--------|
| 0      | 0      | 0      |
| 0      | 1      | 0      |
| 1      | 0      | 0      |
| 1      | 1      | 1      |

### How to Run


### Key Observations
- Works well for linearly separable problems
- Cannot solve XOR problem

---

## 2. Competitive Learning Network

### Objective
To implement a two-layer competitive learning network that performs unsupervised clustering on noisy 2D data.

### Description


Competitive learning is an unsupervised learning technique where neurons compete to respond to input data. Only the winning neuron updates its weights, leading to self-organization and clustering.

### Features
- Generates noisy 2D data automatically
- Uses winner-takes-all strategy
- Visualizes clusters using a scatter plot

### How to Run


### Output
- Cluster centers printed in terminal
- Scatter plot saved as `output.png`

### Key Observations
- Neurons specialize to detect specific clusters
- Performance depends on learning rate and number of neurons

---

## 3. Feedforward Neural Network

### Objective
To design and train a multi-layer feedforward neural network for digit classification.

### Description
A feedforward neural network with one hidden layer is implemented using the scikit-learn library. The network is trained on the built-in digits dataset.

### Dataset
- 1797 handwritten digit images
- Each image represented as 8×8 pixels
- 10 output classes (digits 0–9)

### How to Run


### Key Observations
- Handles complex nonlinear patterns
- Achieves high classification accuracy

---

## Technologies Used

- Python 3
- NumPy
- Matplotlib
- scikit-learn

---

## Installation

Install required libraries using pip:

---

## Running All Programs

You can run each module independently:


---

## Results Summary

| Model | Type | Learning | Performance |
|------|------|----------|-------------|
| Perceptron | Single-layer | Supervised | 100% on AND dataset |
| Competitive Network | Two-layer | Unsupervised | Successfully formed clusters |
| Feedforward Neural Network | Multi-layer | Supervised | ~90–98% accuracy |

---

## Challenges Faced

- Selecting appropriate learning rate
- Handling non-linear data in perceptron
- Choosing optimal number of neurons in competitive learning network
- Training convergence in feedforward network

---

## Learning Outcomes

Through this project, the following concepts were understood and implemented:

- Perceptron learning rule
- Competitive learning and self-organization
- Multi-layer neural network training
- Pattern classification and clustering

---

## License

This project is intended for academic and educational purposes only.
