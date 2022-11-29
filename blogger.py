import datetime
import sys
import json
import time
import os
import markdown

date = datetime.date.today()

def new():
    nm = f"LOGS/{date}.md"
    _ = open(f"{nm}", "w")
    with open(".meta.json", "r") as f:
        txt = f.read()
    with open(".meta.json", "w") as f:
        l = json.loads(txt)
        l[nm] = os.path.getmtime(f"{nm}")
        f.write(json.dumps(l))
        
def update():
    with open(".meta.json", "r") as f:
        txt = f.read()
    with open(".meta.json", "w") as f:
        todo = {}
        l = json.loads(txt)
        for k, v in l.items():
            if (os.path.getmtime(k) - v) > 1:
                print(f"UPDATED {k}")
                with open(k, "r") as ff:
                    th_txt = ff.read()
                todo[k] = markdown.markdown(th_txt, extensions=['nl2br', 'fenced_code'])
        for k in todo.keys():
            l[k] = os.path.getmtime(k)
        f.write(json.dumps(l))
    for k, v in todo.items():
        with open(k.replace("LOGS", "LOGS/COMPILED").replace(".md", ".html"), "w") as f:
            stylish = """
<link rel='stylesheet' href='styles.css'>
<style>
    body {
        font-family: monospace;
        font-size: 200%;
    }
    .main {
        overflow-x: auto;
        overflow-y: auto;
        width: 100%;
        height: 100%;
    }
</style>
            """
            f.write(f"<div class='main'>{v}</div>\n{stylish}")
        with open(k.replace("LOGS", "LOGS/INSERT").replace(".md", ".js"), "w") as f:
            p_t = k.replace('LOGS/', "").replace(".md", "")
            p_v = k.replace("LOGS", "LOGS/COMPILED").replace(".md", ".html")
            f.write(f"LOGS[\"{p_t}\"] = `<embed type=\'text/html\' src=\'{p_v}\' width=\'100%\' height=\'100%\'>`")
        with open("index.html", "r") as f:
            txt = f.read()
        with open("index.html", "w") as f:
            line = f"<script src=\"LOGS/INSERT/{p_t}.js\"></script>"
            if line not in txt:
                txt = f"{txt}\n{line}"
            f.write(txt)




if __name__ == "__main__": 
    if sys.argv[1] == "n":
        new()
    elif sys.argv[1] == "u":
        update()
    elif sys.argv[1] == "r":
        while True:
            update()
            time.sleep(5)
