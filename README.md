
# Document Question Answering App

This Streamlit application enables users to upload a PDF file, process its content using a Retrieval-Augmented Generation (RAG) pipeline with OpenAI's embeddings and language model, and ask questions about the document. It leverages FAISS for efficient document retrieval and provides answers based on the PDF's content.

Below is a detailed breakdown of its functionality and components:

## Key Features
- **PDF Upload**: Users can upload a PDF file through a file uploader widget in the Streamlit interface, restricted to `.pdf` file types.
- **OpenAI API Integration**: The application requires an **OpenAI API key**, which users input via a secure sidebar text field to authenticate API calls for embeddings and language model queries.
- **PDF Processing**:
  - The uploaded PDF is temporarily saved to the server using Python's `tempfile` module to handle file processing.
  - The content is extracted using `PyPDFLoader` from the **LangChain Community** library (with an option to use `UnstructuredPDFLoader` for more complex PDFs).
- **Text Splitting**:
  - The extracted text is segmented into manageable chunks using `CharacterTextSplitter` with a chunk size of 1,000 characters and an overlap of 100 characters to ensure context continuity.
- **Vector Store Creation**:
  - The text chunks are converted into embeddings using **OpenAIEmbeddings**, which generates vector representations of the text.
  - These embeddings are stored in a **FAISS** vector store, enabling efficient similarity-based retrieval of relevant document chunks.
- **RAG Pipeline**:
  - A **RetrievalQA** chain from LangChain is used, combining a **ChatOpenAI** model (specifically `gpt-3.5-turbo`) with the FAISS retriever to answer user queries.
  - The pipeline retrieves the most relevant document chunks based on the user's question and generates a coherent response using the language model.
- **User Interaction**:
  - Users can input a question about the PDF content via a text input field.
  - The application displays a loading spinner during PDF processing and answer generation, improving user experience.
  - The generated answer is presented in a markdown-formatted section for clarity.
- **Error Handling and Cleanup**:
  - The app checks for a valid OpenAI API key and displays a warning if none is provided, halting execution until resolved.
  - It verifies that the PDF contains extractable content, stopping with a warning if the document is empty.
  - The temporary PDF file is deleted after processing to ensure efficient resource management.

## Workflow
1. **API Key Input**: The user enters their OpenAI API key in the sidebar.
2. **PDF Upload**: The user uploads a PDF file, which is temporarily saved.
3. **Document Processing**: The PDF is loaded, split into chunks, and embedded into a FAISS vector store.
4. **Query Handling**: The user submits a question, and the RAG pipeline retrieves relevant document chunks and generates an answer using the OpenAI model.
5. **Result Display**: The answer is displayed in the Streamlit interface, with loading indicators for a smooth user experience.
6. **Cleanup**: The temporary file is removed to free up server resources.

## Dependencies
- **Streamlit**: For building the interactive web interface.
- **LangChain**: Provides tools for document loading (`PyPDFLoader`), text splitting (`CharacterTextSplitter`), embeddings (`OpenAIEmbeddings`), vector storage (`FAISS`), and the RAG pipeline (`RetrievalQA`).
- **OpenAI**: Supplies the language model (`ChatOpenAI`) and embeddings for text processing.
- **tempfile** and **os**: For handling temporary file storage and cleanup.

## Usage Notes
- The application assumes the user has a valid OpenAI API key and sufficient quota to process embeddings and queries.
- The `gpt-3.5-turbo` model is used by default, but this can be modified to other compatible OpenAI models if needed.
- The chunk size and overlap parameters in `CharacterTextSplitter` can be adjusted for different document types or performance requirements.
- For more complex PDFs (e.g., those with images or tables), switching to `UnstructuredPDFLoader` may improve content extraction.

This application provides a simple yet powerful way to interact with PDF content using advanced AI capabilities, making it suitable for tasks like document analysis, research, or knowledge extraction.
