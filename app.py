import streamlit as st
import analise_dados as ad

fig1 = ad.grafico_prop_viagens_semP(ad.df)
fig2 = ad.grafico_top_linhas_vazias(ad.df)
fig3 = ad.grafico_viagens_semP_por_hora(ad.df)
fig4 = ad.grafico_ar_condicionado(ad.rel)
fig5 = ad.grafico_veiculos_antes_2015(ad.rel)

st.set_page_config(page_title="Ônibus de Teresina", page_icon="🚌")

st.title("Análise do Transporte Coletivo de Teresina")
st.markdown("#### Apresentação dos dados coletados de viagens com e sem passageiros")

st.header("📊 Proporção de Viagens com e sem Passageiros")
st.markdown("Viagens que ocorreram com e sem passageiros no período avaliado.")
st.pyplot(fig1)

st.header("📌 Top 10 Linhas com Mais Viagens Vazias")
st.markdown("Essas são as linhas com maior incidência de viagens sem passageiros.")
st.pyplot(fig2)

st.header("🕒 Viagens sem Passageiros por Hora de Início")
st.markdown("Viagens sem passageiros por hora de início da operação.")
st.pyplot(fig3)

st.header("❄️ Presença de Ar Condicionado")
st.markdown("Distribuição da frota de ônibus com e sem ar condicionado.")
st.pyplot(fig4)

st.header("🚍 Veículos Fabricados até 2015")
st.markdown("Análise da quantidade de veículos fabricados até 2015 e a partir de 2016.")
st.pyplot(fig5)
