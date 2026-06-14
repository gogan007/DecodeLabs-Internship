import streamlit as st

def main():
    st.title("💸 Expense Tracker")
    st.write("Type in an amount to add it to your running total.")
    
    # 1 --> State Initialization
    if "total_spent" not in st.session_state:
        st.session_state.total_spent = 0.0
        
    # Bonus: Let's also create a list to keep track of individual transactions!
    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    st.write("---")
    
    # 2 --> THE ENGINE
    # Putting the input box and button side-by-side
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # INPUT: The Gate
        user_input = st.text_input("Enter an expense amount (Rs.):", key="expense_input")
        
    with col2:
        st.write("") 
        st.write("") # Spacing to align the button
        
        if st.button("Add Expense"):
            if user_input:
                # PROCESS: The Engine
                try:
                    # String to Float for decimals
                    expense = float(user_input) 
                    
                    # Accumulator
                    st.session_state.total_spent += expense
                    st.session_state.transactions.append(expense)
                    
                    st.success(f"Added Rs.{expense:.2f}!")
                    
                except ValueError:
                    # Defensive Programming (Digital Poka-Yoke)
                    st.error("Invalid Data! Please enter a valid number.")

    # 3 --> OUTPUT (The Dashboard)
    st.write("\n****************************************")
    
    # Calculation using METRIC widget
    st.metric(label="FINAL TOTAL SPENT", value=f"Rs. {st.session_state.total_spent:.2f}")
    
    st.write("******************************************")
    
    # Displaying the history of what was added
    if st.session_state.transactions:
        st.write("**Transaction History:**")
        for i, val in enumerate(reversed(st.session_state.transactions)):
            st.write(f"- Rs. {val:.2f}")
            
        # For Reset the Records or History
        if st.button("Reset Tracker"):
            st.session_state.total_spent = 0.0
            st.session_state.transactions = []
            st.rerun()

# The Gatekeeper
if __name__ == "__main__":
    main()