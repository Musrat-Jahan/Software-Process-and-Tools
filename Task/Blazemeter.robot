*** Settings ***
Library  SeleniumLibrary
Suite Setup  Open Website
Suite Teardown  Close Browser
Task Setup  Set Selenium Speed    0.1 seconds
Resource  BM_Resources.robot

*** Test Cases ***
Searching for flights
    Select Departure City    Boston
    Select Destination City    London
    Search For Flights

Choosing flights
    Check if Flights Are Available
    Choosing Flight     3

Enter Details and Purchase Ticket
    Enter Particulars
    Purchase Flights

