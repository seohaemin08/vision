import streamlit as st
import random

st.set_page_config(page_title="MBTI + 지역별 맛집 추천", page_icon="🍽️")

st.title("🍽️ MBTI와 지역에 따른 맛집 추천")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

regions = ["서울", "부산"]

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
    },
}

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)
selected_region = st.selectbox("지역을 선택하세요:", regions)

if st.button("맛집 추천받기"):
    region_data = restaurant_data.get(selected_region, {})
    mbti_rests = region_data.get(selected_mbti, [])

    if not mbti_rests:
        st.warning("해당 지역과 MBTI에 맞는 맛집 정보가 없습니다.")
    else:
        rest = random.choice(mbti_rests)
        st.markdown(f"### 🍽️ {rest['name']}")
        st.image(rest["image"], use_column_width=True)

st.markdown("---")
st.caption("💡 이미지와 맛집 정보는 예시이며 Pixabay 무료 이미지를 활용했습니다.")
