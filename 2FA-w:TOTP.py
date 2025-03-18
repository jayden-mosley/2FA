#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 00:17:09 2025

@author: Jayden Andrews
"""

import bcrypt
import pyotp
import time

# Simulated database
user_db = {}

def register(username, password):
    # Hash password which is not reversible
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Generate a TOTP secret key
    totp_secret = pyotp.random_base32()

    # Store user info
    user_db[username] = {"password": hashed_password, "totp_secret": totp_secret}

    print("\n Registration successful!")
    print("Save this TOTP secret key:", totp_secret)
    print("Use this key in Google Authenticator or a TOTP app.")

def login(username, password):
    if username not in user_db:
        print("\n User not found!")
        return

    stored_hash = user_db[username]["password"]
    totp_secret = user_db[username]["totp_secret"]


    if bcrypt.checkpw(password.encode(), stored_hash):
        print("\n Accessing Account")

        totp = pyotp.TOTP(totp_secret)
        otp = totp.now()
        print("Your current 2FA code:", otp)  # Simulating sending it to the user

        user_otp = input("Enter 2FA code: ")

        # Verify TOTP
        if totp.verify(user_otp):
            print("Login successful!")
        else:
            print("Incorrect 2FA code")
    else:
        print("Incorrect password")

# Simulated for prject
print("\n Welcome to Login Systems")

username = input("Choose a username: ")
password = input("Choose a password: ")
register(username, password)

# Simulate a login
time.sleep(2)
print("\n User added, please enter you details below")

username = input("Enter your username: ")
password = input("Enter your password: ")
login(username, password)
