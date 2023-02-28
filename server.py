from flask import Flask, render_template, session,redirect,request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods =['POST'])
def get():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['age']= request.form['age']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'


if __name__ == "__main__":
    app.run(debug=True)