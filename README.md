# PRODIGY_CS-03
Password Complexity Checker

Here's a Python program that serves as a password complexity checker. This tool assesses the strength of a password based on various criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. It also provides feedback to users on the password's strength.

Explanation:
password_strength function:

This function checks the password against various criteria:
Length should be at least 8 characters.
Should contain at least one lowercase letter.
Should contain at least one uppercase letter.
Should contain at least one number.
Should contain at least one special character (from the set @$!%*?&).
It calculates the strength of the password based on how many criteria are met.
It also generates feedback on which criteria are not met.
main function:

Prompts the user to enter a password.
Calls the password_strength function to assess the password.
Prints the strength level of the password based on the number of criteria met.
Provides feedback on how to improve the password if necessary.
