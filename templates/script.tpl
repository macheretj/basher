#!/bin/bash

# {{ par.scriptname }}      ||  Version: {{ par.version }}
# Description: {{ par.description }}                                  
# Author: {{ par.name }}                                 
# Creation date: {{ par.createdate }}                    


function init{

    main

}


function main{

    echo "{{ par.scriptname }} , version: {{ par.version }}"

}

init