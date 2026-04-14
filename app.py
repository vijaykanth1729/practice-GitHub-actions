from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask is accessible by any IP!"

@app.route('/api')
def hello_api():
    return "Hello, Flask is accessible by api endpoint..!"

if __name__ == '__main__':
    # host='0.0.0.0' allows access from any IP address
    # debug=True enables the interactive debugger and auto-reloader
    app.run(host='0.0.0.0', port=5000, debug=True)

