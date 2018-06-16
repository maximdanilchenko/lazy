from functools import partial

from .compiler import Compiler
from .tags import Tags


class Lazy(Compiler, Tags):

    @classmethod
    def new(cls, tag, **attributes):
        new = cls()
        new.to_tag(tag, attributes)
        return new


html = partial(Lazy.new, tag='html')
body = partial(Lazy.new, tag='body')
div = partial(Lazy.new, tag='div')
h1 = partial(Lazy.new, tag='h1')
h2 = partial(Lazy.new, tag='h2')
h3 = partial(Lazy.new, tag='h3')
h4 = partial(Lazy.new, tag='h4')
h5 = partial(Lazy.new, tag='h5')
h6 = partial(Lazy.new, tag='h6')
p = partial(Lazy.new, tag='p')
a = partial(Lazy.new, tag='a')
br = partial(Lazy.new, tag='br')
table = partial(Lazy.new, tag='table')
tr = partial(Lazy.new, tag='tr')
th = partial(Lazy.new, tag='th')
td = partial(Lazy.new, tag='td')
title = partial(Lazy.new, tag='title')
header = partial(Lazy.new, tag='header')
footer = partial(Lazy.new, tag='footer')
meta = partial(Lazy.new, tag='meta')
link = partial(Lazy.new, tag='link')
pre = partial(Lazy.new, tag='pre')
code = partial(Lazy.new, tag='code')
