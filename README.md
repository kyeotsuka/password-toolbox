# Python Password Toolbox

A command-line toolkit for generating secure passwords and analysing their strength based on modern cybersecurity principles. This project demonstrates best practices in Python object-oriented design, secure coding, and adherence to current standards like the NIST Digital Identity Guidelines.

## Features

- **Advanced Strength Analysis:** The checker evaluates passwords based on a sophisticated set of rules.

    - Checks for minimum length, character variety, and predictable patterns like repeated characters.

    - Includes specialised logic to correctly identify and reward the strength of modern passphrases (e.g., "three random words").

    - Penalises passphrases that use low word variety (e.g., "cat cat cat").

- **Secure Password Generation:** The generator can create two types of strong passwords.

    - **Complex Passwords:** Generates cryptographically secure random-character passwords.

    - **Passphrases:** Generates memorable and highly secure multi-word passphrases using the EFF's Large Wordlist.
- **Clean Object-Oriented Design:** The toolkit is built with a clean separation of concerns, using distinct classes for the Password data object, the Generator, and the Checker.

## Authors

- [@kyeotsuka](https://github.com/kyeotsuka)

- [@mikeyangello9](https://github.com/mikeyangello9)