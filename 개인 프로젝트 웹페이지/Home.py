import streamlit as st


st.set_page_config(
    
    page_title="C215226 이명진 개인 프로젝트", # 페이지 Tab의 타이틀
    page_icon="✔️",     # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃: centered, wide
    initial_sidebar_state="expanded", # 사이드바 초기 상태: auto, collapsed, expanded
    menu_items={        # 페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목: Get help, Report a bug, About,
        
        'About': "홍익대학교 C215226 이명진 파이썬프로그래밍 개인과제"
    }

)

st.header("관심 분야와 취업 희망 기업 소개")

st.sidebar.success("궁금한 부분을 선택해주세요.")

st.markdown(   # st.markdown()을 이용한 본문 작성
    """

   저는 홍익대학교 전자전기공학부에 재학중입니다.\n
   제 전공은 주로 전자 회로와 전기 회로에 관련한 지식을 배웁니다.\n
   그래서 저는 졸업 후 **반도체 기업**에 취업하려고 계획중입니다.\n
    **👈 왼쪽의 사이드바**에서 자세히 보고싶은 내용을 선택해주세요.
    
   

   """
)
 