from flask import Flask

app = Flask(__name__)
@app.route('/')  #defines_URL
def hello():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)