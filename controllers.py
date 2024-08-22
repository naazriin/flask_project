from flask import redirect, url_for, render_template, request
from app import app
                        
from models import Blog

user_list = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'user1@gmail.com',
        'password': '1234'
    },
        {
        'id': 2,
        'name': 'Kate Spade',
        'email': 'user2@gmail.com',
        'password': '12345'
    },
        {
        'id': 3,
        'name': 'Cassie Clark',
        'email': 'user3@gmail.com',
        'password': '123456'
    }
]



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home-redirection')
def home():
    return redirect(url_for('index'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        for i in user_list:
            if i['email'] == email:
                if i['password'] == password:
                    return redirect(url_for('profile', name= i['name']))
    return render_template('login.html')


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user_list.append({
            'id': len(user_list)+1,
            'name': name,
            'email': email,
            'password': password
        })
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/blogs')
def blogs():
    blogs = Blog.query.all()
    context = {
        'blogs': blogs
    }
    return render_template('blog.html', **context)