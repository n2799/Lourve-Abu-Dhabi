from Ticket import Ticket

class SpecialEvent(Ticket):
    def __init__(self, ticket_id, event, visitor, price, event_type):
        super().__init__(ticket_id, event, visitor, price)
        self.event_type = event_type

    def get_event_details(self):
        return f"Event Type: {self.event_type}, Ticket Price: {self.price}"
