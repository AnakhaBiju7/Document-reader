import streamlit as st
from langchain_community.document_loaders import PyPDFLoader  # Or UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import tempfile
import os

# UI
st.title("PDF-Based RAG App with OpenAI")

# API Key Input
st.sidebar.title("🔐 OpenAI API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar.")
    st.stop()

# File Upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        temp_file_path = tmp.name

    try:
        with st.spinner("Processing the PDF..."):
            loader = PyPDFLoader(temp_file_path)  # Or UnstructuredPDFLoader
            documents = loader.load()

            if not documents:
                st.warning("No content found in the PDF.")
                st.stop()

            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            docs = text_splitter.split_documents(documents)

            embeddings = OpenAIEmbeddings(openai_api_key=api_key)
            db = FAISS.from_documents(docs, embeddings)

            retriever = db.as_retriever()
            llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)
            rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        query = st.text_input("Ask a question about the PDF content:")

        if query:
            with st.spinner("Generating answer..."):
                result = rag_chain.run(query)
                st.markdown("### 🧠 Answer")
                st.write(result)

    finally:
        os.remove(temp_file_path)

