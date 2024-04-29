from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/login')
def login():
    # if request.method=='POST':
    # redirect(url_for('profile'))

    return render_template('login.html')

@app.route('/signin' )
def signin():

    return render_template('signin.html')

@app.route('/appointments')
def appointments():

    return render_template('appointments.html')

@app.route('/profile')
def profile():

    return render_template('profile.html')

@app.route('/health_details')
def health_details():
    return render_template("health_details.html")

if __name__ == '__main__':
    app.run(debug=True)