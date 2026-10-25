```text
ielts-scoring-system/
├── .github/
│   └── workflows/
│       └── pytest.yml           # CI/CD pipeline for automated testing
├── api/                         # FastAPI backend (Model Serving)
│   ├── routes/                  # API endpoints (e.g., /score, /grammar)
│   ├── schemas/                 # Pydantic models for request/response validation
│   └── main.py                  # FastAPI application entry point
├── ingest/                      # Data pipeline and preparation
│   ├── crawlers/                # Scripts to fetch data (if applicable)
│   ├── preprocessing/           # Data cleaning, text normalization
│   └── eda.ipynb                # Exploratory Data Analysis notebooks
├── rag/                         # Retrieval-Augmented Generation module
│   ├── indexer.py               # Code to create and update the vector database (e.g., Qdrant/FAISS)
│   ├── retriever.py             # Logic to query the vector database
│   └── prompts.py               # Prompt templates for the LLM
├── scoring/                     # Machine Learning / Model training
│   ├── models/                  # PyTorch/Transformers model definitions
│   ├── train.py                 # Training script (DeBERTa-v3)
│   ├── evaluate.py              # Evaluation script (QWK, MAE)
│   └── utils.py                 # Helper functions (e.g., metric calculations)
├── web/                         # Frontend interface (Streamlit/React)
│   └── app.py                   # Streamlit app or frontend source
├── tests/                       # Pytest directory
│   ├── api/                     # Tests for FastAPI endpoints
│   ├── ingest/                  # Tests for data preprocessing
│   ├── rag/                     # Tests for retrieval logic
│   ├── scoring/                 # Tests for metric calculation and model loading
│   └── conftest.py              # Shared fixtures for Pytest
├── .gitignore                   # Ignore __pycache__, .env, venv, data/, weights/
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies (pytest, black, flake8)
└── README.md                    # Project documentation and setup guide
```