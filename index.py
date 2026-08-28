from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"
    
@app.route("/aasim")
def index1():
    return "<h1>Hello Aasim</h1>"
    
@app.route("/ashif")
def index2():
    return "<h1>Hello Ashif!</h1>"

@app.route("/hamza")
def index2():
    return "<h1>Hello Hamza!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
