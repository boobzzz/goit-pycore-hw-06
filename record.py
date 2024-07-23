from name import Name
from phone import Phone, PhoneData


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if not new_phone.value:
            return

        if not self.find_phone(new_phone):
            self.phones.append(new_phone)
            print("Phone added successfully")
        else:
            print("Phone already exists")

    def edit_phone(self, current: str, new: str):
        found_phone = self.find_phone(Phone(current))
        cur_phone = found_phone["phone"]
        new_phone = Phone(new)
        if not cur_phone.value or not new_phone.value or cur_phone.value == new_phone.value:
            return

        if found_phone:
            self.phones[found_phone["index"]] = new_phone
            print("Phone updated successfully")
        else:
            print("Phone does not exist")

    def remove_phone(self, phone: str):
        found_phone = self.find_phone(Phone(phone))
        if found_phone:
            self.phones.pop(found_phone["index"])
            print("Phone removed successfully")
        else:
            print("Phone does not exist")

    def find_phone(self, phone: Phone) -> PhoneData:
        values = [p.value for p in self.phones]
        found = None
        if phone.value in values:
            found = {
                "phone": phone,
                "index": values.index(phone.value)
            }
        return found

