#### Terminal commands ####

'pip install -r requirements' ## ensures requirements are installed

'python3 app.py' ## runs the application

'sudo nohup python3 app.py > log.txt 2>&1 &' ## this terminal command ensures that the app runs in the background even when the client is shut down




#### Imports ####

from flask import Flask, render_template




#### Styling flask with html ####

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/theleech')
def theleech():
    return render_template('theleech.html')

@app.route('/songsoftheweek')
def songsoftheweek():
    return render_template('songsoftheweek.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)