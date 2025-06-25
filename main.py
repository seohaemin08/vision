import streamlit as st

# 전라도 광주 MBTI별 맛집 데이터
mbti_data = {
    "INFP": {
        "restaurant": "광주 무등산 떡갈비",
        "feature": "부드럽고 달콤한 수제 떡갈비, 전통적인 맛",
        "rating": 4.8,
        "address": "광주 동구 무등로 123",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EB%AC%B4%EB%93%B1%EC%82%B0+%EB%96%A1%EA%B0%88%EB%B9%84",
    },
    "ESTJ": {
        "restaurant": "광주 송정떡갈비",
        "feature": "넉넉하고 푸짐한 떡갈비 정식, 현지인 추천 맛집",
        "rating": 4.6,
        "address": "광주 북구 설죽로 200",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%86%A1%EC%A0%95%EB%96%A1%EA%B0%88%EB%B9%84",
    },
    "ENFP": {
        "restaurant": "광주 충장로 김치찌개",
        "feature": "매콤하고 깊은 맛의 김치찌개, 활기찬 분위기",
        "rating": 4.5,
        "address": "광주 동구 충장로 45",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%B6%A9%EC%9E%A5%EB%A1%9C+%EA%B9%80%EC%B9%98%EC%B0%8C%EA%B0%9C",
    },
    "ISTJ": {
        "restaurant": "광주 송정 떡집",
        "feature": "전통 손맛 가득한 떡, 깔끔한 서비스",
        "rating": 4.4,
        "address": "광주 북구 송정로 77",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%86%A1%EC%A0%95+%EB%96%A1%EC%A7%91",
    },
}

st.title("광주 MBTI별 맛집 추천 앱")

mbti_input = st.text_input("MBTI를 입력하세요 (예: INFP)").upper().strip()

if mbti_input:
    if mbti_input in mbti_data:
        info = mbti_data[mbti_input]
        st.subheader(f"추천 맛집: {info['restaurant']}")
        st.write(f"**특징:** {info['feature']}")
        st.write(f"**평점:** {info['rating']} ⭐")
        st.write(f"**주소:** {info['address']}")
        st.markdown(f"[지도에서 위치 보기]({info['map_url']})")
    else:
        st.error("해당 MBTI 맛집 정보가 없습니다. 정확한 MBTI를 입력해주세요.")
