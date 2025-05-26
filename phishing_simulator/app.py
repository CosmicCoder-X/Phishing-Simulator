from flask import Flask, render_template, request, session, redirect, url_for
from phishing_engine.generator import generate_email
import csv
import os

app = Flask(__name__)
app.secret_key = 'your-secure-key'

# CSV logging
def log_result(email, answer, correct):
    filepath = r"C:\Users\divya\OneDrive\Desktop\phishing_simulator\data\results.csv"
    header = ['subject', 'from', 'user_answer', 'correct']
    row = [email['subject'], email['from'], answer, correct]

    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

@app.route('/')
def index():
    email = generate_email()
    session['email'] = email
    return render_template('email.html', email=email)

@app.route('/answer', methods=['POST'])
def answer():
    user_answer = request.form.get('answer')
    email = session.get('email')
    correct = 'phishing'  # all are phishing in this basic version
    is_correct = (user_answer == correct)

    log_result(email, user_answer, is_correct)

    feedback = "✅ Correct!" if is_correct else "❌ Incorrect. That was a phishing email."
    return render_template('feedback.html', feedback=feedback, email=email)

if __name__ == '__main__':
    app.run(debug=True)
