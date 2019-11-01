#!/usr/bin/python

import os
import click
from pyfiglet import Figlet

from jinja2 import Template, Environment, FileSystemLoader


custom_fig = Figlet(font='slant')
print(custom_fig.renderText('<< Basher >>'))

print("Please input basic script creation information. Avoid using spaces in the script name.")
@click.command()
@click.option('--scriptname', prompt='Script name',help='The name of the script')
@click.option('--name', prompt='Your name',help='The person to greet.')
@click.option('--description', prompt='Script short descrtiption:',help='The script short description')
@click.option('--createdate', prompt='Creation date:',help='The script creation date.')
@click.option('--version', prompt='Version', help='Initial version.')


def init(version,name,description,createdate,scriptname):


                                         

    global build_dir
    build_dir = "build/"

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    params = {
        "name": name,
        "version": version,
        "description": description,
        "createdate": createdate,
        "scriptname": scriptname
    }

    basher(params)

def basher(params):

    print("Hello")

    
  

    tpl_render(params)


def tpl_render(params):

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('script.tpl')

    output = template.render(par=params)
    print(output)

    # Save the results

    with open(build_dir+params['scriptname'], "w") as fh:
        fh.write(output)



if __name__ == '__main__':
    init()