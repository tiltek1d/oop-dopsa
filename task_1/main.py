import random

from core import Question
from questions import questions_list


def ask_random_questions(
        questions: list[Question],
        num_questions: int = 5,
) -> int:
    random_questions = random.sample(questions, num_questions)
    score = 0
    for i, question in enumerate(random_questions):
        print(f"Вопрос {i + 1}: {question.get_question()}")
        for idx, ans in enumerate(question.get_answers(), 1):
            print(f"{idx}. {ans}")
        answer = int(input("Ваш ответ: "))
        if question.check_answer(answer):
            score += 1
    return score


def calculate_result(score: int):
    match score:
        case 5:
            return "Отлично"
        case 4:
            return "Хорошо"
        case 3:
            return "Удовлетворительно"
        case _:
            return "Неудовлетворительно"


def main():
    students = 3
    for student in range(1, students + 1):
        print(f"\nСтудент {student} начинает отвечать на вопросы:")
        score = ask_random_questions(questions_list)
        result = calculate_result(score)
        print(f"Студент {student} набрал {score} баллов. Результат: {result}")


if __name__ == '__main__':
    main()
