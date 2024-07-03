from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_session')
def add_session():
    return render_template('add_session.html')

@app.route('/testfw')
def testfw():
    return render_template('testfw.html')

@app.route('/submit', methods=['POST'])
def submit():
    selected_options = request.form.getlist('muscle_groups_trained')
    time_started = request.form.get('time_started')
    time_stopped = request.form.get('time_stopped')
    rpe = request.form.get('rpe')
    satisfaction_rating = request.form.get('satisfaction_rating')
    motivation_rating = request.form.get('motivation_rating')
    notes = request.form.get('notes')
    exercises_done = []
    exercise_names = request.form.getlist('exercise_name[]')
    sets_done = request.form.getlist('sets_done[]')
    reps_done = request.form.getlist('reps_done[]')

    current_rep_index = 0
    for i in range(len(exercise_names)):
        sets = int(sets_done[i])
        reps = reps_done[current_rep_index:current_rep_index + sets]
        current_rep_index += sets
        exercises_done.append({
            'exercise_name': exercise_names[i],
            'sets_done': sets,
            'reps_done': reps
        })

    time_format = "%H:%M"
    start_time = datetime.strptime(time_started, time_format)
    stop_time = datetime.strptime(time_stopped, time_format)
    duration = stop_time - start_time
    workout_duration = duration.total_seconds() / 60
    return f'''
        Selected options: {", ".join(selected_options)}<br>
        Time started: {time_started}<br>
        Time stopped: {time_stopped}<br>
        Duration: {workout_duration}mins<br>
        RPE: {rpe}<br>
        Satisfaction rating: {satisfaction_rating}/5<br>
        Motivation rating: {motivation_rating}/5<br>
        Notes: {notes}<br>
        Exercises done: {exercises_done}
    '''


if __name__ == '__main__':
    app.run(debug=True)