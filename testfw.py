from flask import Flask, render_template

app = Flask(__name__)

@app.route('/testfw')
def test_fw():
    return render_template('testfw.html')

if __name__ == '__main__':
    app.run(debug=True)