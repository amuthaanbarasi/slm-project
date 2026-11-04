import json
from pathlib import Path
from app.faq_engine import find_answer

file_path = Path(__file__).parent / "evaluation_questions.json"

with open(file_path, "r", encoding="utf-8") as file:
    questions = json.load(file)

correct = 0
total = len(questions)

for item in questions:
    question = item["question"]
    expected_topic = item["expected_topic"]

    answer = find_answer(question)

    if expected_topic == "unknown":
        passed = answer.startswith("Sorry")
    else:
        passed = expected_topic.lower() in answer.lower()

    if passed:
        correct += 1
        result = "PASS"
    else:
        result = "FAIL"

    print(f"Question: {question}")
    print(f"Expected topic: {expected_topic}")
    print(f"Result: {result}")
    print("-" * 40)

accuracy = (correct / total) * 100

print(f"Correct answers: {correct}/{total}")
print(f"Evaluation accuracy: {accuracy:.2f}%")