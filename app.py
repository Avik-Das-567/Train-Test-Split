import streamlit as st
from sklearn.model_selection import train_test_split

# Sample data
X = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 20, 30, 40, 50, 60, 70, 80]

# Split the data: 75% train, 25% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

st.write("Training Data:", X_train, y_train)
st.write("Testing Data:", X_test, y_test)