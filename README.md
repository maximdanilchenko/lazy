# lazy
Lazy can can generate html with python code without having to write html markup

### Simple example:
```python
from lazy import *

page = html().compiled()

print(page)

"""Output:
<!DOCTYPE html>
<html>
</html>
"""
```

### More complex example:
```python
from lazy import *

page = html().contains(
    meta(name='viewport', content='width=device-width, initial-scale=1'),
    title().contains('Page Title'),
    body().contains(h2(class_='some_class').contains('Header'),
                    p().contains('Hello world!'))
).compiled()


print(page)

"""Output:
<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page Title</title>
<body><h2 class="some_class">Header</h2>
<p>Hello world!</p></body>
</html>
"""
```

### *mark* function for parametrization templates:
```python
from lazy import *

page = html().contains(
    meta(name='viewport', content='width=device-width, initial-scale=1'),
    title().contains('Page Title'),
    mark('body')
)

body = body().contains(h2(class_='some_class').contains('Header'),
                       p().contains('Hello world!'))

print(page.compiled(body=body))

"""Output:
!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page Title</title>
<body><h2 class="some_class">Header</h2>
<p>Hello world!</p></body>
</html>
"""
```
