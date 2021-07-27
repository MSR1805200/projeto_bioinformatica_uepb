import streamlit as st #criação de aplicações web

class ComponenteArrastaESolta:
    
    def __init__(self):
        pass

    def visualizar_arrasta_e_solta(self):
        arquivo = st.sidebar.file_uploader('Solte o arquivo aqui', type = ['csv','xlsx'])
        return arquivo