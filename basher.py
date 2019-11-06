#!/usr/bin/python3

import os
import json
import click
from pyfiglet import Figlet
from jinja2 import Template, Environment, FileSystemLoader

custom_fig = Figlet(font='slant')
print(custom_fig.renderText('<< Basher >>'))

print("Please input basic script creation information. Avoid using spaces in the script name.")
@click.command()
@click.option('--scriptname', prompt='Script name',help='The name of the script')
@click.option('--description', prompt='Script short descrtiption:',help='The script short description')
@click.option('--language',type=click.Choice(['bash','perl','python'], case_sensitive=False),prompt='Language')

def build_user_input_dict(scriptname,description,language):

    user_input_dict = {
        "description": description,
        "scriptname": scriptname,
        "language": language,
    }

    return(user_input_dict)

def init():                              

    global build_dir
    build_dir = "build/"

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

def basher(user_input_dict):

    print("Hello")

    
    with open('templates/common_data.json', 'r') as f:
        common_data_dict = json.load(f)


    tpl_render(user_input_dict,common_data_dict)


def tpl_render(user_input_dict,common_data_dict):

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('script.tpl')

    output = template.render(user_input=user_input_dict,common_data=common_data_dict)
    print(output)

    # Save the results

    with open(build_dir+user_input_dict['scriptname'], "w") as fh:
        fh.write(output)


init()
user_input_dict = build_user_input_dict(scriptname,description,language)
basher(user_input_dict)
