import json

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"{self.name} / {self.email or 'None'} / {self.phone or 'None'}"

class Lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"{self.name or 'None'} / {self.email or 'None'} / {self.phone or 'None'}"

# Given data
contacts = [
    Contact("Alice Brown", None, "1231112223"),
    Contact("Bob Crown", "bob@crowns.com", None),
    Contact("Carlos Drew", "carl@drewess.com", "3453334445"),
    Contact("Doug Emerty", None, "4564445556"),
    Contact("Egan Fair", "eg@fairness.com", "5675556667"),
]

leads = [
    Lead(None, "kevin@keith.com", None),
    Lead("Lucy", "lucy@liu.com", "3210001112"),
    Lead("Mary Middle", "mary@middle.com", "3331112223"),
    Lead(None, None, "4442223334"),
    Lead(None, "ole@olson.com", None),
]

registrants_json = [
    '{"registrant": {"name": "Lucy Liu", "email": "lucy@liu.com", "phone": null}}',
    '{"registrant": {"name": "Doug", "email": "doug@emmy.com", "phone": "4564445556"}}',
    '{"registrant": {"name": "Uma Thurman", "email": "uma@thurs.com", "phone": null}}'
]

# Parse registrants
registrants = [json.loads(r)["registrant"] for r in registrants_json]

def process_registration(registrant):
    global contacts, leads
    email, phone, name = registrant["email"], registrant["phone"], registrant["name"]

    # 1. Match by email in contacts
    for contact in contacts:
        if contact.email == email:
            return  # Already in contacts

    # 2. Match by phone in contacts
    for contact in contacts:
        if contact.phone == phone:
            return  # Already in contacts

    # 3. Match by email in leads
    for lead in leads:
        if lead.email == email:
            contacts.append(Contact(name, email, phone))  # Move lead to contacts
            leads.remove(lead)
            return

    # 4. Match by phone in leads
    for lead in leads:
        if lead.phone == phone:
            contacts.append(Contact(name, email, phone))
            leads.remove(lead)
            return

    # 5. If no match, add as new contact
    contacts.append(Contact(name, email, phone))

# Process each registrant
for registrant in registrants:
    process_registration(registrant)

# Print final contacts
print("Updated Contacts List:")
for contact in contacts:
    print(contact)
