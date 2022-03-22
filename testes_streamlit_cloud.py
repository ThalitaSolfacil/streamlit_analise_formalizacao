import streamlit as st
import pandas as pd
import pyperclip3 as pc
import clipboard as c
import xerox

st.set_page_config(page_title = "Análise de IDs", page_icon=":mag:", layout = 'wide')


if st.button('Pandas'): pd.DataFrame(['Olá, pandas!']).to_clipboard(index =False, header = False)
if st.button('Pyperclip3'): pc.copy('Olá, Pyperclip3!')
if st.button('Clipboard'): c.copy('Olá, clipboard!')
if st.button('Xerox'): xerox.copy('Olá, xerox!')
    
    
    