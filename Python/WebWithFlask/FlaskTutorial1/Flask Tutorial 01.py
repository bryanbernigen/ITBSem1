from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Ini Home Page</h1>'

@app.route('/owner')
def about():
    return '<h1>Owner: Bryan Bernigen/16520237</h1>'

if __name__ == '__main__':
    app.run(debug=True)
