*** Settings ***
Library   ValidNumberSpecification.py

*** Test Cases ***
String with integer number should be considered as valid number
  12323 should be a valid number

Trailing spaces doesn't affect a result
  ${SPACE * 2}23${SPACE} should be a valid number

Allow decimal values (at most one decimal dot is allowed)
  0.23 should be a valid number
  123.23 should be a valid number
  1.23.23 is an invalid number


A string doesn't have to have digits after a decimal dot
  12. should be a valid number

Can start with dot (considered as a number with leading zero)
  .3 should be a valid number

Leading signs (- or +) are allowed
  +123.23 should be a valid number
  -123.23 should be a valid number

  --123.23 is an invalid number
  +-123.23 is an invalid number


An exponent is allowed
  +123.2e3 should be a valid number
  -123.2e+3 should be a valid number

Should contain any digit at least
  ${SPACE * 2} is an invalid number
  . is an invalid number
  abc is an invalid number

Cannot start with exponent
  e9 is an invalid number
  -e58 is an invalid number

Cannot use decimal exponent
  12e2.5 is an invalid number

Only one exponent letter is allowed
  12e2e5 is an invalid number

*** Keywords ***
${stringValue} should be a valid number
  is a valid number  ${stringValue}

${stringValue} is an invalid number
  is not a valid number  ${stringValue}