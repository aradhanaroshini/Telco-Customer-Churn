import streamlit as st
st.title("Telecommunication company customer churn")
st.text("For calculating churn data for new customers please enter the following:")


custID=st.text_input("Enter Customer ID:")
gender=st.radio("Select Gender:",['Male','Female'])
snrciti=st.radio("Senior Citizen (Yes-1,No-0):",[1,0])
partner=st.radio("Partner:",['Yes','No'])
dependents=st.radio("Dependents:",['Yes','No'])
tenure=st.number_input("Tenure:")
phone=st.radio("Phone Service:",['Yes','No'])
line=st.radio("Multiple Line:",['Yes','No','No Phone Service'])
netservice=st.radio("Internet Service:",['DSL', 'Fiber optic', 'No'])
security=st.radio("OnlineSecurity:",['Yes','No','No internet service'])
backup=st.radio("Online Backup:",['Yes','No','No internet service'])
protection=st.radio("Device Protection:",['Yes','No','No internet service'])
support=st.radio("Tech Support:",['Yes','No','No internet service'])
TV=st.radio("Streaming TV:",['Yes','No','No internet service'])
movies=st.radio("Streaming Movies:",['Yes','No','No internet service'])
contract=st.radio("Contract:",['Month-to-month', 'One year', 'Two year'])
bill=st.radio("Paperless Billing:",['Yes','No'])
payment=st.radio("Payment Method:",['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
charges=st.number_input("Monthly Charges:")
total=st.number_input("Total Charges:")

submit=st.button("SUBMIT")

import pickle as pkl

model = pkl.load(open("model.pkl","rb"))

import numpy as np
import pandas as pd
input_df = pd.DataFrame([[gender, snrciti, partner, dependents, tenure, phone, line,
                          netservice, security, backup, protection, support, 
                         TV, movies, contract, bill, payment, charges, total]], 
                         columns=["gender", "SeniorCitizen", "Partner", "Dependents", 
                                  "tenure", "PhoneService", "MultipleLines", "InternetService"
                                  , "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", 
                                                                                                                                                                                                       "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"])
tenure = float(tenure)
charges = float(charges)
total = float(total)
snrciti = int(snrciti)


if (submit):
    

    prediction=model.predict(input_df)
    st.text("Churn prediction is:")
    if prediction[0]==1:
        st.success("Yes")
    else:
        st.error("No")
    

