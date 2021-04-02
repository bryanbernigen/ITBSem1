from flask import render_template, url_for, flash, redirect, request
from FlaskTutorial import db,bcrypt
from FlaskTutorial.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from FlaskTutorial.models import User, Post
from FlaskTutorial.users.utils import save_picture, send_reset_email
from flask_login import login_user, current_user,logout_user, login_required
from flask import Blueprint
users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('Anda Sudah Masuk Dengan Akun Anda','success')
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Akun berhasil dibuat!, Mohon Login Menggunakan Akun Anda', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Anda Sudah Masuk Dengan Akun Anda','success')
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Login Berhasil!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Gagal, Mohon Cek Kembali Email dan Kata Sandi Anda!', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/logout",)
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account",  methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file= save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Akun Anda Berhasil Diperbaharui!','success')
        return redirect(url_for('users.account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user) \
        .order_by(Post.date_posted.desc()) \
        .paginate(page=page, per_page=3)
    postss = Post.query.filter_by(author=user) \
        .order_by(Post.date_posted.desc()) \
        .paginate(page=page, per_page=1)
    return render_template('user_posts.html', posts=posts, postss=postss)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Sebuah Email telah Terkirim Berisi Cara Mengatur Ulang Kata Sandi Anda.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Atur Ulang Kata Sandi', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Token Tidak Valid atau Kadaluarsa', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Kata Sandi Anda Berhasil Diperbaharui! Anda DApat Login Menggunakan Kata Sandi Baru!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Atur Ulang Kata Sandi', form=form)