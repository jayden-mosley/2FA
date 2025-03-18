# 🔐 Two-Factor Authentication (2FA) Using Python (TOTP-Based)

This project demonstrates TOTP (Time-based One-Time Password) 2FA in Python using pyotp and bcrypt. It simulates the login process where a user:

1.User enters their username & password
If the credentials are wrong, access is denied.
If correct, they move to the 2FA step.
2FA Step (TOTP Authentication)

2. The script generates a unique secret key per user.
The user manually enters the key in their Authenticator app (Google Authenticator, Authy, etc.).
The script shows the current TOTP code for reference.

3. User enters the TOTP code from the app
If it matches, authentication succeeds!
If incorrect, access is denied.

screnshot

## Why TOTP?
TOTP (Time-based One-Time Password) is widely used in real-world authentication systems like Google Authenticator, Microsoft Authenticator, and Authy.

More secure than SMS-based 2FA (which can be intercepted).
Offline – No internet needed to generate the code.
Industry standard – Used in OAuth, OpenID, and enterprise security.

## How does 2FA work?
Google Authenticator is a TOTP (Time-based One-Time Password) application that enhances security by generating temporary 6-digit codes used for two-factor authentication (2FA). When a user enables 2FA on a website, the server generates a secret key, which is shared with the user's app (usually via a QR code). The app then uses this key, along with the current time, to generate a unique one-time password every 30 seconds. When logging in, the user enters their usual credentials followed by the 6-digit code from Google Authenticator. The server, which knows the same secret key, verifies the code using the TOTP algorithm (HMAC-SHA1). If the code is correct, the user is granted access. This method is highly secure because it does not require an internet connection, is resistant to phishing attacks, and ensures that each code is only valid for a short time. In Python, this can be implemented using the pyotp library, which follows the same standard as Google Authenticator, allowing developers to integrate secure 2FA authentication into their applications effortlessly.
