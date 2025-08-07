# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

quiz_data = [
    {
        'id': 'q1',
        'question': 'What is my last name?',
        'choices': ['Vasquez', 'Vazquez', 'Valazquez', 'Valencia'],
        'answer': 'Vazquez'
    },
    {
        'id': 'q2',
        'question': 'Which bourgh am I from?',
        'choices': ['brooklyn', 'queens', 'bronx', 'manhattan'],
        'answer': 'brooklyn'
    },
    {
        'id': 'q3',
        'question': 'What is my fav fruit?',
        'choices': ['watermelon', 'strawberries', 'blackberries', 'papaya'],
        'answer': 'blackberries'
    },
    {
        'id': 'q4',
        'question': 'How many siblings do I have?',
        'choices': ['3', '1', '4', '2'],
        'answer': '2'
    }
]

@app.route('/')
def index():
    return render_template('quiz.html', questions=quiz_data)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    score = 0
    for q_data in quiz_data:
        question_id = q_data['id']
        correct_answer = q_data['answer']
        user_answer = request.form.get(question_id)
# .get(question_id) retrieves the value associated with the question_id from the submitted form data. This value would be the answer that the user selected or entered for that specific question.
        if user_answer == correct_answer:
            score += 1

    return render_template('results.html', score=score, total_questions=len(quiz_data))




if __name__ == '__main__':
    app.run(debug=True)