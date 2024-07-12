import unittest
from app.main import calculate_plagiarism_score

class TestPlagiarismDetector(unittest.TestCase):
    def test_identical_code(self):
        code = "def hello_world():\n    print('Hello, World!')"
        score = calculate_plagiarism_score(code, code)
        self.assertEqual(score, 100.0)

    def test_different_code(self):
        code1 = "def add(a, b):\n    return a + b"
        code2 = "def multiply(x, y):\n    return x * y"
        score = calculate_plagiarism_score(code1, code2)
        self.assertLess(score, 50.0)

    def test_similar_code(self):
        code1 = "def greet(name):\n    print(f'Hello, {name}!')"
        code2 = "def greeting(person):\n    print(f'Hi, {person}!')"
        score = calculate_plagiarism_score(code1, code2)
        self.assertGreater(score, 50.0)
        self.assertLess(score, 100.0)

if __name__ == '__main__':
    unittest.main()