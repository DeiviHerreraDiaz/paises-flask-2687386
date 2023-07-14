from flask import Flask

# Creating variable
app = Flask(__name__)

@app.route('/')
def index():
    return 'FLASK FUNCIONA'