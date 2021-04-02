from flask import render_template, request
from FlaskTutorial.models import Post
from flask import Blueprint
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/owner")
def about():
    return render_template('owner.html', title='Owner')