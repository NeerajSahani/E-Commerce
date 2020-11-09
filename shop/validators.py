from django.core.exceptions import ValidationError


def phone_validator(value):
    assert len(value) <= 10, ValidationError("Enter 10 Digits Mobile Number")
    return value
