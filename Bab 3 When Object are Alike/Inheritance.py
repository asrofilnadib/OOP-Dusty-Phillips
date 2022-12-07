class ContactList(list):
    def search(self, name):
        """mengembalikan semua kontak yang sesuai dengan kontak
        yang dicari"""
        matching_contact = []
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact


class LongDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
            return longest


class Contact(object):
    all_contact = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contact.append(self)


class Supplier(Contact):
    def order(self, order):
        print("Jika ini sistem asli maka akan mengirim pesanan "
              "{} untuk {}".format(order, self.name))


class MailSender:
    def send_email(self, message):
        print("mengirim pesan kepada " + self.email)


class EmailAbleContact(MailSender):
    pass


class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        """super() berfungsi untuk allowing us to call the parent
        method directly"""
        # super().__init__(name, email)
        Contact.__init__(name, email)
        AddressHolder.__init__(street, city, state, code)
        self.phone = phone