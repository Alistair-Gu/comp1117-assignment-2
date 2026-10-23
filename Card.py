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
    number = 1
    for kind, accepted, balance_after in transactions:
        if kind == 1:
            transaction_type = "Ride"
        else:
            transaction_type = "Top-up"
        
        if accepted:
            status = "accepted"
        else:
            status = "refused"
        
        balance_str = "{:.2f}".format(balance_after)
        print(f"{number}: {transaction_type} {status}. Balance: {balance_str}")
        number = number + 1


def main():
    # Read card type
    card_type = int(input("Card type (1 adult, 2 student, 3 elder): "))
    
    # Read starting balance
    balance = float(input("Starting balance: "))
    
    # Track state
    follows_ride = False
    transactions = []
    rides_taken = 0
    top_ups = 0
    fares_paid = 0
    lowest_balance = balance
    refused = 0
    
    # Process transactions
    while True:
        kind = int(input("Transaction (1 ride, 2 top-up, 0 stop): "))
        if kind == 0:
            break
        
        if kind == 1:
            # Ride
            amount = int(input("Amount: "))
            fare = ride_fare(card_type, amount, follows_ride)
            
            if can_ride(balance, fare):
                # Accepted ride
                balance = balance - fare
                rides_taken = rides_taken + 1
                fares_paid = fares_paid + fare
                follows_ride = True
                transactions.append((1, True, balance))
            else:
                # Refused ride
                refused = refused + 1
                follows_ride = False
                transactions.append((1, False, balance))
        
        elif kind == 2:
            # Top-up
            amount = int(input("Amount: "))
            
            if can_top_up(balance, amount):
                # Accepted top-up
                balance = balance + amount
                top_ups = top_ups + 1
                follows_ride = False
                transactions.append((2, True, balance))
            else:
                # Refused top-up
                refused = refused + 1
                follows_ride = False
                transactions.append((2, False, balance))
        
        # Update lowest balance
        if balance < lowest_balance:
            lowest_balance = balance
    
    # Determine card type name
    if card_type == 1:
        card_name = "adult"
    elif card_type == 2:
        card_name = "student"
    else:
        card_name = "elder"
    
    # Print summary
    print("Card type:", card_name)
    print("Rides taken:", rides_taken)
    print("Top-ups:", top_ups)
    print("Fares paid:", "{:.2f}".format(fares_paid))
    print("Lowest balance:", "{:.2f}".format(lowest_balance))
    print("Final balance:", "{:.2f}".format(balance))
    print("Refused:", refused)
    
    # Print transaction history
    transaction_history(transactions)


main()  # Don't change this
