from app.faq_engine import find_answer


def test_python_question():
    answer = find_answer("What is Python?")
    assert "programming language" in answer.lower()


def test_machine_learning_question():
    answer = find_answer("What is Machine Learning?")
    assert "machine learning" in answer.lower()


def test_unknown_question():
    answer = find_answer("Who is the president of India?")
    assert "sorry" in answer.lower()