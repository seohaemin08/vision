import streamlit as st

# 광주 지역 MBTI별 맛집 데이터 예시 (16개 MBTI 모두 포함)
mbti_data = {
    "INFP": {
        "restaurant": "무등산 떡갈비",
        "feature": "부드럽고 달콤한 수제 떡갈비, 전통적인 맛",
        "rating": 4.8,
        "address": "광주 동구 무등로 123",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EB%AC%B4%EB%93%B1%EC%82%B0+%EB%96%A1%EA%B0%88%EB%B9%84",
    },
    "ESTJ": {
        "restaurant": "송정떡갈비",
        "feature": "넉넉하고 푸짐한 떡갈비 정식, 현지인 추천 맛집",
        "rating": 4.6,
        "address": "광주 북구 설죽로 200",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%86%A1%EC%A0%95%EB%96%A1%EA%B0%88%EB%B9%84",
    },
    "ENFP": {
        "restaurant": "충장로 김치찌개",
        "feature": "매콤하고 깊은 맛의 김치찌개, 활기찬 분위기",
        "rating": 4.5,
        "address": "광주 동구 충장로 45",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%B6%A9%EC%9E%A5%EB%A1%9C+%EA%B9%80%EC%B9%98%EC%B0%8C%EA%B0%9C",
    },
    "ISTJ": {
        "restaurant": "송정 떡집",
        "feature": "전통 손맛 가득한 떡, 깔끔한 서비스",
        "rating": 4.4,
        "address": "광주 북구 송정로 77",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%86%A1%EC%A0%95+%EB%96%A1%EC%A7%91",
    },
    "ISFP": {
        "restaurant": "광주 다도원 한정식",
        "feature": "아름다운 정원과 전통 한식 코스 요리",
        "rating": 4.7,
        "address": "광주 서구 상무대로 812",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EB%8B%A4%EB%8F%84%EC%9B%90+%ED%95%9C%EC%A0%95%EC%8B%9D",
    },
    "ESFJ": {
        "restaurant": "광주 금남로 김밥",
        "feature": "친절한 서비스와 깔끔한 김밥 맛집",
        "rating": 4.3,
        "address": "광주 동구 금남로 147",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EA%B8%88%EB%82%A8%EB%A1%9C+%EA%B9%80%EB%B0%A5",
    },
    "INTJ": {
        "restaurant": "광주 브런치카페 하루",
        "feature": "조용하고 세련된 분위기의 브런치 카페",
        "rating": 4.6,
        "address": "광주 북구 동문대로 250",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EB%B8%8C%EB%9F%B0%EC%B9%98%EC%B9%B4%ED%8E%98+%ED%95%98%EB%A3%A8",
    },
    "ENTP": {
        "restaurant": "광주 상무지구 퓨전 바",
        "feature": "다양한 칵테일과 퓨전 음식, 활기찬 분위기",
        "rating": 4.4,
        "address": "광주 서구 상무대로 1234",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%83%81%EB%AC%B4%EC%A7%80%EA%B5%AC+%ED%94%84%EC%9C%A0%EC%A0%84+%EB%B0%94",
    },
    "INFJ": {
        "restaurant": "광주 무진동 순대국",
        "feature": "깊고 진한 국물 맛이 일품인 순대국 전문점",
        "rating": 4.7,
        "address": "광주 북구 무진대로 456",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EB%AC%B4%EC%A7%84%EB%8F%99+%EC%88%9C%EB%8C%80%EA%B5%AD",
    },
    "ESTP": {
        "restaurant": "광주 양림동 치킨",
        "feature": "바삭하고 매콤한 치킨, 젊은 층 인기",
        "rating": 4.5,
        "address": "광주 남구 양림로 22",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%96%91%EB%A6%BC%EB%8F%99+%EC%B9%98%ED%82%A8",
    },
    "ISFJ": {
        "restaurant": "광주 광천식당 백반",
        "feature": "정성 가득한 한식 백반, 가족 단위 방문 많음",
        "rating": 4.6,
        "address": "광주 동구 광천로 88",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EA%B4%91%EC%B2%9C%EC%8B%9D%EB%8B%B9",
    },
    "ESFP": {
        "restaurant": "광주 금남로 술집",
        "feature": "다양한 주류와 안주, 활기찬 분위기",
        "rating": 4.3,
        "address": "광주 동구 금남로 150",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EA%B8%88%EB%82%A8%EB%A1%9C+%EC%88%A0%EC%A7%91",
    },
    "INTP": {
        "restaurant": "광주 문학 카페",
        "feature": "조용하고 차분한 분위기의 독서 카페",
        "rating": 4.5,
        "address": "광주 북구 문학로 98",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EB%AC%B8%ED%95%99+%EC%B9%B4%ED%8E%98",
    },
    "ENTJ": {
        "restaurant": "광주 첨단 스테이크 하우스",
        "feature": "고급스럽고 품격있는 스테이크 전문점",
        "rating": 4.7,
        "address": "광주 광산구 첨단중앙로 321",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%B2%A8%EB%8B%A8+%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%81%AC+%ED%95%98%EC%9A%B0%EC%8A%A4",
    },
    "INFP": {
        "restaurant": "무등산 떡갈비",
        "feature": "부드럽고 달콤한 수제 떡갈비, 전통적인 맛",
        "rating": 4.8,
        "address": "광주 동구 무등로 123",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EB%AC%B4%EB%93%B1%EC%82%B0+%EB%96%A1%EA%B0%88%EB%B9%84",
    },
    "ENTP": {
        "restaurant": "상무지구 퓨전 바",
        "feature": "다양한 칵테일과 퓨전 음식, 활기찬 분위기",
        "rating": 4.4,
        "address": "광주 서구 상무대로 1234",
        "map_url": "https://map.kakao.com/?q=%EA%B4%91%EC%A3%BC+%EC%83%81%EB%AC%B4%EC%A7%80%EA%B5%AC+%ED%94%84%EC%9C%A0%EC%A0%84+%EB%B0%94",
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
