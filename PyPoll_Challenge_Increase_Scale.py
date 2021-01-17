# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""
"""Detail breakdown"""

# Add our dependencies.
import csv
import os

# create a variable for listing the files
fileList=[]

# list all files within the directory (up level)/Resources & populate variable
for root, dirs, files in os.walk(".", "Resources"):
    fileList = files

for item in file_to_load:
    input_name = item
    output_name = item+ "_analysis.txt"

# Add a variable to load a file from a path.
file_to_load = os.path.join(".","Resources", input_name)

# Add a variable to save the file to a path.
file_to_save = os.path.join(".", "analysis", output_name)

# TODO: insert working PyPoll_Challenge_Detail_breakdown.py script & indent appropriately