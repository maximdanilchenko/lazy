from functools import partial
from .compiler import Lazy


class LazyFabric:
    def __init__(self):
        pass

    @staticmethod
    def born(tag, **attributes):
        new_lazy = Lazy()
        new_lazy.to_tag(tag, attributes)
        return new_lazy

lf = LazyFabric()

html = partial(lf.born, tag='html')
body = partial(lf.born, tag='body')
div = partial(lf.born, tag='div')

h1 = partial(lf.born, tag='h1')
h2 = partial(lf.born, tag='h2')
h3 = partial(lf.born, tag='h3')
h4 = partial(lf.born, tag='h4')
h5 = partial(lf.born, tag='h5')
h6 = partial(lf.born, tag='h6')

p = partial(lf.born, tag='p')
a = partial(lf.born, tag='a')
br = partial(lf.born, tag='br')

table = partial(lf.born, tag='table')
tr = partial(lf.born, tag='tr')
th = partial(lf.born, tag='th')
td = partial(lf.born, tag='td')

title = partial(lf.born, tag='title')
header = partial(lf.born, tag='header')
footer = partial(lf.born, tag='footer')

meta = partial(lf.born, tag='meta')
link = partial(lf.born, tag='link')

pre = partial(lf.born, tag='pre')
code = partial(lf.born, tag='code')
