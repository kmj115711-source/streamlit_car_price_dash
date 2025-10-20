import streamlit as st

from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml


def _local_css():
    # 깔끔한 카드 스타일과 타이포그래피를 위한 간단한 CSS
    st.markdown("""
    <style>
    :root{
      --brand:#0f4c81;
      --accent:#ff6b6b;
      --muted:#6b6b6b;
      --bg:#f7fbff;
    }
    .stApp {
      background: linear-gradient(180deg, #ffffff 0%, var(--bg) 100%);
      color: #0b2545;
    }
    .app-header{
      padding: 12px 18px;
      border-radius: 8px;
      background: white;
      box-shadow: 0 6px 18px rgba(15,76,129,0.08);
      margin-bottom: 18px;
    }
    .card{ 
      background: white;
      padding: 18px;
      border-radius: 10px;
      box-shadow: 0 6px 18px rgba(15,76,129,0.06);
      margin-bottom: 16px;
    }
    .muted{ color: var(--muted); }
    .brand{ color: var(--brand); font-weight:600 }
    .small{ font-size:0.9rem }
    </style>
    """, unsafe_allow_html=True)


def main():
    _local_css()

    # 헤더 영역
    st.markdown('<div class="app-header">', unsafe_allow_html=True)
    st.title('🚗 자동차 구매 금액 예측')
    st.markdown('<div class="small muted">데이터 기반의 간편한 자동차 구매 금액 예측 대시보드</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 사이드바 브랜딩 및 메뉴
    st.sidebar.title('메뉴')
    st.sidebar.markdown('---')
    st.sidebar.image('./image/car.jpg', use_column_width=True)

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('', menu)

    if choice == 'Home':
        run_home()
    elif choice == 'EDA':
        run_eda()
    elif choice == 'ML':
        run_ml()


if __name__ == '__main__':
    main()