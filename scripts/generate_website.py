from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json

def main():
    TEMPLATE_FILE = "index.html.jinja"
    DATA_FILE = "data.json"
    OUT_FILE = "index.html"
    # create the intermediate dirs for the out file
    out_dir = os.path.dirname(OUT_FILE)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(DATA_FILE) as fd:
        data = json.load(fd)

    env = Environment(
        loader = FileSystemLoader("templates"),
        autoescape = select_autoescape()
    )
    template = env.get_template(TEMPLATE_FILE)
    with open(OUT_FILE, "w", encoding="utf-8") as fd:
        fd.write(template.render(data=data))

if __name__ == "__main__":
    main()