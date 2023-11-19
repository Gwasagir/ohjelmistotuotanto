*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  niklas  niklas123
    Output Should Contain   New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain    Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  k33!e  kalle123
    Output Should Contain    Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  juusto  ja
    Output Should Contain    Invalid password
    
 Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  juusto  jaaastopaa
    Output Should Contain    Invalid password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123