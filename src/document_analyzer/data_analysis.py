import os
import sys
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from prompt.prompt_library import *
class DocumentAnalyzer:
    """
    Analyzes documents using a pre-trained model
    Automatically logs all  actions and supports session-based organisations   
    """
    def __init__(self):
        
        self.log = CustomLogger().get_logger(__name__)
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_llm()

            #Prepare parsers
            self.parser = JsonOutputParser(pydantic_object=MetaData)
            self.fixing_parser = OutputFixingParser.from_llm(parser = self.parser,llm = self.llm)
            self.prompt = document_analysis_prompt
            self.log.info("Document Analyser initialised successfully")


        except Exception as e:
            self.log.error(f"Error initialising Document Analyzer:{e}")
            raise DocumentPortalException("Error in DocumentAnalyzer Initialisation",sys)
        


    def analyze_metadata():
        pass
