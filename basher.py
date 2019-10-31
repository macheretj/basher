#!/usr/bin/python

from jinja2 import Template, Environment, FileSystemLoader


def init():

    global results_dir
    results_dir = "results/"

def main():

    print("Hello")

    
    params = {
        "name": "Jonas Macheret",
        "version": "v1.0.0",
        "description": "tralala",
        "author": "Jojo",
        "createdate": "21.09.2019",
        "scriptname": "Skeletor"
    }

    tpl_render(params)


def tpl_render(params):

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('script.tpl')

    output = template.render(par=params)
    print(output)

    # Save the results

    with open(results_dir+params['scriptname'], "w") as fh:
        fh.write(output)


init()
main()
