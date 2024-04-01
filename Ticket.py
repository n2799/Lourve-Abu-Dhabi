class Ticket:
    def __init__(self, ticket_id, event, visitor, price):
        self.ticket_id = ticket_id
        self.event = event
        self.visitor = visitor
        self.price = price
        
    def generate_ticket(self):
        pass

    def calculate_price(self):
        pass
