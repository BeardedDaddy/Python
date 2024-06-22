"""Import doc from yattag."""

from yattag import Doc

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')

with tag("html"):
    with tag('head'):
        with tag('title'):
            text('Blade comes in theaters November 7 2025')
        with tag('body'):
            with tag('p'):
                text('Blade was the first Marvel Movie that premiered back in August 21 1998')
                
result = doc.getvalue()

from yattag import indent

with open('index.html', 'w') as file:
    file.writelines(indent(result))

