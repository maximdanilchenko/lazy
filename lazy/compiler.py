class MarkedLazy:
    def __init__(self, name):
        self.name = name


class Lazy:
    doctype = '<!DOCTYPE html>'
    no_close = {'meta', 'link', 'br'}
    html_tag = 'html'

    def __init__(self):
        self.page = ''
        self.open = ''
        self.close = ''

    def to_tag(self, elem, attributes):
        if elem == self.html_tag:
            self.open = '%s%s<%s%s>' % (self.doctype, self.open, elem, self.to_attributes(attributes))
        else:
            self.open = '%s<%s%s>' % (self.open, elem, self.to_attributes(attributes))
        if elem not in self.no_close:
            self.close = '</%s>%s' % (elem, self.close)

    @staticmethod
    def to_attributes(attributes):
        atr = ' '.join('%s="%s"' % (k.strip('_'), v.replace('"', "'")) for k, v in attributes.items())
        if atr:
            return ' %s' % atr
        return ''

    def to_page(self):
        self.page = '%s%s%s' % (self.open, self.page, self.close)
        self.open = ''
        self.close = ''

    def __getattr__(self, key):

        def fn(**attributes):
            self.to_tag(key, attributes)
            return self

        return fn

    def _close(self):
        self.to_page()
        return self.page

    def compiled(self, **kwargs):
        self.to_page()
        return self.page.format(**{key: name._close() if isinstance(name, Lazy) else name
                                   for key, name in kwargs.items()})

    def contains(self, *content):
        if content:
            self.page = '%s%s' % (self.page,
                                  ''.join(
                                      lazy._close() if isinstance(lazy, Lazy)
                                      else '{%s}' % lazy.name if isinstance(lazy, MarkedLazy)
                                      else lazy if isinstance(lazy, str)
                                      else ''
                                      for lazy in content)
                                  )
        return self

    def tr(self, **attributes):
        self.to_tag('tr', attributes)
        return self

    def html(self, **attributes):
        self.to_tag('html', attributes)
        return self

    def body(self, **attributes):
        self.to_tag('body', attributes)
        return self

    def div(self, **attributes):
        self.to_tag('div', attributes)
        return self

    def h1(self, **attributes):
        self.to_tag('h1', attributes)
        return self

    def h2(self, **attributes):
        self.to_tag('h2', attributes)
        return self

    def h3(self, **attributes):
        self.to_tag('h3', attributes)
        return self

    def h4(self, **attributes):
        self.to_tag('h4', attributes)
        return self

    def h5(self, **attributes):
        self.to_tag('h4', attributes)
        return self

    def h6(self, **attributes):
        self.to_tag('h5', attributes)
        return self

    def p(self, **attributes):
        self.to_tag('p', attributes)
        return self

    def a(self, **attributes):
        self.to_tag('a', attributes)
        return self

    def table(self, **attributes):
        self.to_tag('table', attributes)
        return self

    def th(self, **attributes):
        self.to_tag('th', attributes)
        return self

    def td(self, **attributes):
        self.to_tag('td', attributes)
        return self

    def header(self, **attributes):
        self.to_tag('header', attributes)
        return self

    def footer(self, **attributes):
        self.to_tag('footer', attributes)
        return self

    def meta(self, **attributes):
        self.to_tag('meta', attributes)
        return self

    def link(self, **attributes):
        self.to_tag('link', attributes)
        return self

    def br(self, **attributes):
        self.to_tag('br', attributes)
        return self

    def pre(self, **attributes):
        self.to_tag('pre', attributes)
        return self

    def code(self, **attributes):
        self.to_tag('code', attributes)
        return self

    def title(self, **attributes):
        self.to_tag('title', attributes)
        return self
