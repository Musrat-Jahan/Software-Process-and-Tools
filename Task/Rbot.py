*** Settings **
Documentation Login Functionality
Library SeleniumLibrary
*** variables **
*** keywords **
*** Test cases **
Open Website
[Documentation] This test case verify user is able to open the URL
Open Browser http://localhost/loginsystem/login.php chrome
Page Should Contain  Login Registration System


${URL}  http://localhost/loginsystem/login.php 
${Browser}  chrome


Login to your account
    Input Text    username    admin
    Input Text    password    admin
    Click Button    Login

Logout
    Click Element  xpath=//a[@data-toggle='dropdown']
    # Wait for the dropdown menu to be visible
    Wait Until Element Is Visible  xpath=//ul[@class='dropdown-menu']
    # Click the logout link
    Click Element  xpath=//ul[contains(@class, 'dropdown-menu')]//li[contains(@class, 'last')]
*** Settings ***
Documentation  Login Functionality
Library  SeleniumLibrary
Suite Setup  Go to Website
Suite Teardown  Close Browser
Task Setup  Set Selenium Speed   0.5 seconds

*** Variables ***
${URL}  http://localhost/loginsystem/login.php 
${Browser}  chrome


*** Keywords ***
Go to Website
    [Documentation]  This test case verify user is able to open the URL
    Open Browser  ${URL}  ${Browser}
    Page Should Contain  Login Registration System

Input username
    [Arguments]  ${username}    
    Input Text    username    ${username}


Input password
    [Arguments]  ${password}    
    Input Text    username    ${password}

Submit Credentials
    Click Button  Submit


Select details to view 
     Click Element    //div[@class="container mt-5"]//table//tbody/tr[9]/td[4]



Logout from system
    Click Link    Logout

Update your details
    [Documentation]  this is to update details
    [Arguments]  ${name}  ${username}  ${email}  ${password}  ${confirm_password} 
    Input Text  name  ${name}
    Input Text  username  ${username}
    Input Text  email  ${email}
    Input Text  password  ${password}
    Input Text  cpassword  ${confirm_password}
    Click Button  submit

*** Test Cases ***
Login to your account
    Input Text    username    test1
    Input Text    password    test1pw
    Click Button    Submit
View and Update details
    Click Element    //div[@class="container mt-5"]//table//tbody/tr[9]/td[4]
    Update your details   User    user1    user1@gmail.com   user1pw    user1pw
Logout
    Click Link    Logout