class Visitor:
    def __init__(self, name, age, ticket_type):
        self.name = name
        self.age = age
        self.ticket_type = ticket_type
        
    def purchase_ticket(self):
        pass

    def get_demographics(self):
        return f"Name: {self.name}, Age: {self.age}, Ticket Type: {self.ticket_type}"
