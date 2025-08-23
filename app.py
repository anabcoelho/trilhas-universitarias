import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta, timezone
import streamlit.components.v1 as components


# FUNCOES
def get_trilhas():
    df = pd.read_csv('./db/programacao_trilhas.csv', sep=';')
    df['data'] = pd.to_datetime(df['data'].str.split(' e ').str[0], format='%d/%m/%Y')
    hoje = datetime.today().date()
    df_filtrado = df[df['data'].dt.date >= hoje]
    df_filtrado = df_filtrado.sort_values(by="data")

    return df_filtrado


st.title("Trilhas Universitárias")

# --- Sidebar de navegação ---
pagina = st.sidebar.selectbox("Navegar para:", ['Início', 'Programação'])

if pagina == 'Início':
    st.markdown("[Instagram do Trilhas Universitárias](https://www.instagram.com/trilhasuniversitarias)")

    st.write("""
    Fala, galera! 😎✨

    Hoje somos mais de 4 mil aventureiros prontos para explorar o mundo e viver experiências únicas. E o melhor: crescemos tanto que agora temos três comunidades pra todo tipo de vibe!

    🥾 Comunidade 1.0 - Só trilha raiz! Pé na estrada, natureza, cachoeira e aquele cansaço que vale cada segundo.
    
    🎟 Comunidade 2.0 - Rolês insanos e gratuitos, ingressos para shows, paintball, futebol, passeio de barco, remo… e por aí vai!
    
    🏕 Comunidade 3.0 - Aventuras de montanha, camping e viagens pra quem curte virar a noite sob as estrelas.

    E o mais legal: agora o MAPAS e o TRILHAS são parceiros de vida! Vamos juntar forças pra criar atividades cada vez mais épicas — como bons irmãos de caminhada. 💚

    Agradecimento especial ao nosso querido professor José Otávio pela energia e presença nas aventuras.

    📢 Então já sabe: seja qual for sua vibe, vem com a gente! Participe, conheça pessoas incríveis e viva histórias que você vai contar pro resto da vida.

    🚀 MAPAS + TRILHAS = Felicidade garantida!
    """)

    #st.markdown('## Links')
    #for nome, link in trilhas_mapas.items():
    #    st.markdown(f"[{nome}]({link})")

    st.markdown("## Como funciona?")
    st.markdown("""

    Para facilitar a organização, criamos subgrupos temporários para cada atividade que vai acontecer na semana.
    O passo a passo é simples:

    1. Escolha a atividade que quer participar na nossa programação.
    2. Entre no subgrupo específico daquela atividade (o link será enviado no grupo principal).
    3. No subgrupo, você receberá todos os detalhes: horário, ponto de encontro, o que levar, etc.
    4. Após o término da atividade, o subgrupo será apagado — assim mantemos tudo organizado e pronto para os próximos eventos.

    💡 Importante: novas atividades podem surgir a qualquer momento! Então, o calendário pode sofrer alterações. Fique de olho para não perder nada.
    """)

# --- Página: Programação---
elif pagina == "Programação":
    st.header("Programação")

    
    df = get_trilhas()
    for index, row in df.iterrows():
        grupo_link = f"[Entrar no grupo]({row['grupo']})" if pd.notna(row['grupo']) else 'Não definido'

        st.markdown(f"""
        **📅 Data:** {row['data'].strftime('%d/%m/%Y')}

        **📌 Evento:** {row['evento']}

        **📝 Descrição:** {row['descrição']}
        ---
        """)

#**👥 Grupo:** {grupo_link}



