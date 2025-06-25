import streamlit as st
import random
import time

st.set_page_config(page_title="맞춤 메뉴 추천 앱 + 룰렛", page_icon="🎡")

st.title("🎡 룰렛으로 돌리는 맞춤 메뉴 추천 앱")
st.write("계절, 날씨, 기분에 맞는 메뉴를 추천하고, 랜덤 추천은 룰렛처럼 돌려 보여드려요!")

# 옵션들
seasons = ["봄", "여름", "가을", "겨울"]
weather_types = ["맑음", "비", "흐림", "더움", "추움"]
moods = ["행복", "우울", "피곤", "스트레스"]

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

# 선택 UI
season = st.selectbox("계절을 선택해 주세요:", ["(선택 안 함)"] + seasons)
weather = st.selectbox("날씨를 선택해 주세요:", ["(선택 안 함)"] + weather_types)
mood = st.selectbox("기분을 선택해 주세요:", ["(선택 안 함)"] + moods)

def roulette_spin(candidates, spins=20, delay=0.1):
    placeholder = st.empty()
    for _ in range(spins):
        choice = random.choice(candidates)
        placeholder.markdown(f"### 🎲 룰렛 중... **{choice}**")
        time.sleep(delay)
    placeholder.markdown(f"### 🎉 최종 추천 메뉴: **{choice}**")
    return choice

if st.button("메뉴 추천"):
    candidates = []
    if season != "(선택 안 함)":
        candidates += menu_dict.get(season, [])
    if weather != "(선택 안 함)":
        candidates += menu_dict.get(weather, [])
    if mood != "(선택 안 함)":
        candidates += menu_dict.get(mood, [])

    if not candidates:
        # 전체 메뉴 중 랜덤 선택
        candidates = sum(menu_dict.values(), [])

    roulette_spin(candidates)
    
st.markdown(
    "---\n"
    "💡 조건을 선택하지 않으면 전체 메뉴에서 랜덤으로 룰렛이 돌아갑니다."
)
