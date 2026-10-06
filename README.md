# Password Security Lab

An interactive password-security demonstration built with Python, Flask, HTML, CSS, and JavaScript.

The project explores how password characteristics, hashing, and salting work through a simple browser-based security lab.

Educational project: Only use fictional passwords. Never enter passwords used for real accounts.

## Overview

Password Security Lab allows users to enter a fictional password and observe several security characteristics.

The application calculates:

- Password length
- Estimated entropy
- Strength classification
- SHA-256 hash
- Random salt
- Salted hash

It also demonstrates an important security principle:

The same password combined with different salts produces different hashes.

## How It Works

User enters password
        ↓
JavaScript sends password to Flask
        ↓
Flask processes the request
        ↓
Python calculates password characteristics
        ↓
Entropy + strength + hashes + salts
        ↓
JSON response
        ↓
Results displayed in browser

## Features

### Password Analysis

The application analyzes the entered password and reports its length, estimated entropy, and a simple strength classification.

### Entropy Estimation

Entropy is estimated from the password length and the character groups used:

- Lowercase letters
- Uppercase letters
- Numbers
- Punctuation

The result is expressed in bits.

### SHA-256 Demonstration

The application generates a SHA-256 hash to demonstrate how a password can be transformed into a fixed-length hexadecimal representation.

This is included for educational purposes and is not recommended for real password storage.

### Salting Demonstration

A cryptographically secure random salt is generated using Python's secrets module.

The application then combines the salt with the password before hashing.

Two different salts are generated for the same password to demonstrate that:

Same password + Salt A → Hash A

Same password + Salt B → Hash B

Hash A ≠ Hash B

This illustrates why salting helps prevent identical passwords from producing identical stored hashes.

## Technology

- Python
- Flask
- JavaScript
- HTML
- CSS
- SHA-256
- Python secrets module
- Browser Fetch API

## Project Structure

password-security-lab/
├── app.py
├── security.py
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── script.js
│   └── style.css
└── venv/

## Running Locally

Clone the repository:

git clone https://github.com/shivanyaarunachalam/password-security-lab.git

Move into the project:

cd password-security-lab

Create a virtual environment:

python -m venv venv

Activate it on Git Bash:

source venv/Scripts/activate

Install Flask:

python -m pip install flask

Run the application:

python app.py

Open the local address shown in the terminal, usually:

http://127.0.0.1:5000

## Example

For a fictional password such as:

River!42Moon

the application can display:

Length: 12 characters
Entropy: 78.66 bits
Strength: Strong

It then generates a SHA-256 hash and demonstrates how different random salts produce different salted hashes.

## Technical Notes

The entropy calculation is an estimate based on the character pool and password length. It should not be interpreted as an exact measurement of real-world password security.

SHA-256 is used here to demonstrate the concept of cryptographic hashing. General-purpose hashes such as SHA-256 are not appropriate for storing real user passwords because they are designed to be fast.

Real password-storage systems should use dedicated password-hashing algorithms such as Argon2id, scrypt, or bcrypt with appropriate parameters.

## Why I Built This

Password security concepts are often taught as isolated definitions.

This project was built to make those concepts observable through an interactive application.

Instead of only explaining hashing and salting, the lab allows users to see how the same password produces different salted hashes when different random salts are used.

## Future Improvements

Possible extensions include:

- Password breach detection using a safe demonstration dataset
- Password policy comparison
- Visual entropy comparison
- Password-storage algorithm comparison
- Rate-limiting simulation
- Interactive attack-cost demonstrations using fictional data

## Author

Shivanya Arunachalam

Computer Science and Engineering Student

GitHub: https://github.com/shivanyaarunachalam