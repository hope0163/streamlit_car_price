import streamlit as st
import pandas as pd

def run_eda():
    st.subheader('탐색적 데이터 분석')

    st.text('데이터프레임 보기 / 통계치 보기를 할 수 있습니다.')

    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    radio_menu = ['데이터프레임', '통계치']
    choice_radio = st.radio('선택하세요.', radio_menu)

    if choice_radio == radio_menu[0]:
        st.dataframe(df)

    else:
        st.dataframe(df.describe())

    # 각 컬럼별로 최대/최소 값을 보여주는 화면 개발
    # 유저가 컬럼을 선택하면 해당 컬럼의 최대 / 최소 데이터를 보여주도록

    st.text('컬럼을 선택하면 각 컬럼별 최대/최소 데이터를 보여드립니다.')
    column_list = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    choice_column = st.selectbox('컬럼을 선택하세요.', column_list)
    if choice_column[0]:
        st.text(f'{choice_column}값이 최대인 데이터')
        st.dataframe(df.loc[ df[choice_column].max() == df[choice_column] , ])
        st.text(f'{choice_column}값이 최소인 데이터')
        st.dataframe(df.loc[ df[choice_column].min() == df[choice_column] , ])

    elif choice_column[1]:
        st.text(f'{choice_column}값이 최대인 데이터')
        st.dataframe(df.loc[ df[choice_column].max() == df[choice_column] , ])
        st.text(f'{choice_column}값이 최소인 데이터')
        st.dataframe(df.loc[ df[choice_column].min() == df[choice_column] , ])
    
    elif choice_column[2]:
        st.text(f'{choice_column}값이 최대인 데이터')
        st.dataframe(df.loc[ df[choice_column].max() == df[choice_column] , ])
        st.text(f'{choice_column}값이 최소인 데이터')
        st.dataframe(df.loc[ df[choice_column].min() == df[choice_column] , ])

    elif choice_column[3]:
        st.text(f'{choice_column}값이 최대인 데이터')
        st.dataframe(df.loc[ df[choice_column].max() == df[choice_column] , ])
        st.text(f'{choice_column}값이 최소인 데이터')
        st.dataframe(df.loc[ df[choice_column].min() == df[choice_column] , ])

    elif choice_column[4]:
        st.text(f'{choice_column}값이 최대인 데이터')
        st.dataframe(df.loc[ df[choice_column].max() == df[choice_column] , ])
        st.text(f'{choice_column}값이 최소인 데이터')
        st.dataframe(df.loc[ df[choice_column].min() == df[choice_column] , ])