import streamlit as st
from hanspell import spell_checker

st.set_page_config(page_title="맞춤법 검사기", page_icon="📝")

st.title("📝 한국어 맞춤법 검사기")

st.markdown(
    "맞춤법 검사할 문장을 입력해 주세요. 교정된 문장과 교정 정보를 보여드립니다!"
)

# 텍스트 입력
text_input = st.text_area(
    "문장을 입력하세요:",
    placeholder="예: 안녕하새요 저는 오늘 학교에 갔읍니다.",
    height=200,
)

# 검사하기 버튼
if st.button("검사하기"):
    if text_input.strip() == "":
        st.warning("문장을 입력해 주세요!")
    else:
        try:
            result = spell_checker.check(text_input)
            st.success("✅ 검사 완료!")

            # 교정된 문장 출력
            st.subheader("교정된 문장")
            st.write(f"> {result.checked}")

            # 교정 정보 출력
            st.subheader("교정 정보 (원문과 수정된 부분)")
            st.json(result.as_dict())  # JSON 형태 출력

        except Exception as e:
            st.error(f"맞춤법 검사 중 오류 발생: {e}")

# 추가 안내
st.markdown(
    "---\n"
    "💡 **참고:** 교정 엔진은 `py-hanspell`을 이용하고 있습니다. 교정된 결과를 꼭 확인해 주세요."
)


