# Train-Test Split in Machine Learning
### App Link
* https://train-test-split.streamlit.app/
## What is Train-Test Split?
* It is a process of dividing our dataset into **two parts**:
  * **Training data** – used to train the model
  * **Testing data** – used to test how well the model performs
* It helps check if our model works well **on new data**.
## Algorithm
* Load your full dataset.
* Use **`train_test_split()`** from sklearn.
* Set how much data goes to training (e.g., 80%) and testing (e.g., 20%).
* Train your model using the training set.
* Test your model using the test set.
* Use **random_state** to get repeatable results.
* Common split: **80% train & 20% test, or 70%-30%**.
