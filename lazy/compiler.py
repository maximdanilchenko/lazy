

class MarkedLazy:

    def __init__(self, name):
        self.name = name


class Compiler:

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
        return self.page.format(**{key: name._close() if isinstance(name, Compiler) else name
                                   for key, name in kwargs.items()})

    def contains(self, *content):
        if content:
            self.page = '%s%s' % (self.page,
                                  ''.join(
                                      lazy._close() if isinstance(lazy, Compiler)
                                      else '{%s}' % lazy.name if isinstance(lazy, MarkedLazy)
                                      else lazy if isinstance(lazy, str)
                                      else ''
                                      for lazy in content)
                                  )
        return self
