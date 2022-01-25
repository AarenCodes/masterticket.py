SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  


#create calculate_price function. Takes # tickets and returns value
# (number of tickets * 2) + (number of tickets * price)

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining > 0: 
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?    ")
    number_of_tickets = input("How many tickets would you like, {}?   ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("Sorry, there are only {} tickets remaining!".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, {} we ran into an issue. {} Please try again".format(name,err))
    else:
        total_cost = calculate_price(number_of_tickets)
        print("The total cost is ${}" .format(total_cost)) 
        prompt = input("Would you like to proceed, {}? \n Yes or No?" .format(name))
        if prompt.lower() == "yes":
            print("SOLD!, You bought {} tickets for {}.".format(number_of_tickets,total_cost))    
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you for consideration, {}!".format(name))
print("Sorry, tickets are all sold out.")

