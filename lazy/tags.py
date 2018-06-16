
class Tags:

    def to_tag(self, *_):
        raise NotImplementedError

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
