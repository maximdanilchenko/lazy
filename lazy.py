
DOCTYPE = '<!DOCTYPE html>'


class Lazy:

    def __init__(self):
        self.page = ''
        self.open = ''
        self.close = ''

    def _to_tag(self, elem, attributes, need_close=True):
        self.open = '{open}<{elem}{attributes}>'.format(open=self.open, elem=elem,
                                                        attributes=self._to_attributes(attributes))
        if need_close:
            self.close = '</{elem}>{close}'.format(elem=elem, close=self.close)

    @staticmethod
    def _to_attributes(attributes):
        atr = ' '.join('%s="%s"' % (k.strip('_'), v.replace('"', "'")) for k, v in attributes.items())
        if atr:
            return ' %s' % atr
        return ''

    def _to_page(self):
        self.page = '%s%s%s' % (self.open, self.page, self.close)
        self.open = ''
        self.close = ''

    def __getattr__(self, key):

        def fn(*contents, need_close=True, content=None, **attributes):
            self._to_tag(key, attributes, need_close)
            content = list(content) if content else []
            content.extend(contents)
            if content:
                self.page = '%s%s' % (self.page,
                                      ''.join(
                                          lazy._close() if isinstance(lazy, Lazy)
                                          else lazy if isinstance(lazy, str)
                                          else ''
                                          for lazy in content)
                                      )
            return self
        return fn

    def _close(self):
        self._to_page()
        return self.page

    def compiled(self):
        self._to_page()
        return '%s%s' % (DOCTYPE, self.page)


def tr(*args, **kwargs):
    return Lazy().tr(*args, **kwargs)


def html(*args, **kwargs):
    return Lazy().html(*args, **kwargs)


def body(*args, **kwargs):
    return Lazy().body(*args, **kwargs)


def div(*args, **kwargs):
    return Lazy().div(*args, **kwargs)


def h1(*args, **kwargs):
    return Lazy().h1(*args, **kwargs)


def h2(*args, **kwargs):
    return Lazy().h2(*args, **kwargs)


def h3(*args, **kwargs):
    return Lazy().h3(*args, **kwargs)


def h4(*args, **kwargs):
    return Lazy().h4(*args, **kwargs)


def h5(*args, **kwargs):
    return Lazy().h5(*args, **kwargs)


def h6(*args, **kwargs):
    return Lazy().h6(*args, **kwargs)


def p(*args, **kwargs):
    return Lazy().p(*args, **kwargs)


def a(*args, **kwargs):
    return Lazy().a(*args, **kwargs)


def table(*args, **kwargs):
    return Lazy().table(*args, **kwargs)


def th(*args, **kwargs):
    return Lazy().th(*args, **kwargs)


def td(*args, **kwargs):
    return Lazy().td(*args, **kwargs)


def header(*args, **kwargs):
    return Lazy().header(*args, **kwargs)


def footer(*args, **kwargs):
    return Lazy().footer(*args, **kwargs)


def meta(*args, **kwargs):
    return Lazy().meta(*args, need_close=False, **kwargs)


def link(*args, **kwargs):
    return Lazy().link(*args, need_close=False, **kwargs)


if __name__ == '__main__':
    """testing"""
    page = html(
        link(rel='stylesheet', href='https://www.w3schools.com/w3css/4/w3.css'),
        body().div(
            h2('Название'),
            div(class_='w3-panel w3-card-2').table(tr(th('Таблица')),
                                                   tr(td('один')),
                                                   tr(td('два')), class_='w3-table'),
            class_='w3-container'
        )
    ).compiled()

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def main():
        return page, 200

    app.run()
