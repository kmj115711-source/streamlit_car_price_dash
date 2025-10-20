import streamlit as st


def run_home():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader('자동차 데이터를 분석하고, 예측하는 앱')
    st.markdown('<div class="small muted">캐글에 공개된 Car_Purchasing_Data.csv 데이터를 사용했습니다.</div>', unsafe_allow_html=True)
    st.markdown('---')

    # 간단한 매트릭스
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('관측치 수', '1,000+')
    with col2:
        st.metric('특성 수', '7')
    with col3:
        st.metric('모델', '선형 회귀')

    st.markdown('<div class="muted small" style="margin-top:8px">탐색적 데이터 분석(EDA)과 머신러닝(ML) 예측을 하나의 대시보드에서 제공합니다.</div>', unsafe_allow_html=True)

    # 전체 화면(뷰포트) 너비로 이미지를 표시하도록 HTML 사용
    st.image('./image/car.jpg', use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

