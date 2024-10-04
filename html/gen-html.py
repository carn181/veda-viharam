import re
from yattag import Doc
from yattag import indent
import os

chfolder="../chapters/"

def renderhtml(pages,n):
    doc, tag, text = Doc(nl2br=True).tagtext()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.stag('link',rel="stylesheet",href="style.css")
        with tag('body'):
            with tag('h1'):
                text("അധ്യായം "+str(n))
            for page in pages:
                with tag('div', id='page'):
                    with tag('div', id='pagetext'):
                        text(page[1])
                    with tag('div'):
                        doc.stag('img',src='../pages/'+page[0])
    return indent(doc.getvalue(),newline='\n',indent_text=True).replace('[','<h3>').replace(']','</h3>')


for n in range(1,51):
    with open(chfolder+"CH"+str(n)+".txt") as f: s = f.read()

    test = re.split('^(\\(.*\\))',s,flags=re.MULTILINE)[1:]

    pages=[]
    for i in range(0,(len(test))//2):
        pageno=re.sub("[\\(\\)]",'',test[2*i])

        pagetext=test[2*i+1]
        pages.append([pageno,pagetext])

    with open("CH"+str(n)+".html","w") as f: f.write(renderhtml(pages,n))
