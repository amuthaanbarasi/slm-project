# SLM Model Comparison

## 1. Project Use Case

Project Name: FAQ Assistant

The goal is to build an AI-powered FAQ Assistant
using a Small Language Model (SLM). It will answer
user questions based on a specific set of information.

## 2. Models Researched

1. SmolLM2 1.7B Instruct - Hugging Face
2. Qwen2.5 1.5B Instruct - Qwen
3. Gemma 3 1B IT - Google

## 3. Model Comparison

| Feature | SmolLM2 1.7B | Qwen2.5 1.5B | Gemma 3 1B |
|---|---|---|---|
| Developer | Hugging Face | Qwen | Google |
| Parameters | 1.7B | 1.54B | 1B |
| Context | 8K | 32K | 32K |
| License | Apache 2.0 | Apache 2.0 | Gemma Terms |
| Main use | Text generation | Question answering | Text generation |

## 4. Advantages and Limitations

### SmolLM2
Advantages:
- Lightweight model.
- Suitable for simple tasks.

Limitations:
- May struggle with complex questions.

### Qwen2.5
Advantages:
- Good instruction following.
- Suitable for question answering.
- Apache 2.0 license.

Limitations:
- Requires sufficient RAM.
- May generate incorrect answers.

### Gemma 3
Advantages:
- Compact model.
- Supports text generation and summarization.

Limitations:
- Requires checking its usage terms.
- May struggle with complex tasks.

## 5. Selected Model

Qwen2.5 1.5B Instruct

## 6. Reason for Selection

Qwen2.5 1.5B Instruct is selected because
it is a compact instruction-tuned model.
It is suitable for experimenting with a
FAQ Assistant and can be tested locally
using a quantized version.

## 7. Official Model Links

- SmolLM2:
  https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct

- Qwen2.5:
  https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct

- Gemma 3:
  https://ai.google.dev/gemma/docs/core/model_card_3