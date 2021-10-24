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
            my_bar.progress(percent_complete +1)
        st.success("Super! Znaleziono tłumaczanie")
        st.write(answer)


st.write("S18490")
        

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
