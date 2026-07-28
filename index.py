# Paso 1: Instalación de librerías
!pip install langchain openai faiss-cpu pdfplumber pandas

# Paso 2: Cargar documentos
# Documento de texto (FAQ, reglamento, políticas)
faq_text = """
Reglamento del Estudiante:
- El acceso a los cursos es personal e intransferible.
- Los certificados se emiten únicamente cuando el estudiante completa el 100% del curso.

Política de Reembolso:
- Los reembolsos pueden solicitarse dentro de los primeros 7 días posteriores a la inscripción.
- No se realizan reembolsos una vez emitido el certificado.

FAQ:
- ¿Cómo obtengo mi certificado? Debes completar todas las lecciones y aprobar las evaluaciones finales.
- ¿Qué pasa si me atraso en el pago? Tu acceso al curso quedará suspendido hasta regularizar la situación.
"""

# CSV de estudiantes y cursos
import pandas as pd
from io import StringIO

csv_data = """id_estudiante,nombre,curso,fecha_inscripcion,estado,calificacion_final
1,Ana López,Python Básico,2025-03-12,Completado,8.5
2,Juan Pérez,Java Intermedio,2025-04-05,En curso,
3,María Gómez,React Avanzado,2025-05-20,Completado,9.0
4,Carlos Díaz,Python Básico,2025-06-01,Completado,7.8
5,Lucía Fernández,Data Science,2025-06-15,En curso,
6,Martín Rodríguez,Java Intermedio,2025-07-02,Completado,8.2
7,Sofía Martínez,Data Science,2025-07-10,Completado,9.3
8,Diego Torres,React Avanzado,2025-07-18,En curso,
9,Valentina Castro,Python Básico,2025-07-20,Completado,8.7
10,Agustín Morales,Data Science,2025-07-25,Completado,7.9
"""

df = pd.read_csv(StringIO(csv_data))
print(df.head())

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Dividir texto en fragmentos
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_text(faq_text)

# Crear base vectorial
embeddings = OpenAIEmbeddings()
db = FAISS.from_texts(docs, embeddings)

# Crear agente QA
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=db.as_retriever()
)

# Ejemplo de pregunta textual
respuesta_textual = qa.run("¿Cómo obtengo mi certificado?")
print("Respuesta textual:", respuesta_textual)

# Curso con más inscriptos
curso_popular = df['curso'].value_counts().idxmax()
print("Curso con más inscriptos:", curso_popular)

# Promedio de calificaciones en Python Básico
promedio_python = df[df['curso'] == "Python Básico"]['calificacion_final'].mean()
print("Promedio en Python Básico:", promedio_python)

# Mejor calificación en React Avanzado
mejor_react = df[df['curso'] == "React Avanzado"]['calificacion_final'].max()
print("Mejor calificación en React Avanzado:", mejor_react)

#respuesta = qa.run("¿Cuál fue el producto más vendido en diciembre de 2015?")
#print(respuesta)
