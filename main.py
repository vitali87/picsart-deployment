from sklearn.datasets import fetch_openml
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

data = fetch_openml("heart-statlog")
df = data.frame
X, y = df.iloc[:, :-1], df.iloc[:, [-1]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

st.title("Heart Disease Diagnosis")

age = st.text_input("Enter age", "")
sex = st.text_input("Enter gender: 1-male, 0-female", "")
chest = st.text_input(
    "Enter chest pain type: 1-typical angina, 2-atypical angina, 3-nonanginal pain, 4-asymptomatic",
    "",
)
resting_blood_pressure = st.text_input("Enter resting blood pressure", "")
serum_cholestoral = st.text_input("Enter serum cholestoral", "")
fasting_blood_sugar = st.text_input(
    "Is fasting blood sugar > 120mg/dL: 1-yes, 0-no", ""
)
resting_electrocardiographic_results = st.text_input(
    "Enter resting electrocardiographic results: 0-normal, 1-having ST-T waveabnormality, 2-left ventricular hypertrophy",
    "",
)
maximum_heart_rate_achieved = st.text_input("Enter maximum heart rate achieved", "")
exercise_induced_angina = st.text_input(
    "Is it exercise induced angina?: 1-yes, 0-no", ""
)
oldpeak = st.text_input(
    "Enter old peak, i.e. ST depression induced by exercise relative to rest", ""
)
slope = st.text_input(
    "Enter the slope of the peak exercise ST segment : 1-upsloping, 2-flat, 3-downsloping",
    "",
)
number_of_major_vessels = st.text_input(
    "Enter number of major vessels (0-3) colored by flourosopy", ""
)
thal = st.text_input(
    "Enter defect type: 3 = normal; 6 = fixed defect; 7 = reversable defect", ""
)
d= {
    "age": [int(age)],
    "sex": [int(sex)],
    "chest": [chest],
    "resting_blood_pressure": [resting_blood_pressure],
    "serum_cholestoral": [serum_cholestoral],
    "fasting_blood_sugar": [fasting_blood_sugar],
    "resting_electrocardiographic_results": [resting_electrocardiographic_results],
    "maximum_heart_rate_achieved": [maximum_heart_rate_achieved],
    "exercise_induced_angina": [exercise_induced_angina],
    "oldpeak": [oldpeak],
    "slope": [slope],
    "number_of_major_vessels": [number_of_major_vessels],
    "thal": [thal],
}
X_input = pd.DataFrame(d)

if st.button("Predict"):
    st.write(f"{clf.predict(X_input)}")
