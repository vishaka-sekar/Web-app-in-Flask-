from flask import Flask

app = Flask(__name__)
app.debug= True;

@app.route('/hello/')

def hello():
    return "Hello World !"

@app.route('/python/')
def hello_python():
   return 'Hello Python'


if __name__ == "__main__":
    app.run()