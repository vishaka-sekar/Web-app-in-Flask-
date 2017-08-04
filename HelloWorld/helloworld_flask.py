from flask import Flask, render_template

app = Flask(__name__)
app.debug= True;

@app.route('/hello/<user>/')

def hello(user):
 #   return 'Hello World ! %s'%user wihtout templating

#with templates
    return render_template('login.html', name = user)




if __name__ == "__main__":
    app.run()