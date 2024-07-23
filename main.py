from address_book import AddressBook


def main():
    book = AddressBook()
    book.add_record("James")
    book.add_record("Alex")
    print(book)

    james = book.find_record("James")
    james.add_phone("0123456789")
    james.add_phone("0987654321")
    james.add_phone("0987654321")
    james.edit_phone("0987654321", "0147258369")
    james.remove_phone("0147258369")
    print(james)

    alex = book.find_record("Alex")
    alex.add_phone("0112233445")
    alex.add_phone("0559963377")
    print(alex)

    book.delete_record("James")
    print(book)


if __name__ == "__main__":
    main()
