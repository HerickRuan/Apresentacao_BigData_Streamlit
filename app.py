import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar arquivos
jan = pd.read_excel("arquivos/01-relfatporlinhaveiculoviagem_jan25.xlsx")
fev = pd.read_excel("arquivos/02-relfatporlinhaveiculoviagem_fev25.xlsx")
mar = pd.read_excel("arquivos/03-relfatporlinhaveiculoviagem_mar25.xlsx")
rel = pd.read_csv("arquivos/relveiculos (ABR25).csv", sep=';', encoding='latin1')

# Adicionando a Coluna "Mês" nas 3 tabelas
jan['Mês'] = 'Janeiro'
fev['Mês'] = 'Fevereiro'
mar['Mês'] = 'Março'

# Juntando as tabelas em uma (df)
df = pd.concat([jan, fev, mar], ignore_index=True)

# Filtra viagens sem passageiros
df['Passageiros'] = pd.to_numeric(df['Passageiros'], errors='coerce')
df['Data Hora Início Operação'] = pd.to_datetime(df['Data Hora Início Operação'], errors='coerce')
df['hora_inicio'] = df['Data Hora Início Operação'].dt.hour

df_semP = df[df['Passageiros'] == 0]
viagens_sem_passageiros_por_hora = df_semP['hora_inicio'].value_counts().sort_index()

st.title("Análise das Viagens sem Passageiros")

# Gráfico
fig, ax = plt.subplots()
ax.plot(viagens_sem_passageiros_por_hora.index, viagens_sem_passageiros_por_hora.values, marker='o')
ax.set_xlabel("Hora do Dia")
ax.set_ylabel("Número de Viagens sem Passageiros")
ax.set_title("Viagens sem Passageiros por Hora de Início")

st.pyplot(fig)
