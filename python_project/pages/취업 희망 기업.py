import streamlit as st

st.set_page_config(
    page_title="취업하고 싶은 기업",
    page_icon="🔹"
)














import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from datetime import datetime

# 윈도우에서 Malgun Gothic 폰트를 Matplotlib에 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 초기 세션 상태 설정
if 'company_data' not in st.session_state:
    st.session_state.company_data = {}

# 초기 세션 상태 설정 - 데이터 최신화 시간
if 'last_updated_time' not in st.session_state:
    st.session_state.last_updated_time = {}

# 웹 페이지 제목 및 설명
st.title("취업 희망 기업 소개")

# 사이드바를 사용하여 탭 선택
selected_tab = st.sidebar.radio("탭을 선택하세요:", ["기업 소개", "주가 그래프"])

# 소개할 기업 목록
companies = {
    '삼성전자': {
        'ticker': '005930.KS',
        'website': 'https://www.samsung.com',
        'description': """
        삼성전자는 대한민국 반도체 산업의 큰 부분을 차지하고 있는 기업입니다. 주요 제품으로 스마트폰, 반도체, 디스플레이 패널 등이 있으며, 
        대한민국뿐만 아닌 세계 최대의 반도체 제조업체 중 하나로 자리잡고 있습니다. 반도체 공정, 회로 설계 등 모든 부분을 관여하는 종합반도체사(IDM)입니다.
        """,
        'desired_skills': """
        **취업에 필요한 요구사항:**
        - 전자공학, 컴퓨터 공학 등과 같은 공학 분야 전공자 
        - 반도체 설계 및 제조 기술에 대한 이해
        
        """,
        'logo_url': 'https://images.samsung.com/kdp/aboutsamsung/brand_identity/logo/720_600_1.png?$720_N_PNG$'
    },'SK하이닉스': {
        'ticker': '000660.KS',
        'website': 'https://www.skhynix.com',
        'description': """
        SK하이닉스는 한국의 반도체 제조 기업입니다. 주로 DRAM 및 NAND 플래시 메모리를 생산합니다, 삼성전자와 같은 종합반도체사(IDM)입니다.
        한국에서는 삼성전자가 시장을 대부분 점유하고 있지만, 중국 시장 매출 1위를 달성하며 글로벌 반도체 기업으로 성장하고 있습니다.
        """,
        'desired_skills': """
        **취업에 필요한 요구사항:**
        - 반도체 공정 및 기술에 대한 깊은 이해
        - 집적회로 설계 및 시스템 구현 능력
        - 데이터 분석 및 문제 해결 능력
        """,
        'logo_url': 'https://news.skhynix.co.kr/hubfs/0_Medialibrary_v2/Newsroom/SK%ED%95%98%EC%9D%B4%EB%8B%89%EC%8A%A4%20%EC%98%81%EB%AC%B8%20CI_1_%ED%9A%8C%EC%82%AC_%EC%82%AC%EC%A7%84_2020.jpg'
    },
    'ASML': {
        'ticker': 'ASML',
        'website': 'https://www.asml.com',
        'description': """
        ASML은 네델란드에 본사를 둔 세계적인 반도체 장비 제조 기업입니다. 반도체 공정 과정은 크게 8단계로 구분됩니다. 이 중 노광이라는 과정이 존재하는데, ASML은 최첨단 노광 장비를 개발 및 제조하여 
        반도체 제조 공정에서 핵심적인 역할을 하고 있습니다. sk 하이닉스 본사가 있는 이천과 가까운 화성에 ASML KOREA가 위치해 있습니다.
        만약 취업을 하게 된다면 이곳 ASML KOREA 지부로 취업하고 싶습니다.
        """,
        'desired_skills': """
        **취업에 필요한 요구사항:**
        - 광학공학 및 물리학에 대한 깊은 이해
        - 노광 기술 및 장비 개발 경험
        - 글로벌 프로젝트 관리 및 커뮤니케이션 능력
        """,
        'logo_url': 'https://www.logo.wine/a/logo/ASML_Holding/ASML_Holding-Logo.wine.svg'
    }
}

if selected_tab == "기업 소개":
    # 사이드바를 사용하여 회사 선택
    selected_company = st.sidebar.selectbox("회사를 선택하세요:", list(companies.keys()))

    # 선택한 회사의 정보
    company_info = companies[selected_company]
    ticker = company_info['ticker']
    website = company_info['website']
    description = company_info['description']
    desired_skills = company_info['desired_skills']
    logo_url = company_info['logo_url']

    # 기업 로고 이미지 표시
    st.image(logo_url, caption=f"{selected_company} 로고", use_column_width=True)

    # 기업 소개 표시
    st.subheader(f"{selected_company} 소개")
    st.markdown(description)
    st.markdown(desired_skills)

    # 기업 웹사이트 링크 표시
    st.subheader("공식 웹사이트")
    st.write(f"[{selected_company} 공식 웹사이트]({website})")

elif selected_tab == "주가 그래프":
    # 사이드바를 사용하여 회사 선택
    selected_company = st.sidebar.selectbox("회사를 선택하세요:", list(companies.keys()))

    # 선택한 회사의 정보
    company_info = companies[selected_company]
    ticker = company_info['ticker']
    website = company_info['website']

    # 데이터 가져오기 및 업데이트 함수 정의
    def update_data(ticker):
        stock_data = yf.Ticker(ticker)
        history = stock_data.history(period="1y")
        return history

    # 최신화 버튼을 클릭하여 데이터 갱신
    update_button = st.button('갱신')
    if update_button or selected_company not in st.session_state.company_data:
        st.session_state.company_data[selected_company] = update_data(ticker)
        st.session_state.last_updated_time[selected_company] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 최신화 시간 표시
    if selected_company in st.session_state.last_updated_time:
        st.write(f"데이터 갱신 시간: {st.session_state.last_updated_time[selected_company]}")

    # 주가 그래프를 그리는 함수
    def draw_stock_chart(history):
        fig, ax = plt.subplots()
        ax.plot(history.index, history['Close'], label='Stock Closing Price', linestyle='-', color='b')
        ax.set_xlabel('Date')
        ax.set_ylabel('Stock Price (USD)')
        ax.legend()
        ax.grid(True)  # 그리드 추가
        ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=True))  # 과학적 표기법 사용하지 않도록 설정
        return fig, ax

       # 주가 그래프 그리기
    st.header(f"{selected_company} 주가 그래프")
    fig, ax = draw_stock_chart(st.session_state.company_data[selected_company])
    st.pyplot(fig)

    # 시가총액 그래프 및 기업 웹사이트 표시
    st.subheader(f"{selected_company} 시가총액 그래프")
    history = st.session_state.company_data[selected_company]
    history['Shares Outstanding'] = yf.Ticker(ticker).info['sharesOutstanding']
    history['Market Cap'] = history['Close'] * history['Shares Outstanding']
    fig_market_cap, ax_market_cap = plt.subplots()
    ax_market_cap.plot(history.index, history['Market Cap'], label='Market Capitalization', linestyle='-', color='r')
    ax_market_cap.set_xlabel('Date')
    ax_market_cap.set_ylabel('Market Capitalization (USD)')
    ax_market_cap.legend()
    ax_market_cap.grid(True)  # 그리드 추가
    ax_market_cap.yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=True))  # 과학적 표기법 사용하지 않도록 설정
    st.pyplot(fig_market_cap)
