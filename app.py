
import streamlit as st
import ollama
st.title("Friendly AI Bot")
st.write("Ask me anything !")
question = st.text_input("Enter your question here:")
if st.button("Ask AI"):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a friendly assistant. Explain things in simple language.Be helpful and encouraging."""},
            {"role": "user", "content": question}   
        ]
    )
    answer = response["message"]["content"]
    st.write(" AI Response")
    st.write(answer)

st.markdown("""
<style>

/* Background */
body {
    background-color: #0f172a;
}

/* Main container */
.stApp {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
}

/* Title styling */
h1 {
    text-align: center;
    color: #38bdf8;
    font-size: 40px;
}

/* Input box */
.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
    border: 2px solid #38bdf8;
    padding: 10px;
}

/* Button */
.stButton > button {
    background-color: #38bdf8;
    color: black;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

/* Button hover */
.stButton > button:hover {
    background-color: #0ea5e9;
    color: white;
}

/* AI Response box */
.css-1cpxqw2 {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #38bdf8;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)
