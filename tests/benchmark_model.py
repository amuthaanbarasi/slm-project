import time
from app.llm_engine import generate_answer

questions = [
    "What is Python?",
    "What is Machine Learning?",
    "What is an API?"
]

context = "Python is a high-level programming language."

total_time = 0

for question in questions:
    start_time = time.perf_counter()

    answer = generate_answer(question, context)

    end_time = time.perf_counter()

    response_time = end_time - start_time
    total_time += response_time

    print(f"Question: {question}")
    print(f"Answer: {answer}")
    print(f"Response Time: {response_time:.2f} seconds")
    print("-" * 40)

average_time = total_time / len(questions)

print(f"Average Response Time: {average_time:.2f} seconds")