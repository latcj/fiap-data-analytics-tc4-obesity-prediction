#!/usr/bin/env python
# coding: utf-8

# ## Importações

# In[2]:


from pathlib import Path

import streamlit as st
import pandas as pd
import joblib


# ## Configuração da página

# In[4]:


st.set_page_config(
    page_title="Obesity Prediction",
    page_icon="🏥",
    layout="wide"
)


# ## Carregamento do Modelo

# In[6]:


MODEL_PATH = Path(__file__).resolve().parent / "obesity_model.pkl"

@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except Exception as exc:
        st.error("Falha ao carregar o modelo. Verifique se a dependência scikit-learn está na versão 1.5.1 e execute novamente.")
        st.exception(exc)
        return None

model = load_model()


# ## Título

# In[8]:


st.title("🏥 Obesity Prediction System")

st.markdown("""
Sistema preditivo para auxiliar a equipe médica
na identificação de níveis de obesidade.
""")


# ## Formulário
# Linha 1

# In[10]:


col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:
    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=25
    )

with col3:
    family_history = st.selectbox(
        "Family History",
        ["yes", "no"]
    )


# Linha 2

# In[12]:


col1, col2, col3 = st.columns(3)

with col1:
    favc = st.selectbox(
        "High Calorie Food Consumption",
        ["yes", "no"]
    )

with col2:
    fcvc = st.slider(
        "Vegetable Consumption",
        min_value=1.0,
        max_value=3.0,
        value=2.0
    )

with col3:
    ncp = st.slider(
        "Main Meals Per Day",
        min_value=1.0,
        max_value=4.0,
        value=3.0
    )


# Linha 3

# In[14]:


col1, col2, col3 = st.columns(3)

with col1:
    caec = st.selectbox(
        "Food Between Meals",
        ["no", "Sometimes", "Frequently", "Always"]
    )

with col2:
    smoke = st.selectbox(
        "Smoking",
        ["yes", "no"]
    )

with col3:
    ch2o = st.slider(
        "Water Consumption",
        min_value=1.0,
        max_value=3.0,
        value=2.0
    )


# Linha 4

# In[16]:


col1, col2, col3 = st.columns(3)

with col1:
    scc = st.selectbox(
        "Monitor Calories",
        ["yes", "no"]
    )

with col2:
    faf = st.slider(
        "Physical Activity",
        min_value=0.0,
        max_value=3.0,
        value=1.0
    )

with col3:
    tue = st.slider(
        "Technology Usage",
        min_value=0.0,
        max_value=2.0,
        value=1.0
    )


# Linha 5

# In[18]:


col1, col2 = st.columns(2)

with col1:
    calc = st.selectbox(
        "Alcohol Consumption",
        ["no", "Sometimes", "Frequently", "Always"]
    )

with col2:
    mtrans = st.selectbox(
        "Transportation",
        [
            "Walking",
            "Bike",
            "Motorbike",
            "Public_Transportation",
            "Automobile"
        ]
    )


# ## Preparação dos dados

# In[20]:


input_data = pd.DataFrame({
    'Gender': [gender],
    'Age': [age],
    'family_history': [family_history],
    'FAVC': [favc],
    'FCVC': [fcvc],
    'NCP': [ncp],
    'CAEC': [caec],
    'SMOKE': [smoke],
    'CH2O': [ch2o],
    'SCC': [scc],
    'FAF': [faf],
    'TUE': [tue],
    'CALC': [calc],
    'MTRANS': [mtrans]
})


# ##  Predição

# In[22]:

if model is not None and st.button("Predict Obesity Level"):

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Obesity Level: {prediction}")

    try:
        probabilities = model.predict_proba(input_data)[0]
    except AttributeError:
        probabilities = None

    if probabilities is not None:
        st.subheader("Prediction Confidence")
        classes = model.classes_
        prob_df = pd.DataFrame({
            "Class": classes,
            "Probability": probabilities
        })
        st.dataframe(prob_df)
    else:
        st.info("O modelo não fornece probabilidades. A previsão foi exibida acima.")


# ## Probabilidades

# In[24]:


if st.button("Predict Obesity Level"):

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    st.success(
        f"Predicted Obesity Level: {prediction}"
    )

    st.subheader("Prediction Confidence")

    classes = model.classes_

    prob_df = pd.DataFrame({
        "Class": classes,
        "Probability": probabilities
    })

    st.dataframe(prob_df)


# ## Rodapé

# In[26]:


st.divider()

st.caption(
    "FIAP Tech Challenge 4 - Obesity Prediction"
)

