import streamlit as st
import random

st.set_page_config(page_title="MBTI 맛집 추천기", page_icon="🍽️")

st.title("🍽️ MBTI별 맛집 추천 앱")
st.write("내 MBTI에 딱 맞는 맛집 스타일을 추천받아 보세요!")

# MBTI 유형 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI별 맛집 스타일 사전
mbti_restaurant = {
    "ISTJ": ["전통 한식집", "가성비 좋은 백반집"],
    "ISFJ": ["따뜻한 분위기의 카페", "가족적인 분식집"],
    "INFJ": ["아늑한 북카페", "채식 전문 레스토랑"],
    "INTJ": ["미슐랭 레스토랑", "컨셉 있는 이색 카페"],
    "ISTP": ["바비큐 전문점", "아웃도어 분위기 펍"],
    "ISFP": ["감성 가득한 브런치 카페", "홈메이드 베이커리"],
    "INFP": ["이색 디저트 카페", "조용한 와인바"],
    "INTP": ["퓨전 레스토랑", "코워킹 스페이스 카페"],
    "ESTP": ["트렌디한 바 & 클럽", "스포츠 펍"],
    "ESFP": ["분위기 좋은 펍", "야외 테라스 카페"],
    "ENFP": ["인스타 핫플 카페", "푸드트럭 & 스트리트 푸드"],
    "ENTP": ["창의적인 퓨전 음식점", "테마 레스토랑"],
    "ESTJ": ["회식하기 좋은 고깃집", "가성비 술집"],
    "ESFJ": ["가족 모임 가능한 한식집", "따뜻한 카페"],
    "ENFJ": ["모임하기 좋은 레스토랑", "분위기 좋은 와인바"],
    "ENTJ": ["고급 스테이크하우스", "파인 다이닝 레스토랑"],
}

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

if st.button("맛집 추천받기"):
    recommendations = mbti_restaurant.get(mbti, [])
    if recommendations:
        choice = random.choice(recommendations)
        st.success(f"✨ 당신의 MBTI({mbti})에 어울리는 맛집 스타일 추천: **{choice}**")
    else:
        st.error("추천할 맛집 스타일이 없습니다.")

st.markdown("---")
st.caption("💡 MBTI별 성향에 맞춘 맛집 추천 예시입니다. 원하는 스타일로 자유롭게 수정해 보세요!")
