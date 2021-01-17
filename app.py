from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxx'

posts = [
    {
        'auth':'satya pati',
        'title':'first post',
        'content':'First post content'
    },
    {
        'auth':'Chorey scaffer',
        'title':'second post',
        'content':'second post content'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET','POST'])
def register():
    redg_form = RegistrationForm()
    if redg_form.validate_on_submit():
        flash(f"Account created for {redg_form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', r_form=redg_form)


@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash(f"Account created for {login_form.email.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', l_form=login_form)



if __name__ == '__main__':
    app.run(debug=True)