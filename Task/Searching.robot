*** Settings ***
Library  SeleniumLibrary
Library    XML
Resource   Searching_Resources.robot
Suite Teardown  Close Browser

*** Test Cases ***
Open Website
    Searching using Google

Searching Website
    Search Topic    python

Going to Python Website
    Selecting a page and verify    Welcome to Python.org

Navigating within Python Website
    Viewing More On    Success Stories
    Reading On         Clean and Safe

Searching within Python Website
    Search Topic    code

Choosing a Menu
    Choose Menu On   Jobs
    Display Info to Console


