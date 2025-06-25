import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="맞춤법 검사기", page_icon="📝")
st.title("📝 한국어 맞춤법 검사기")

text_input = st.text_area(
    "검사할 문장을 입력해 주세요:",
    placeholder="예: 안녕하새요 저는 오늘 학교에 갔읍니다.",
    height=200,
)

def check_spell(text: str) -> str:
    """부산대 맞춤법 검사기를 호출하여 교정된 텍스트 반환"""
    url = "https://speller.cs.pusan.ac.kr/results"
    data = {"text1": text}
    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.text, "html.parser")

    # 교정된 텍스트 가져오기
    corrected_text_elem = soup.select_one(".replace_text")
    if corrected_text_elem:
        return corrected_text_elem.get_text(strip=True)
    return "교정된 결과를 찾을 수 없습니다."

if st.button("검사하기"):
    if not text_input.strip():
        st.warning("문장을 입력해 주세요!")
    else:
        with st.spinner("검사 중..."):
            try:
                corrected_text = check_spell(text_input)
                st.success("✅ 검사 완료!")
                st.subheader("교정된 문장")
                st.write(f"> {corrected_text}")
            except Exception as e:
                st.error(f"맞춤법 검사 중 오류가 발생했습니다: {e}")

st.markdown(
    "---\n"
    "💡 **참고:** 교정된 결과를 꼭 다시 한 번 확인해 주세요. (부산대 검사기 기반)"
)
