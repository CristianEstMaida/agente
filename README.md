# 📄 Agente de Preguntas y Respuestas sobre Documentos

Este proyecto implementa un agente de IA capaz de **leer documentos (PDF/CSV)**, **responder preguntas en lenguaje natural** sobre su contenido y estar disponible públicamente gracias a un **deploy en Oracle Cloud Infrastructure (OCI)**.

---

## 🚀 Arquitectura

```text
                ┌─────────────────────┐
                │   Documento fuente  │
                │ (PDF / CSV / otros) │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   Procesamiento     │
                │ PyPDF / Pandas      │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   Indexación        │
                │ Embeddings + Vector │
                │ Store (FAISS/Chroma)│
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   Agente QA         │
                │ LangChain + LLM     │
                │ (Gemma, ChatGPT,    │
                │ Cohere, etc.)       │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   API REST          │
                │ Flask / FastAPI     │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   OCI Compute       │
                │ (Deploy en la nube) │
                └─────────────────────┘
💡 Ejemplos de preguntas y respuestas
text
Pregunta: ¿Cuál fue el producto más vendido en diciembre de 2015?
Respuesta: El producto más vendido fue "Notebook X", con 1.245 unidades.

Pregunta: ¿Qué lenguajes de programación se usan en el back-end?
Respuesta: Según la documentación, se utilizan Java y .NET.
🛠️ Instrucciones de ejecución local
Clonar el repositorio:

bash
git clone https://github.com/usuario/agente-oci.git
cd agente-oci
Instalar dependencias:

bash
pip install -r requirements.txt
Ejecutar la aplicación:

bash
python src/main.py
La API estará disponible en http://localhost:5000.

☁️ Deploy en OCI
Construir imagen Docker:

bash
docker build -t agente-oci .
docker tag agente-oci <tu-registry-oci>/agente-oci:v1
docker push <tu-registry-oci>/agente-oci:v1
Crear instancia de contenedor en OCI.

Configurar Load Balancer para acceso público.

✅ Comprobación del deploy
Enlace público: [Parece que el resultado no era seguro para mostrar. ¡Cambiemos de enfoque y probemos algo diferente!]

Captura de pantalla: ver /docs/deploy.png

📚 Tecnologías utilizadas
Python

LangChain

PyPDF / Pandas

Modelos LLM: Gemma, ChatGPT, Cohere (configurable)

OCI Compute para despliegue en la nube

📌 Historial de commits sugerido
feat: estructura inicial del proyecto

feat: lector de PDF y CSV

feat: integración con LangChain

feat: agente QA con LLM

feat: API REST con FastAPI

chore: Dockerfile y scripts de deploy

docs: README completo con arquitectura y ejemplos

👨‍💻 Autor
Proyecto desarrollado por Cristian
