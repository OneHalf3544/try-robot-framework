*** Settings ***
Library     ValidNumberSpecification.py

*** Test Cases ***
String with integer number should be considered as valid number
    is a valid number    12323

Trailing spaces doesn't affect a result
    is a valid number    ${SPACE * 2}23${SPACE}

Allow decimal values (at most one decimal dot is allowed)
    is a valid number    0.23
    is a valid number    123.23
    is not a valid number    1.23.23


A string doesn't have to have digits after a decimal dot
    is a valid number    12.

Can start with dot (considered as a number with leading zero)
    is a valid number    .3

Leading signs (- or +) are allowed
    is a valid number    +123.23
    is a valid number    -123.23

    is not a valid number    --123.23
    is not a valid number    +-123.23


An exponent is allowed
    is a valid number    +123.2e3
    is a valid number    -123.2e+3

Should contain any digit at least
    is not a valid number    ${SPACE * 2}
    is not a valid number    .
    is not a valid number    abc

Cannot start with exponent
    is not a valid number    e9
    is not a valid number    -e58

Cannot use decimal exponent
    is not a valid number    12e2.5

Only one exponent letter is allowed
    is not a valid number    12e2e5
