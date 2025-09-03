# password-toolbox
A password toolbox. Password strength checker, generater and keeper.

# Features
- Checks strength of password 
- Generates secure password

<!-- temp -->

## Enhancing Your Existing Features
Before adding new things, let's make sure your current features are as robust as possible.

1. Advanced Password Strength Checker
A basic checker looks at length and character types. A professional one understands how passwords get cracked.

Entropy Calculation: Instead of a simple "score", calculate the password's entropy. Entropy, measured in bits, is a true gauge of how unpredictable a password is. The formula is H=L×log 
2
​
 (N), where L is the password length and N is the size of the pool of unique characters. A higher bit count is exponentially better (aim for >70 bits). This shows you understand the underlying mathematics.

Common Password & Dictionary Check: The biggest weakness is using a common password. Your tool should check the input against a list of the most common passwords (like a sample from the infamous "RockYou.txt" list). Also, check for dictionary words, common names, and simple keyboard patterns (e.g., qwerty, asdfgh).

The Best Method (The zxcvbn library): Honestly, the best way to implement all of the above is to use a battle-tested library. Dropbox created and open-sourced zxcvbn (there are Python ports like zxcvbn-python). It performs entropy checks, dictionary checks, pattern matching, and provides detailed feedback (e.g., "This is a common password", "A dictionary word is easy to guess"). Using and referencing a well-regarded security library shows you know how to leverage industry-standard tools.

2. Cryptographically Secure Password Generator
A standard random.choice() function isn't suitable for security-sensitive applications.

Use the secrets Module: Python's built-in random module is fine for games, but not for cryptography. The secrets module is specifically designed for generating cryptographically strong random numbers. Use secrets.choice() to pick characters. This is a crucial distinction that recruiters in the security field will notice.

Generate Passphrases: A very modern approach is to generate memorable passphrases based on the famous XKCD comic. Instead of Tr0ub4dor&3, you get correct-horse-battery-staple. These are often more secure and easier for humans to remember. You could use a wordlist (like the EFF's) and the secrets module to pick four or five random words.

Add Customisation: Allow the user to set parameters, such as length, and options to exclude ambiguous characters (e.g., I, l, 1, O, 0).

## Advanced New Features to Add
These features will elevate your project from a "generator" to a genuine "toolbox".

1. Pwned Password Checker (API Integration)
This is a fantastic feature. It checks if a password has appeared in a known data breach.

How it Works: Use the Have I Been Pwned (HIBP) Pwned Passwords API. Crucially, you must use it correctly to protect user privacy, which demonstrates your security-first mindset.

The K-Anonymity Model: You never send the plain-text password to the API. Instead:

You hash the password using SHA-1 (this is the specific hash the API requires).

You take the first 5 characters of the hexadecimal SHA-1 hash.

You send only those 5 characters to the HIBP API.

The API returns a list of all hash suffixes in its database that start with those 5 characters.

You then check locally, on your machine, if your full hash's suffix is in the returned list.

Why this is impressive: Implementing this correctly shows you understand hashing, how to use APIs securely, and the principle of k-Anonymity (hiding in a crowd) to protect data. It's a very practical, real-world security feature.

2. Secure Password Hasher
Show you understand how passwords should be stored. Add a feature that takes a password and securely hashes it.

Don't Use MD5/SHA-1: Explicitly state in your tool's UI or documentation why these are bad for password storage (they are too fast and susceptible to rainbow table/collision attacks).

Use a Modern Algorithm: Implement hashing using a modern, slow, salted hashing algorithm. The best choices are:

Argon2 (winner of the Password Hashing Competition)

scrypt

bcrypt

Explain the Concepts: Your tool should allow the user to see the salt (a unique random value added to each password before hashing) and adjust the work factor (a parameter that controls how slow/computationally expensive the hashing is). Showing these parameters demonstrates a deep understanding of preventing brute-force and rainbow table attacks. Python has great libraries like argon2-cffi and bcrypt.

## "Gold Standard" CV-Boosting Features
This is the stuff that really makes you stand out.

Two-Factor Authentication (2FA/TOTP) Tool
This is a brilliant feature to include. It shows you're thinking about authentication as a multi-layered process, not just about passwords.

Secret Key Generator: Create a function that generates a cryptographically secure base32-encoded secret key, which is the foundation of 2FA.

QR Code Generation: Use the generated secret key to create a QR code. When scanned by an authenticator app (like Google Authenticator or Authy), it will add the account. You can use a library like qrcode in Python.

Token Verification: Add a function where a user can input their secret key and a 6-digit token from their authenticator app, and your tool will verify if the token is correct.

Libraries like pyotp can handle the underlying TOTP (Time-based One-Time Password) algorithm, but by building the user-facing tools around it (key generation, QR display, verification), you're showing a complete understanding of the entire 2FA workflow.