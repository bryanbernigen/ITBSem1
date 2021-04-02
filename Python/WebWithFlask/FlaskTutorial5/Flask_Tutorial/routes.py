from flask import Flask, render_template, url_for, flash, redirect
from Flask_Tutorial import app
from Flask_Tutorial.forms import RegistrationForm,LoginForm
from Flask_Tutorial.models import User, Post

data = [
    {
        'nama': 'Corey Schafer',
        'judul': 'Blog Post 1',
        'konten': 'First post content',
        'tanggal': 'April 20, 2018'
    },
    {
        'nama': 'Jane Doe',
        'judul': 'Blog Post 2',
        'konten': 'Second post content',
        'tanggal': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', data=data)

@app.route("/owner")
def about():
    return render_template('owner.html', title='Owner')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Akun {form.username.data} berhasil dibuat!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Sukses!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Gagal, Mohon Cek Kembali Email dan Kata Sandi Anda!', 'danger')
    return render_template('login.html', title='Login', form=form)
