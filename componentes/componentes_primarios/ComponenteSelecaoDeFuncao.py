import streamlit as st


class ComponenteSelecaoDeFuncao:
    def __init__(self):
        pass

    def visualizar_opcoes(self):
        opcao = st.sidebar.selectbox('Selecione a opção',['Visualização dos dados',
                                            'Análise',
                                             'Criação de gráficos'
                                          ])

        return opcao
