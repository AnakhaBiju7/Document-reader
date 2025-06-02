
# Document Question Answering App

A **Streamlit-based web application** that enables users to upload documents (PDF, DOCX, or TXT) and ask questions about their content, delivering accurate, context-aware answers using **LangChain**, **FAISS**, and **OpenAI's GPT-3.5** model. The app processes documents into embeddings, stores them in a vector database, and uses a retrieval-augmented generation (RAG) pipeline to provide answers with source citations for transparency and verifiability.

## How It Works

1. **User Input**:
   - Users provide an **OpenAI API key** via a secure text input to enable embeddings and language model access.
   - A file uploader accepts documents in **PDF, DOCX, or TXT** formats.

2. **Document Processing**:
   - Uploaded documents are saved temporarily using Python's `tempfile` module.
   - The `UnstructuredFileLoader` from LangChain extracts raw content from the document, regardless of its format.

3. **Text Splitting and Embedding**:
   - Documents are split into chunks (1000 characters, 200-character overlap) using `RecursiveCharacterTextSplitter` for manageable segments.
   - **OpenAIEmbeddings** converts chunks into vector representations, stored in a **FAISS** vector database for efficient retrieval.

4. **Vector Storage and Retrieval**:
   - The FAISS vector store, cached with Streamlit’s `@st.cache_resource`, enables fast similarity-based retrieval.
   - The retriever fetches the top **3 relevant chunks** for each user query.

5. **Question Answering**:
   - User questions are processed by the `RetrievalQA` chain, combining retrieved chunks with **GPT-3.5** (`ChatOpenAI`, temperature=0) for concise, accurate answers.
   - Answers include **source citations**, displayed in an expandable "Sources" section for transparency.

6. **User Interface**:
   - The **Streamlit interface** features a clean, wide-layout design with a title, API key input, file uploader, question input, and answer display.
   - Success messages confirm document processing, and info prompts guide users to provide required inputs.

## Key Features
- **Supported Formats**: Processes PDF, DOCX, and TXT files using `UnstructuredFileLoader`.
- **Efficient Retrieval**: FAISS ensures fast and accurate document chunk retrieval.
- **Transparent Responses**: Answers include source excerpts for verification.
- **Cached Processing**: Document processing is cached for improved performance.
- **Secure API Handling**: OpenAI API key is securely input and set as an environment variable.

## Technical Stack
- **Streamlit**: User-friendly web interface.
- **LangChain**: Document loading, splitting, embedding, and RAG pipeline.
- **FAISS**: Efficient vector storage and similarity search.
- **OpenAI**: Embeddings and GPT-3.5 for question answering.
- **Python**: Core programming language.

## Use Cases
- **Research and Study**: Extract answers from academic papers or reports.
- **Professional Use**: Query contracts, manuals, or technical documents.
- **Personal Knowledge Management**: Retrieve insights from personal documents.

This app is ideal for users seeking efficient interaction with document content, leveraging advanced AI and vector search for precise, source-backed answers.
