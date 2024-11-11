import streamlit as st
import numpy as np
import pickle


with open("model.pkl","rb") as file:
    model = pickle.load(file)

st.title("Marks Predictor")
input1 = st.text_input("Number Of Hours Studied Daily (Select Value from 0-15)")
input2 = st.text_input("Previous Marks Obtained (Select Values from 0-500)")
input3 = st.text_input(" Involved in Extracurricular Activites ( Select Value 0 or 1 i.e. 0 For Involved and 1 for Not involved)")
input4 = st.text_input("Number of Sleeping Hours Daily")
input5 = st.text_input('Number Of Sample Papers Solved Daily')

if st.button("predict"):
    inputs = np.array([[input1,input2,input3,input4,input5]], dtype="i")
    output = model.predict(inputs)
    st.write(output)