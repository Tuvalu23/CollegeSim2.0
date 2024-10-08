from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_college', methods=['GET', 'POST'])
def select_college():
    colleges = ['MIT', 'Georgia Tech']
    return render_template('select_college.html', colleges=colleges)

@app.route('/login/<college_name>', methods=['GET', 'POST'])
def login(college_name):
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('status', college_name=college_name, name=name))
    return render_template(f'{college_name.lower()}_login.html')

@app.route('/status/<college_name>/<name>')
def status(college_name, name):
    return render_template(f'{college_name.lower()}_status.html', name=name)

@app.route('/decision/<college_name>/<name>')
def decision_letter(college_name, name):
    decision = random.choice(['Accepted', 'Rejected'])
    return render_template(f'{college_name.lower()}_decision.html', name=name, decision=decision)

if __name__ == '__main__':
    app.run(debug=True)
