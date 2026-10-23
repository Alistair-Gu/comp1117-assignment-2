# A2 Harbour Card: My Specifications

**Finish this file first, before any code is written.** You supply the
reasoning and fill in this worksheet in your own words, with the AI
assistant's help. It describes the problem only, not how your program will solve
it.

## Input and output types

What the program reads and what it prints, with the type of each value:
int, float, str, bool. Say why.

- **Inputs:** what values does the program read, in what order, and what
  type is each?
  1. card_type, int
  2. starting balance, float
  3. kind, int
  4. amount, int
      
- **Outputs:** what does the program print, what type is each value, and
  how are the money values printed?
  1. Card type, str
  2. rides taken, int
  3. top-ups, int
  4. fares paid, str
  5. lowest balance, str
  6. final balance, str
  7. refused, int
  money values are printed using "{:.2f}".format() to correct them to two decimal points.

## The rules in my own words

State each rule in your own words, not the assignment's wording pasted back.
For every boundary, write **both sides**: what happens exactly on it, and
what happens just past it.

  ### Card-type rules
  - Adult (1): fare = full fare
  - Student (2): fare = full fare / 2
  - Elder (3): fare = 2, or full fare if full fare < 2
  
  ### Interchange discount
  - If follows_ride is True AND fare >= 1:
      fare = fare - 1
  - A fare never goes below 0
  - The first transaction of the day never gets this discount
  
  ### Order
  1. Apply card type to get intermediate fare
  2. Apply interchange discount if applicable

- **When a ride is refused:**
  balance > 0 and balance - fare >= -35

- **When a top-up is refused:**
  amount % 50 != 0 or amount is not in the interval [50,1000] or balance + amount is larger than 3000
  
- **What a refused transaction changes, and what it does not:**
  It adds 1 to refused and change follows_ride to False (interchange discount cannot be applied to the next ride) and add that transaction to the transactions history.
  
- **The lowest balance:**
  At the beginning, the lowest_balance is equal to balance. If the balance after a transaction is lower than the previous lowest balance, update the lowest_balance to current balance.
  
- **The transaction history:** which transactions appear, their order and numbering, and what each line shows. How is this different from your chat history?
  All the transactions appeared no matter accepted or refused. They are in list order atarting from 1. Each line shows the numbering, the transaction kind (ride / top-up),whether it is accepted or refused, and the balance after that transaction. In the chat history, the AI returns basically the same thing except that it uses < > rather than complete sentences.

## Edge cases

The inputs where something special happens, and what the program must do in
each. For example: a ride straight after a refused ride, or a top-up that
lands exactly on 3000.
1. can_ride: balance <= 0 and it returns false; balance - fare >= -35 and it returns true.
2. can_top_up: amount % 50 != 0 or amount < 50 or amount > 1000 or balance + amount >3000 and it returns false
3. ride_fare: if the previous transaction is a top-up or a refused ride, the interchange discount does not apply. If the fare is smaller than 1, the discount does not apply too.

-
