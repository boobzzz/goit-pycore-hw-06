from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, name: str):
        if not self.find_record(name):
            self[name] = Record(name)
            print("Record added successfully")
        else:
            print("Record already exists")

    def delete_record(self, name: str):
        has_record = self.find_record(name)
        if has_record:
            self.pop(name)
            print("Record deleted successfully")
        else:
            print("Record was not found")

    def find_record(self, name: str) -> Record:
        record = None
        if name in self:
            record = self[name]
        return record
