import binascii
import hashlib
import os


class HashPassword:
    def __init__(self):
        self.salt = b'4e43860f7089025601c5ffcc507e3b57cb59ba93d1c4c466235a0f8d65637f25'

    def hash_password(self, password):
        """Hash a password for storing."""
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      self.salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (self.salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      self.salt,
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
