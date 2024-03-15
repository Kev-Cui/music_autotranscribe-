# Import python libraries
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import os
import tempfile
from IO_framework import iScribe

def ml():

    st.image('images/bank-loan.jpeg')
    st.title("Upload a mp3 file to get notes in MIDI")

    # loading the model
    # models_path = 'models/'
    # model_name = models_path + 'logistic_model.pkl'
    # loaded_model = pickle.load(open(model_name, 'rb'))

    # Lists of accptable values
    # valid_types = ['PRIJEM', 'VYDAJ', 'VYBER']
    # valid_operation = ['PREVOD Z UCTU', 'VKLAD', 'VYBER', 'PREVOD NA UCET','VYBER KARTOU']
    # valid_ksymbol = ['UROK', 'SIPO', 'SLUZBY']
    # valid_duration = ['12', '24', '36', '48', '60']

    # Get input values.
    uploaded_file = st.file_uploader("Choose a file")
    # type = st.selectbox("Please enter the type of transaction: ",valid_types, key = '2')
    # operation = st.selectbox("Please enter the operation: ",valid_operation, key = '3')
    # t_amount = st.number_input("Please enter the transaction amount: ")
    # balance = st.number_input("Please enter the balance: ")
    # k_symbol = st.selectbox("Please enter the k_symbol: ",valid_ksymbol, key = '4')
    # l_amount = st.number_input("Please enter the loan amount: ")
    # duration = st.radio("Please enter the loan duration: ",valid_duration, key = '5')
    # payments = st.number_input("Please enter the payments: ")

    # when 'Predict' is clicked, make the prediction and store it
    if st.button('Process File'):
        # Check if a file has been uploaded
        if uploaded_file is not None:
            # Create a temporary file
            tfile = tempfile.NamedTemporaryFile(delete=False) 
            tfile.write(uploaded_file.getvalue())
            
            # Call your function with the file path as input
            midi_file = iScribe(mp3_file_path = tfile.name)

            # Create a download button for the MIDI file
            st.download_button(
                label="Download MIDI File",
                data=midi_file,
                file_name='output.mid',
                mime='audio/midi'
            )

            # Remove the temporary file
            os.unlink(tfile.name)
        else:
            st.write("No file uploaded")