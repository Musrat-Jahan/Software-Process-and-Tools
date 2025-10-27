*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${website}  http://blazedemo.com
${browser}  chrome

*** Keywords ***
Open Website
    Open Browser  ${website}  ${browser}
    Maximize Browser Window
    Page should contain  Welcome

Select Departure City
    [Arguments]  ${departure_city}
    Select From List By Value  xpath://select[@name='fromPort']  ${departure_city}

Select Destination City
    [Arguments]  ${destination_city}
    Select From List By Value  xpath://select[@name='toPort']  ${destination_city}

Search For Flights
    Click Button  Find Flights

Check if Flights Are Available
    Page Should Contain     Flights from Boston to London
    @{flights}=  Get WebElements    css:table[class='table']
    Should Not Be Empty    ${flights}

Choosing Flight
    [Arguments]     ${Row}
    Click Element    //div[@class="container"]//table//tbody/tr[${Row}]/td[1]

Enter Particulars
    Input Text  inputName   User
    Input Text  address     CDU
    Input Text  city        Darwin
    Input Text  state       NT
    Input Text  zipCode     0810
    Select From List By Value  xpath://select[@name='cardType']  amex
    Input Text  creditCardNumber    1234567890
    Input Text  creditCardMonth     10
    Input Text  creditCardYear      2022
    Input Text  nameOnCard          Test User

Purchase Flights
    Click Button  Purchase Flight
    Capture Page Screenshot     Flight_Purchase_Invoice.png