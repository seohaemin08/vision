import streamlit as st

st.set_page_config(page_title="할 일 리스트", page_icon="✅")

st.title("✅ 할 일 리스트 앱")

# 세션 상태 초기화
if "todos" not in st.session_state:
    st.session_state.todos = []

# 새 할 일 추가
new_task = st.text_input("할 일 추가하기:")
if st.button("추가"):
    if new_task.strip():  # 공백이 아닌 경우만 추가
        st.session_state.todos.append(new_task.strip())

st.markdown("---")

# 현재 할 일 리스트 표시
st.subheader("📋 현재 할 일")
if len(st.session_state.todos) == 0:
    st.info("할 일이 없습니다. 새 할 일을 추가해보세요!")
else:
    for i, task in enumerate(st.session_state.todos):
        cols = st.columns([5, 1])
        cols[0].write(f"{i+1}. {task}")
        if cols[1].button("삭제", key=f"delete_{i}"):
            del st.session_state.todos[i]
            st.experimental_rerun()

st.markdown("---")
st.caption("💡 페이지를 새로 고치면 리스트가 초기화됩니다. CSV 저장 등 확장 가능!")
