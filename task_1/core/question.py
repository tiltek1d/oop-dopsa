from dataclasses import dataclass


@dataclass
class Question:
    question: str

    _answer1: str
    _answer2: str
    _answer3: str
    _answer4: str

    correct_answer: int
    git
    remote
    set - url
    origin
    https: // your_username: your_personal_access_token @ github.com / your_username / your_repo.git
    def __post_init__(self):
        self.answers = [self._answer1, self._answer2, self._answer3, self._answer4]

    def get_question(self) -> str:
        return self.question

    def get_answers(self) -> list[str]:
        return self.answers

    def check_answer(self, answer: int) -> bool:
        return self.correct_answer == answer
