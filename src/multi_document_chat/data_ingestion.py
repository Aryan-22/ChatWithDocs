
import uuid
from pathlib import Path
import sys
from langchain_community.document_loaders import PyPDFLoader,Docx2txtLoader,TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import  FAISS
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader
from datetime import datetime,timezone
class DocumentIngestor:
    SUPPORTED_EXTENSIONS = {".pdf",".docx",".txt",".md"}
    def __init__(self,temp_dir:str = "data/multi_document_chat",faiss_dir:str = "faiss_index",session_id:str | None = None):
        try:
            self.log = CustomLogger().get_logger(__name__)
            
            self.temp_dir = Path(temp_dir)
            self.faiss_dir = Path(faiss_dir)
            self.temp_dir.mkdir(parents=True,exist_ok=True)
            self.faiss_dir.mkdir(parents=True,exist_ok=True)


            #session paths
            self.session_id = session_id or f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
            self.session_temp_dir = self.temp_dir / self.session_id
            self.session_faiss_dir = self.faiss_dir / self.session_id
            self.session_temp_dir.mkdir(parents = True,exist_ok=True)
            self.session_faiss_dir.mkdir(parents = True,exist_ok=True)

            self.model_loader = ModelLoader()
            self.log.info("DocumentIngestor initialised.",
                        
                temp_base = str(self.temp_dir),
                faiss_base = str(self.faiss_dir),
                session_id = self.session_id,
                temp_path = str(self.session_temp_dir),
                faiss_path = str(self.session_faiss_dir),)
        
        except Exception as e:
            self.log.error("Failed to initialize DocumentIngestor",error = str(e))
            raise DocumentPortalException("Initialization error in DocumentIngestor",sys)
        

    def ingest_files(self):
        try:
            pass
        except Exception as e:
            self.log.error("Failed to ingest files",error = str(e))
            raise DocumentPortalException("Ingestion error in DocumentIngestor",sys)

    def __create_retriever(self,documents):
        try:
            embeddings = ModelLoader().load_embeddings()
            vectorstore = FAISS.from_documents(documents,embeddings)
            return vectorstore.as_retriever()
        except Exception as e:
            self.log.error("Failed to create retriever",error = str(e))
            raise DocumentPortalException("Retrieval error in DocumentIngestor",sys)
        