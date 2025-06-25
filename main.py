import streamlit as st
import random

st.set_page_config(page_title="MBTI + 지역별 맛집 추천", page_icon="🍽️")

st.title("🍽️ MBTI와 지역에 따른 맛집 추천")

# MBTI 유형
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 지역 리스트 (예시)
regions = ["서울", "부산"]

# MBTI별 지역별 맛집 데이터 (가게 이름, 음식 사진 URL)
# 실제 프로젝트면 DB나 API로 관리하세요
restaurant_data = {
    "서울": {
        "ISTJ": [
            {
                "name": "전통 한식집 서울점",
                "image": "https://cdn.pixabay.com/photo/2017/12/09/08/18/korean-food-3004441_1280.jpg"
            },
            {
                "name": "가성비 백반집",
                "image": "https://cdn.pixabay.com/photo/2018/10/29/15/06/korean-food-3784015_1280.jpg"
            },
        ],
        "ENFP": [
            {
                "name": "인스타 핫플 카페",
                "image": "https://cdn.pixabay.com/photo/2017/08/06/13/11/coffee-2595553_1280.jpg"
            },
            {
                "name": "푸드트럭 서울",
                "image": "https://cdn.pixabay.com/photo/2017/06/16/11/40/street-food-2400729_1280.jpg"
            },
        ],
        # ...다른 MBTI 생략
    },
    "부산": {
        "ISTJ": [
            {
                "name": "부산 전통 한식집",
                "image": "https://cdn.pixabay.com/photo/2016/03/05/19/02/korean-food-1239429_1280.jpg"
            }
        ],
        "ENFP": [
            {
                "name": "부산 해변가 카페",
                "image": "https://cdn.pixabay.com/photo/2016/11/29/03/52/coffee-1869716_1280.jpg"
            }
        ],
        # ...다른 MBTI 생략
    },
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)
selected_region = st.selectbox("지역을 선택하세요:", regions)

if st.button("맛집 추천받기"):
    region_data = restaurant_data.get(selected_region, {})
    mbti_rests = region_data.get(selected_mbti, [])

    if not mbti_rests:
