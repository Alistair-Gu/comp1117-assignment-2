def ride_fare(card_type, full_fare, follows_ride):
    # Apply the card-type rule first
    if card_type == 1:
        fare = full_fare
    elif card_type == 2:
        fare = full_fare / 2
    elif card_type == 3:
        if full_fare < 2:
            fare = full_fare
        else:
            fare = 2
    
    # Then apply the interchange discount
    if follows_ride and fare >= 1:
        fare = fare - 1
    
    return fare

def can_ride(balance, fare):
    if balance > 0 and balance - fare >= -35:
        return True
    else:
        return False


def can_top_up(balance, amount):
    # Condition 1: amount must be a multiple of 50
    if amount % 50 != 0:
        return False
    
    # Condition 2: amount must be from 50 to 1000
    if amount < 50 or amount > 1000:
        return False
    
    # Condition 3: balance after adding must be 3000 or less
    if balance + amount > 3000:
        return False
    
    # All three conditions passed
    return True

def transaction_history(transactions):
    # Prints each recorded transaction in order. Returns nothing.
    pass  # your code here


def main():
    # main() is yours to write, by working it out with the AI assistant.
    # Some things it will need to do:
    #   - keep track of the balance, whether the last transaction was an
    #     accepted ride, and the transaction history
    #   - read transactions until the input ends
    #   - for each transaction, decide what to do, using your first three functions
    #   - print the summary and call transaction_history at the end
    pass


main()  # Don't change this
