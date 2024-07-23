from typing import TypedDict
from field import Field
import re


class Phone(Field):
    phone_len = 10

    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        trimmed = ''.join(re.findall(r"\d+", self.value))
        if len(trimmed) >= Phone.phone_len:
            self.value = f"+38{trimmed[len(trimmed) - Phone.phone_len:]}"
        else:
            self.value = None
            print(f"Invalid phone {self.value} format: at least {Phone.phone_len} digits needed")


class PhoneData(TypedDict):
    phone: Phone
    index: int
