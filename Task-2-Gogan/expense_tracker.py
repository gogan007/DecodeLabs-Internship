def main():
    print("--- DecodeLabs Expense Tracker ---")
    print("Type 'quit' at any time to stop and see your total.\n")
    
    # 1 --> State Initialization
    total_spent = 0.0 
    
    # 2 --> Continous Audit loop
    while True:
        # INPUT: The Gate
        user_input = input("Enter an expense amount (or 'quit'): ")
        
        #
        if user_input.lower() == 'quit':
            break
            
        # PROCESS: The Engine
        try:
            # String to Float for decimals
            expense = float(user_input) 
            
            # Accumulator
            total_spent += expense
            print(f"Added! Current running total: Rs.{total_spent:.2f}\n")
            
        except ValueError:
            # Defensive Programming
            print("Invalid Data! Please enter a valid number.\n")

    # 3. OUTPUT
    print("\n****************************************")
    print(f"FINAL TOTAL SPENT: Rs.{total_spent:.2f}")
    print("****************************************")

# The Gatekeeper
if __name__ == "__main__":
    main()