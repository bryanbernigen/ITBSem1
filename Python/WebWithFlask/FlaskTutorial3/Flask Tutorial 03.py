from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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


if __name__ == '__main__':
    app.run(debug=True)