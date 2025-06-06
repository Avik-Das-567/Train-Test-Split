# Train-Test Split in Machine Learning
### App Link
- https://train-test-split.streamlit.app/
---
### What is Train-Test Split?
- It is a process of dividing your dataset into **two parts**:
  - **Training data** - used to train the model
  - **Testing data** - used to test how well the model performs
- It helps check if your model works well **on new data**.
- **Real-Life Example:** Think of studying for a test. You read 80% of the book (**Training**), and solve 20% as a test (**Testing**) to check your understanding.
- Common Split: **80% train & 20% test**, or **70%-30%**. It helps avoid **overfitting**.
---
### Required Python Packages
- **`scikit-learn`**
- **`streamlit`**
---
### Algorithm
- Load your full dataset.
- Use **`train_test_split()`** from sklearn.
- Set how much data goes to training (e.g., **80%**) and testing (e.g., **20%**).
- Train your model using the training set.
- Test your model using the test set.
- Use **random_state** to get repeatable results.
---
### Output Example
```
Training Data: [1, 8, 3, 5, 4, 7] [10, 80, 30, 50, 40, 70]
Testing Data: [2, 6] [20, 60]
```
---
