# ChatWithDocs

## Description

This project provides a Python-based Document Portal API built with FastAPI, designed to facilitate various operations on documents, including analysis, comparison, and conversational AI (Retrieval Augmented Generation). It supports PDF documents and offers a Streamlit-based user interface for interaction.

## Features

- **Document Analysis**: Analyze uploaded PDF documents to extract key information.
- **Document Comparison**: Compare two PDF documents to identify differences and similarities.
- **Multi Document Chat**: Chat with one or more than one document at once.
- **Conversational AI (RAG)**: Ingest documents to build a FAISS index and enable conversational queries using Retrieval Augmented Generation.
- **FastAPI Backend**: A robust and scalable API built with FastAPI.
- **PDF Handling**: Efficiently processes and extracts text from PDF documents using PyMu-PDF.
- **Vector Store**: Utilizes FAISS for efficient similarity search and retrieval of document chunks.

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://aryan-22/ChatWithDocs.git
    cd document_portal_project
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add necessary environment variables. For example:
    ```
    FAISS_BASE=faiss_index
    UPLOAD_BASE=data
    # Add any API keys for language models (e.g., GROQ_API_KEY, GOOGLE_API_KEY) if required by your setup
    ```

## Usage

### Running the FastAPI Application

To start the FastAPI server:

```bash
python -m uvicorn main_archive:app --host 0.0.0.0 --port 8000 --reload
```

The API documentation will be available at `http://localhost:8000/docs`.

## API Endpoints

The following are the main API endpoints provided by the application:

-   **`/health` (GET)**: Checks the health status of the API.
    -   Returns: `{"status": "ok", "service": "document-portal"}`

-   **`/analyze` (POST)**: Analyzes an uploaded PDF document.
    -   **Input**: `file` (UploadFile) - The PDF document to analyze.
    -   **Returns**: JSON response with analysis results.

-   **`/compare` (POST)**
```python
    async def compare_documents(reference: UploadFile = File(...), actual: UploadFile = File(...)) -> Any:
```
    -   Compares two uploaded PDF documents.
    -   **Input**: `reference` (UploadFile), `actual` (UploadFile) - The two PDF documents to compare.
    -   **Returns**: JSON response with comparison results.

-   **`/chat/index` (POST)**
```python
    async def chat_build_index(
        files: List[UploadFile] = File(...),
        session_id: Optional[str] = Form(None),
        use_session_dirs: bool = Form(True),
        chunk_size: int = Form(1000),
        chunk_overlap: int = Form(200),
        k: int = Form(5),
    ) -> Any:
```
    -   Ingests documents to build a FAISS index for conversational AI.
    -   **Input**: `files` (List[UploadFile]), `session_id` (Optional[str]), `use_session_dirs` (bool), `chunk_size` (int), `chunk_overlap` (int), `k` (int)
    -   **Returns**: JSON response with session details.

-   **`/chat/query` (POST)**
```python
    async def chat_query(
        question: str = Form(...),
        session_id: Optional[str] = Form(None),
        use_session_dirs: bool = Form(True),
        k: int = Form(5),
    ) -> Any:
```
    -   Queries the FAISS index for conversational AI.
    
    -   **Input**: `question` (str), `session_id` (Optional[str]), `use_session_dirs` (bool), `k` (int)
    -   **Returns**: JSON response with the AI's answer.

## Technologies Used

-   **Backend**: FastAPI
-   **Frontend**: Html,CSS
-   **Language Models**: LangChain, LangChain Community, LangChain Core, LangChain Groq, LangChain Google GenAI
-   **Vector Database**: FAISS
-   **Document Processing**: PyMuPDF, docx2txt
-   **Environment Management**: python-dotenv
-   **Logging**: structlog

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.


