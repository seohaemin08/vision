import streamlit as st
import random

st.set_page_config(page_title="맞춤 메뉴 추천 앱", page_icon="🍽")

st.title("🍽 맞춤형 메뉴 추천 앱")
st.write(
    "계절, 날씨, 기분에 맞춰 메뉴를 추천받아요! 정하기 어려우면 랜덤 추천까지 😄"
)

# 옵션들 정의
seasons = ["봄", "여름", "가을", "겨울"]
weather_types = ["맑음", "비", "흐림", "더움", "추움"]
moods = ["행복", "우울", "피곤", "스트레스"]

# 메뉴 사전 정의
menu_dict = {
    "봄": ["비빔밥", "샐러드", "쑥국"],
    "여름": ["냉면", "콩국수", "빙수"],
    "가을": ["된장찌개", "칼국수", "고등어구이"],
    "겨울": ["순두부찌개", "짬뽕", "설렁탕"],
    "맑음": ["샌드위치", "샐러드", "스테이크"],
    "비": ["파전", "칼국수", "우동"],
    "흐림": ["짬뽕", "수제비", "김치찌개"],
    "더움": ["메밀소바", "냉면", "빙수"],
    "추움": ["곰탕", "순대국밥", "육개장"],
    "행복": ["치킨", "피자", "스파게티"],
    "우울": ["초콜릿케이크", "아이스크림", "떡볶이"],
    "피곤": ["삼계탕", "낙지볶음", "곰탕"],
    "스트레스": ["매운닭발", "불족발", "마라탕"],
}

# 사용자 선택
season = st.selectbox("계절을 선택해 주세요:", ["(선택 안 함)"] + seasons)
weather = st.selectbox("날씨를 선택해 주세요:", ["(선택 안 함)"] + weather_types)
mood = st.selectbox("기분을 선택해 주세요:", ["(선택 안 함)"] + moods)

# 메뉴 추천하기
if st.button("메뉴 추천"):
    candidates = []

    if season != "(선택 안 함)":
        candidates += menu_dict.get(season, [])
    if weather != "(선택 안 함)":
        candidates += menu_dict.get(weather, [])
    if mood != "(선택 안 함)":
        candidates += menu_dict.get(mood, [])

    if not candidates:
        # 아무 조건 없음 -> 전체 메뉴 리스트 중 랜덤
        all_menus = sum(menu_dict.values(), [])  # 모든 리스트 합치기
        recommended = random.choice(all_menus)
    else:
        recommended = random.choice(candidates)

    st.success(f"🎉 오늘의 추천 메뉴: **{recommended}**")

st.markdown(
    "---\n"
    "💡 조건을 선택하지 않으면 무작위 메뉴를 추천해 드립니다."
)

