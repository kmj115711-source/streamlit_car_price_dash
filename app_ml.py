import streamlit as st
import joblib
import pandas as pd


def run_ml():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader('구매 금액 예측하기')
    st.markdown('<div class="small muted">아래 정보를 입력하면 머신러닝 모델이 예상 구매 금액을 안내합니다.</div>', unsafe_allow_html=True)

    gender_list = ['여자', '남자']

    with st.form('prediction_form'):
        col1, col2 = st.columns([1, 2])
        with col1:
            gender = st.radio('성별', gender_list)
            age = st.number_input('나이', min_value=18, max_value=100, value=30)
        with col2:
            salary = st.number_input('연봉(달러)', min_value=0, value=50000, step=1000)
            debt = st.number_input('카드 빚(달러)', min_value=0, value=1000, step=100)
            worth = st.number_input('자산(달러)', min_value=0, value=20000, step=1000)

        submitted = st.form_submit_button('예측하기')

    if submitted:
        gender_data = 0 if gender == gender_list[0] else 1

        # 모델 로드
        try:
            regressor = joblib.load('./model/regressor.pkl')
        except Exception as e:
            st.error('모델을 불러오는 데 실패했습니다. model/regressor.pkl 파일을 확인하세요.\n' + str(e))
            return

        new_data = [{'Gender': gender_data, 'Age': age, 'Annual Salary': salary, 'Credit Card Debt': debt, 'Net Worth': worth}]
        df_new = pd.DataFrame(new_data)

        try:
            y_pred = regressor.predict(df_new)
        except Exception as e:
            st.error('예측 중 오류가 발생했습니다: ' + str(e))
            return

        pred_val = float(y_pred[0])
        if pred_val <= 0:
            st.warning('예측 결과가 유효하지 않습니다. 입력값을 확인해주세요.')
        else:
            price = f"{round(pred_val):,}"
            st.success(f'예측한 금액은 {price} 달러 입니다.')

    st.markdown('</div>', unsafe_allow_html=True)

 

        