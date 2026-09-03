# はなうた帳：artifact用の本体（hanauta.html）を、自前の置き場（GitHub Pages）用の完全なHTMLに包む。
# 使い方: py -X utf8 build_pages.py [出力先]   省略時は docs/index.html
import io, sys, os
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, 'hanauta.html')
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'docs', 'index.html')
body = io.open(src, encoding='utf-8').read()
head = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="apple-mobile-web-app-capable" content="yes">'
        '<meta name="apple-mobile-web-app-status-bar-style" content="default">'
        '<meta name="theme-color" content="#F4F2F6">'
        '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 100 100%27%3E%3Ctext y=%27.9em%27 font-size=%2790%27%3E%F0%9F%8E%B6%3C/text%3E%3C/svg%3E">'
        '<link rel="apple-touch-icon" href="icon.png">'
        '<style>:root{color-scheme:light dark}body{margin:0}</style></head><body>\n')
tail = '\n</body></html>\n'
os.makedirs(os.path.dirname(out), exist_ok=True)
io.open(out, 'w', encoding='utf-8', newline='\n').write(head + body + tail)
print('wrote', out, len(head + body + tail), 'chars')
