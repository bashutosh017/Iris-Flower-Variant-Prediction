import streamlit as st
import requests

st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon=":cherry_blossom:",
    layout="centered"
)

st.title(":cherry_blossom: Iris Flower Prediction")
st.markdown(
    "Measuerment are in centimeters(CM)"
)

sepal_length=st.slider("Sepal Length",4.0,8.0,5.1)
sepal_width=st.slider("Sepal Width",2.0,4.5,3.1)
petal_length=st.slider("Petal Length",1.0,7.0,1.2)
petal_width=st.slider("Petal Width",0.1,2.5,0.6)

if st.button("Predict"):
    data={
        "sepal_length":sepal_length,
        "sepal_width":sepal_width,
        "petal_length":petal_length,
        "petal_width":petal_width
    }
    response=requests.post("http://localhost:8000/predict",json=data)
    if response.status_code==200:
        result=response.json()
        st.success(f"Prediccted Class: {result['prediction'].capitalize()}")
    else:
        st.error("Prediction Failed")