import streamlit as st
from openai import OpenAI

def get_answer(api_key: str, user_question: str) -> str:
    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-4o",
            input=user_question
        )
        return response.output_text
    except Exception as e:
        return f"⚠️ 오류 발생: {str(e)}"

st.header("❓ 무엇이든 물어보세요")

api_key = st.text_input("🔑 OPENAI API KEY를 입력하세요.", type="password")
question = st.text_input("💬 질문을 입력하세요.")

if st.button("✅ 답변 확인"):

    if not api_key or not question:
        st.warning("API 키와 질문을 모두 입력해주세요.")
        
    else:
        with st.spinner("답변을 생성 중입니다..."):
            answer = get_answer(api_key, question)
            st.markdown(answer)