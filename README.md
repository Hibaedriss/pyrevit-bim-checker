# BIM Checker (pyRevit)

A simple BIM quality checking tool built using Python and pyRevit for Autodesk Revit.

## Overview

This project demonstrates how to extend Autodesk Revit using Python and the Revit API through pyRevit.

The tool checks doors in a Revit model and detects missing Width parameters.

## Features

- Custom button inside Revit
- Checks doors in the model
- Detects missing width values
- Displays results inside Revit

## Technologies

- Python
- pyRevit
- Revit API

## How to Use

1. Copy the folder `MyBIMTools.extension` into:
   %appdata%\pyRevit\Extensions

2. Open Revit

3. Click:
   pyRevit → Reload

4. Go to:
   MyTools → QA → BIM Checker

## Folder Structure

MyBIMTools.extension
└── MyTools.tab
    └── QA.panel
        └── BIM Checker.pushbutton
            └── script.py

## Author

BIM + Programming learning project
