import os

posts = os.listdir('./posts')
posts.sort(reverse=True)


def read(dr):
    return (
        open('%s/name.txt' % dr).read(),
        open('%s/abstract.txt' % dr).read(),
        open('%s/content.txt' % dr).read(),
    )


posts_db = {}

for index, post in enumerate(posts):
    name, abstract, content = read('./posts/%s' % post)
    content = content.replace(
        '\n\n', '<br>'
    ).replace(
        '**/\n', '<pre class="w3-panel w3-leftbar w3-border-green"><code>'
    ).replace(
        '/**', '</code></pre>'
    )
    posts_db[post] = {'name': name, 'abstract': abstract, 'content': content, 'date': post}
