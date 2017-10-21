from lazy import *
from .posts_loader import posts_db, posts

POSTS = 'posts'
ABOUT = 'about'
MAIN_NAME = 'ProstoBlog'
a_simple = 'w3-bar-item w3-button w3-hover-none w3-border-white w3-bottombar w3-hover-border-green'
a_chosen = 'w3-bar-item w3-button w3-hover-none w3-border-green w3-bottombar'
a_logo = 'w3-bar-item w3-button w3-hover-none w3-right'
a_read = 'w3-right w3-button w3-hover-none w3-hover-text-green w3-large'

base = html().contains(
    meta(name='viewport', content='width=device-width, initial-scale=1'),
    link(rel='stylesheet', href='https://www.w3schools.com/w3css/4/w3.css'),
    title().contains(mark('title')),
    mark('body')
)


def make_nav(page_name=None):
    return div(class_='w3-bar w3-border-bottom w3-border-green w3-large').contains(
        a(class_=a_chosen if page_name == POSTS else a_simple, href='../posts').contains('Статьи'),
        a(class_=a_chosen if page_name == ABOUT else a_simple, href='../about').contains('Обо мне'),
        a(class_=a_logo).contains(MAIN_NAME),
    )

blog_page_body = body(class_='w3-content').contains(
    make_nav(POSTS),
    *list(div(class_='w3-container w3-border-bottom').contains(
        p(class_='w3-opacity').contains('%s:' % post),
        h2().contains(posts_db[post]['name']),
        posts_db[post]['abstract'],
        br(),
        a(class_=a_read, href='./posts/%s' % post).contains('Читать..'),
    ) for post in posts)

)

about_page_body = body(class_='w3-content').contains(
    make_nav(ABOUT),
    div(class_='w3-container').contains('Что-то обо мне...')
)

post_page_body = body(class_='w3-content').contains(
    make_nav(),
    div(class_='w3-container').contains(
        h2().contains(mark('name')),
        mark('abstract'),
        br().br(),
        mark('content'),
    )
)
