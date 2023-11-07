import langchain
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models.openai import ChatOpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.retrievers.web_research import WebResearchRetriever
import chromadb
import sys
import config_key
from langchain.chains import create_extraction_chain
from langchain.chains import RetrievalQAWithSourcesChain
import logging

# Load environmental variables from config_key.py if not set
required_keys = ['OPENAI_API_KEY', 'GOOGLE_API_KEY', 'GOOGLE_CSE_ID']
for key in required_keys:
    if not key in os.environ:
        value = getattr(config_key, key, None)
        if value is not None:
            os.environ[key] = value

# Vectorstore
vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(), persist_directory="./chroma_db_oai"
)

# LLM
llm = ChatOpenAI(temperature=0, model = "gpt-4")

# Search
search = GoogleSearchAPIWrapper()

# Initialize
web_research_retriever = WebResearchRetriever.from_llm(
    vectorstore=vectorstore, llm=llm, search=search, num_search_results = 6)


# Run

logging.basicConfig()
logging.getLogger("langchain.retrievers.web_research").setLevel(logging.INFO)

user_input = " I want information on marketing intelligence, companies working in this field  like G2.com."
qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm, retriever=web_research_retriever
)
result = qa_chain({"question": user_input})
#print(result)

schema = {
    "properties": {
        "Information" : {"type": "string"},
        "companies" : {"type": "string"}

        
    },
    "required": ["Information", "companies" ],
}
def extract(content: str, schema: dict):
    input_data = {"input": content}  # Wrap the content in a dictionary with the 'input' key
    return create_extraction_chain(schema=schema, llm=llm).run(input_data)

print(extract(result,schema))