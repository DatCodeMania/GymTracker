from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_session')
def add_session():
    return render_template('add_session.html')

@app.route('/submit', methods=['POST'])
def submit():
    selected_options = request.form.getlist('muscle_groups_trained')
    return f'Selected options: {", ".join(selected_options)}'

if __name__ == '__main__':
    app.run(debug=True)