*** Settings ***
Library  SeleniumLibrary
Library    XML

*** Variables ***
${Website}  https://news.com.au
${Browser}  chrome

*** Keywords ***
Open Website
    Open Browser  ${Website}  ${Browser}
    Maximize Browser Window
    Set Selenium Speed    0.5 seconds

Select location
    [Arguments]     ${POSTCODE}
    Click Element   xpath://div[@class="weather-widget_location weather-widget_item"]
    Input Text      id=weather-widget_location    ${POSTCODE}
    Click Button    Ok

Display Min and Max Temperature
    ${MIN}=        Get Text    xpath://div//span[@class="weather-widget_temperature_min"]
    ${MAX}=        Get Text    xpath://div//span[@class="weather-widget_temperature_max"]
    Log To Console    The Minimum Temperature is ${MIN}
    Log To Console    The Maximum Temperature is ${MAX}