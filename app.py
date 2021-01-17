from flask import Flask, escape, request, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)