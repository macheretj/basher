#!/bin/bash

# Code information --------------------------------------
# {{ user_input.scriptname }}      ||  Version: {{ common_data.version }}
# Description: {{ user_input.description }}                                  

# Company information -----------------------------------
# Name: {{ common_data.company.name }}
# Address: {{ common_data.company.address }}                                 
# City: {{ common_data.company.city }}                                 
# Zip code: {{ common_data.company.zipcode }}                                 

# Author information -----------------------------------
# Name: {{ common_data.author.name }}                                 
# E-mail: {{ common_data.author.email }} 
# Job Ttitle: {{ common_data.author.jobtitle }}                                 


function init{

    main

}


function main{

    echo "{{ user_input.scriptname }} , version: {{ user_input.version }}"

}

init