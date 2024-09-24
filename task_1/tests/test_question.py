import unittest

from core.question import Question


class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.question = Question(
            question="What is the capital of France?",
            _answer1="Berlin",
            _answer2="Madrid",
            _answer3="Paris",
            _answer4="Rome",
            correct_answer=3
        )

    def test_get_question(self):
        self.assertEqual(self.question.get_question(), "What is the capital of France?")

    def test_get_answers(self):
        expected_answers = ["Berlin", "Madrid", "Paris", "Rome"]
        self.assertEqual(self.question.get_answers(), expected_answers)

    def test_check_answer_correct(self):
        self.assertTrue(self.question.check_answer(3))

    def test_check_answer_incorrect(self):
        self.assertFalse(self.question.check_answer(1))

    def test_check_answer_out_of_bounds(self):
        self.assertFalse(self.question.check_answer(5))

    def test_check_answer_negative(self):
        self.assertFalse(self.question.check_answer(-1))


if __name__ == '__main__':
    unittest.main()
