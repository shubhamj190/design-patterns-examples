# consolidating all the processing strategy using abstractclass/interface

import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketProcessStrategy(ABC):
    @abstractmethod
    def strategy(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOStrategy(TicketProcessStrategy):
    def strategy(self, list: List[SupportTicket]) ->  List[SupportTicket]:
        return list.copy()


class FILOStategy(TicketProcessStrategy):
    def strategy(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class RandomStrategey(TicketProcessStrategy):
    def strategy(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class CustomerSupport:
    def __init__(self, processing_strategy: TicketProcessStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        """
            getting the stratigist ticket liist
        """

        ticket_list=self.processing_strategy.strategy(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
# s=FIFOStrategy()
s=FILOStategy()
app = CustomerSupport(s)

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
