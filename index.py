import pandas as pd

df = pd.read_csv("ventas.csv")
print(df.head())

import pdfplumber

with pdfplumber.open("politicas.pdf") as pdf:
    texto = ""
    for pagina in pdf.pages:
        texto += pagina.extract_text()
print(texto[:500])

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Dividir texto en chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = splitter.split_text(texto)

# Crear base vectorial
embeddings = OpenAIEmbeddings()
db = FAISS.from_texts(docs, embeddings)

# Crear agente QA
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=db.as_retriever()
)

respuesta = qa.run("¿Cuál fue el producto más vendido en diciembre de 2015?")
print(respuesta)
