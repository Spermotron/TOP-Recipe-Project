import os
import hashlib

# Generate a 16-byte (128-bit) random salt
password = "Jojomamafriedrice@25!"
salt = os.urandom(16)

hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)  # Hash the password with the salt
print("Salt (hex):", salt.hex())
print("Hashed Password (hex):", hashed_password.hex())
