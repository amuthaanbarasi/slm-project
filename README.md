
# SLM General FAQ Assistant

## Project Overview

The SLM General FAQ Assistant is a question-answering application powered by Qwen2.5 1.5B Instruct.

It uses FAQ retrieval and a Small Language Model (SLM) to provide simple and relevant answers to general questions.

The application runs locally using Ollama and provides an API through FastAPI.

## Technologies Used

- Python
- Qwen2.5 1.5B Instruct
- Ollama
- FastAPI
- Pydantic
- Pytest
- JSON

## Project Structure

```text
slm-project/
│
├── app/
│   ├── faq_engine.py
│   ├── llm_engine.py
│   └── main.py
│
├── data/
│   └── faqs.json
│
├── tests/
│   ├── benchmark_model.py
│   ├── evaluate_model.py
│   ├── evaluation_questions.json
│   ├── evaluation_results.md
│   ├── optimization_report.md
│   └── test_faq_engine.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── SLM_Model_Comparison.md
```

## Features

- General FAQ question answering.
- FAQ retrieval using fuzzy string matching.
- Qwen2.5 1.5B model integration.
- Prompt engineering for improved responses.
- Unknown question handling.
- REST API using FastAPI.
- Automated testing and evaluation.
- Local model execution using Ollama.

## Model Information

- Model: Qwen2.5 1.5B Instruct
- Parameters: 1.5 Billion
- Context Length: 32K
- Quantization: Q4_K_M
- Runtime: Ollama
- License: Apache 2.0

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/amuthaanbarasi/slm-project.git
cd slm-project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Download the model

Install Ollama and run:

```bash
ollama pull qwen2.5:1.5b
```

### 6. Start the application

```bash
python -m uvicorn app.main:app --reload
```

## API Usage

### Home Endpoint

```http
GET /
```

### Ask Endpoint

```http
POST /ask
```

Example request:

```json
{
    "question": "What is Python?"
}
```

Example response:

```json
{
    "question": "What is Python?",
    "answer": "Python is a high-level programming language."
}
```

## API Documentation

After starting the application, open:

http://127.0.0.1:8000/docs

## Testing

Run automated tests:

```bash
python -m pytest tests/test_faq_engine.py -v
```

Run evaluation:

```bash
python -m tests.evaluate_model
```

Run response-time benchmark:

```bash
python -m tests.benchmark_model
```

## Evaluation Results

- Evaluation questions: 5
- Correct retrievals: 5
- Retrieval accuracy: 100%
- Average response time in initial benchmark: 3.18 seconds

Note: Evaluation accuracy is based on a small five-question dataset. Benchmark timing is based on three local generation requests.

## Documentation

- SLM_Model_Comparison.md
- tests/evaluation_results.md
- tests/optimization_report.md

## Future Improvements

- Expand the FAQ dataset.
- Improve semantic question retrieval.
- Evaluate answer quality with a larger dataset.
- Explore fine-tuning or parameter-efficient adaptation.
- Improve response speed.

## Author

Anbarasi Kathirvel
