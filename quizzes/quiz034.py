class FLIGHT:
    def __init__(self, flight_number, num_seat_business, num_seat_economy, ticket_price_economy, ticket_price_business):
        self.flight_number = flight_number
        self.num_seat_economy = num_seat_economy
        self.num_seat_business = num_seat_business
        self.ticket_price_economy = ticket_price_economy
        self.ticket_price_business = ticket_price_business

        self.economy_profit = None
        self.business_profit = None

    def get_profit_economy(self):
        self.economy_profit = self.num_seat_economy * self.ticket_price_economy

    def get_profit_business(self):
        self.business_profit = self.num_seat_business * self.ticket_price_business
