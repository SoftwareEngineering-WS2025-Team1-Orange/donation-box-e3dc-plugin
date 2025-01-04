from ..utils.settings import settings
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import HTTPException


class AuthService:
    def __init__(self):
        self.ph = PasswordHasher()
        self.passkey = self.ph.hash(settings.api_passkey)

    def validate_passkey(self, passkey):
        try:
            self.ph.verify(self.passkey, passkey)
        except VerifyMismatchError:
            raise HTTPException(status_code=403, detail="Invalid passkey")
