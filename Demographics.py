import pandas as pd
import streamlit as st

st.title('都道府県 男女 人口推移')

df = pd.read_csv('c01.csv', encoding='shift-jis')

st.title('人口推移')
#都道府県を選んでくださいの所
st.sidebar.write("""
# 条件分岐
""")

eras = df['都道府県名'].unique()

selected = st.sidebar.multiselect(
    '都道府県を選んでください',
    eras
)
##############################
#元号を選んでくださいの所

era_name = df['元号'].unique().tolist()#これはリスト形式ではないのでtolistが必要

selected_era_name = st.sidebar.multiselect(
    '元号を選んでください',
    era_name
)

filterd_df = df[(df['都道府県名'].isin(selected))& (df['元号'].isin(selected_era_name))]

st.write(filterd_df)