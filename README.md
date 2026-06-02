# Tech Challenge 4 - Obesity Prediction

## Objetivo

Desenvolver um modelo de Machine Learning capaz de prever níveis de obesidade com base em características demográficas, hábitos alimentares e estilo de vida, auxiliando profissionais da saúde no processo de tomada de decisão.

## Tecnologias utilizadas

* Python
* Pandas
* NumPy
* Scikit-Learn
* Random Forest
* Streamlit
* Power BI

## Estrutura do projeto

```text
├── data/
│   └── Obesity.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_training.ipynb
│
├── streamlit/
│   ├── obesity_model.pkl
│   └── app.py
│
├── dashboard/
│   └── Dashboard - Obesity Analysis.pbix
│
├── requirements.txt
└── README.md
```

## Execução local

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run streamlit/app.py
```

## Resultados

* Modelo selecionado: Random Forest
* Accuracy: 79%
* Avaliação realizada utilizando conjunto de teste separado do treinamento.

## Links

### [Aplicação Streamlit](https://fiap-data-analytics-tc4-obesity-prediction-fdeaegtjfddkuydpkd6.streamlit.app/)

### [Dashboard analítico](https://app.powerbi.com/view?r=eyJrIjoiNzVmYjJmYTMtYjdkNi00ZWM4LWIyM2ItYTY5NDdiNjkwNWU4IiwidCI6Ijc2MmU1ODhmLTMxOTgtNGUzYS04Y2VkLWM1MTZjZGU3ZTg1NiJ9)

### [Vídeo de apresentação](https://www.youtube.com/watch?v=4z3HHzEyyTU)

## Autor

Luiz Carvalho
Pós-graduação em Data Analytics – FIAP
