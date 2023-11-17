
from flask import Flask, render_template,url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', page_title='Home', page_subtitle='Welcome to my website!')

@app.route('/about')
def about():
    return render_template('about.html', page_title='About', page_subtitle='About me')

@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact', page_subtitle='Contact me')

@app.route('/login', methods=['GET', 'POST'])   
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html', page_title='Login', page_subtitle='Login to your account')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('register.html', page_title='Register', page_subtitle='Register a new account')
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
