
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",
                          task="text-generation"
                          )
model = ChatHuggingFace(llm=llm)



def translate(text,source_lang,target_lang):
    prompt=f"""
translate the following text from {source_lang} to {target_lang}:

{text}

don't add extra text , only translate

"""
    res=model.invoke(prompt)
    return res.text if res else "Translation failed"
import streamlit as st
st.title("Translation Engine")
text=st.text_area("Enter text to translate")
source_lang=st.selectbox("select source language",["English","hindi","French","Telgu","tamil","Japanies","urdu"])
target_lang=st.selectbox("select target language",["English","hindi","French","Telgu","tamil","Japanies","urdu"])
if st.button("Translate"):
    if text.strip():
        r=translate(text,source_lang,target_lang)
        st.write(r)
    else:
        st.warning("Translation failed")
