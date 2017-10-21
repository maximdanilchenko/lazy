from flask import Blueprint, abort
from .pages import base, blog_page_body, about_page_body, post_page_body
from .posts_loader import posts_db


site = Blueprint('site', __name__)


@site.route('/')
@site.route('/posts')
def blog():
    return base.compiled(title='ProstoBlog | Статьи',
                         body=blog_page_body.compiled())


@site.route('/about')
def about():
    return base.compiled(title='ProstoBlog | Обо мне',
                         body=about_page_body.compiled())


@site.route('/posts/<string:post_date>')
def post(post_date):
    if post_date not in posts_db:
        abort(404)
    return base.compiled(title='ProstoBlog | %s' % posts_db[post_date]['name'],
                         body=post_page_body.compiled(name=posts_db[post_date]['name'],
                                                      abstract=posts_db[post_date]['abstract'],
                                                      content=posts_db[post_date]['content'])
                         )
