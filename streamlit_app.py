import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.title('Translator angielsko-niemiecki')
from PIL import Image
img = Image.open("flagi.png")
st.image(img)

st.text('Ta aplikacja służy do tłumaczanie z języka angielskiego na niemiecki')

from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
       "Angielski -> Niemiecki",
       
    ],
)

if option == "Angielski -> Niemiecki":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("translation_en_to_de")
        answer = classifier(text)
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        st.success("Super! Znaleziono tłumaczanie")
        st.write(answer)


st.write("S18490")
        


