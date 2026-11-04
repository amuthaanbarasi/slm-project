# SLM FAQ Assistant - Optimization Report

## 1. Model Details

- Model: Qwen2.5 1.5B Instruct
- Runtime: Ollama
- Architecture: Qwen2
- Parameters: 1.5 Billion
- Context Length: 32,768 tokens
- Quantization: Q4_K_M
- License: Apache 2.0

## 2. Optimization Techniques

### Model Quantization

The Qwen2.5 1.5B model is available locally in Q4_K_M quantized format.

This reduces memory requirements and supports local execution.

### FAQ Retrieval Improvement

The FAQ retrieval threshold was increased from 0.4 to 0.6.

This helped reduce incorrect matches for unrelated questions.

### Local Model Execution

Ollama is used to execute the model locally without depending on a cloud-based inference API.

## 3. Evaluation

- Evaluation questions: 5
- Correct retrievals: 5
- Retrieval accuracy: 100%

## 4. Conclusion

The project uses a compact, quantized SLM for local FAQ assistance.

The retrieval threshold improvement helped reject unrelated questions in the evaluation dataset.

Further performance testing is required to measure response time, memory usage, and answer quality.
## 5. Response Time Benchmark

Three questions were used to measure Qwen2.5 response time.

| Question | Response Time |
|---|---:|
| What is Python? | 5.39 seconds |
| What is Machine Learning? | 1.69 seconds |
| What is an API? | 2.46 seconds |

Average Response Time: 3.18 seconds

The first response took longer than the subsequent responses.
This may be due to initial model loading.

These results represent an initial local benchmark.
## 6. Prompt Engineering and Adaptation

The original prompt was improved by adding a structured system prompt.

The improved prompt includes:
- Clear FAQ assistant role.
- Instructions to use only the provided FAQ information.
- Rules to avoid generating unsupported facts.
- Simple English responses.
- Concise and relevant answers.

The updated prompt was tested using Qwen2.5 1.5B Instruct.

Result:
The model generated a relevant and clear answer for the Python question.

This is inference-time prompt adaptation. Model weights were not modified or fine-tuned.