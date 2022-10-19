from flask import Flask
app = Flask(__name__)
@app.route('/')
def test_test():
    return 'Its working!'

# use in command line in terminal: export FLASK_APP=app.py
#lask run

