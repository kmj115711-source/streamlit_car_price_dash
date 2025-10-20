import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda():
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader('탐색적 데이터 분석 (EDA)')
    st.markdown('<div class="small muted">데이터 구조를 빠르게 파악하고 시각화합니다.</div>', unsafe_allow_html=True)

    # 데이터 / 통계 선택
    radio_menu = ['데이터 프레임', '기본통계']
    radio_choice = st.radio('보기', radio_menu, horizontal=True)
    if radio_choice == radio_menu[0]:
        st.dataframe(df)
    else:
        st.dataframe(df.describe())

    st.markdown('---')
    st.subheader('최대 / 최소값 확인')
    min_max_menu = df.columns[4:]
    select_choice = st.selectbox('컬럼을 선택하세요', min_max_menu)

    min_val = int(df[select_choice].min())
    max_val = int(df[select_choice].max())
    st.info(f'{select_choice}는 {min_val} 부터 {max_val} 까지 있습니다.')

    st.markdown('---')
    st.subheader('상관관계 분석')
    multi_menu = df.columns[4:]
    choice_multi_list = st.multiselect('컬럼을 2개 이상 선택하세요.', multi_menu)

    if len(choice_multi_list) >= 2:
        corr = df[choice_multi_list].corr(numeric_only=True)
        st.dataframe(corr)

        fig1, ax1 = plt.subplots(figsize=(6, 5))
        sb.heatmap(corr, vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8, ax=ax1)
        st.pyplot(fig1)

    st.markdown('---')
    st.subheader('각 컬럼간의 pair plot')
    vars_for_pair = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    # pairplot은 큰 리소스를 쓸 수 있으므로 선택적으로 렌더링
    if st.checkbox('Pair plot 표시 (시간이 걸릴 수 있음)'):
        try:
            g = sb.pairplot(data=df, vars=vars_for_pair)
            # seaborn의 PairGrid에서 figure 추출
            st.pyplot(g.fig)
        except Exception as e:
            st.error('pair plot 렌더링 중 오류가 발생했습니다: ' + str(e))

    st.markdown('</div>', unsafe_allow_html=True)
   
