*** Settings ***
Library  SeleniumLibrary
Suite Setup     Open Website
Resource    Temperature_Resources.robot

*** Test Cases ***
Get Temperature Information
    Select location    0810
    Display Min and Max Temperature





