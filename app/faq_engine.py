import json
from pathlib import Path
from difflib import get_close_matches

DATA_PATH = Path(__file__).parent.parent / "data" / "faqs.json"

with open(DATA_PATH, "r", encoding="utf-8") as file:
    faqs = json.load(file)


def find_answer(user_question):
    questions = [faq["question"] for faq in faqs]

    matches = get_close_matches(
        user_question.lower(),
        [question.lower() for question in questions],
        n=1,
        cutoff=0.6
    )

    if matches:
        for faq in faqs:
            if faq["question"].lower() == matches[0]:
                return faq["answer"]

    return "Sorry, I could not find an answer to your question."