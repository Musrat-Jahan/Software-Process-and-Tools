*** Settings ***
Library  SeleniumLibrary
Library    XML

*** Variables ***
${Website}  http://google.com
${Browser}  chrome

*** Keywords ***
Searching using Google
    Open Browser  ${Website}  ${Browser}
    Maximize Browser Window
    Set Selenium Speed    0.05 seconds
    Title Should Be    Google                           #Page Should Contain  About
    Capture Page Screenshot     screenshot.png

Search Topic
    [Documentation]  Searching topic
    [Arguments]  ${topic}
    Input Text  name=q  ${topic}
    Press Keys  name=q  RETURN                          #Press Key  name=q  \\13

Selecting a page and verify
    [Arguments]  ${page}
    Click Element    xpath://h3[contains(text(), '${page}')]
    Title Should Be    Welcome to Python.org
    Page Should Contain    Python is a programming language that lets you work quickly and integrate systems more effectively.
    Execute Javascript  window.scrollTo(0,800)

Viewing More On
    [Arguments]     ${details}
    Click Element    xpath://a[contains(@title, '${details}')]          #or    Click Element    xpath://a[@title="More Success Stories"]
    Title Should Be    Our Success Stories | Python.org

Reading On
    [Arguments]     ${news}
    Click Element    xpath://a[contains(text(), '${news}')]
    Title Should Be  Deliver Clean and Safe Code for Your Python Applications | Our Success Stories | Python.org

Choose Menu On
    [Arguments]     ${headings}
    Click Link    ${headings}
    Title Should Be    Python Job Board | Python.org

Display Info to Console
    ${display}=         Get Text            xpath://div/h1[@class="call-to-action"]                      #or xpath://div[@class="jobs-intro"]//.h1[contains(text(), 'jobs on')]
    Log To Console      ${display}