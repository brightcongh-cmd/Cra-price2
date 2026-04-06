import streamlit as st
import pickle

# Charger le modèle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Titre de l'app
st.title("Car Price Prediction ")

st.write("Enter the details below:")

# Inputs utilisateur
year = st.number_input("Year", min_value=1900.0, max_value=2100.0, value=2020.0)
mileage = st.number_input("Mileage", min_value=0.0, value=50000.0)
engine = st.number_input("Engine Size", min_value=0.0, value=2.0)
doors = st.number_input("Number of Doors", min_value=1.0, max_value=10.0, value=4.0)

# Bouton de prédiction
if st.button("Predict"):
    try:
        prediction = model.predict([[year, mileage, engine, doors]])
        st.success(f"Predicted Price: {prediction[0]}")
    except Exception as e:
        st.error(f"Error: {e}")