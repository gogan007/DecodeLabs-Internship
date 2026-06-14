import streamlit as st

def main():
    st.title("---- TO DO List ----")
    st.write("DecodeLabs Intern Web App")
    
    # initialize the session state memory if it doesn't exist yet
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    st.subheader("1. Add Task")
    
    # create an input box and an add button side-by-side
    col1, col2 = st.columns([3, 1])
    with col1:
        new_task = st.text_input("Enter your task:", key="task_input")
    with col2:
        # vertical spacing to align the button with the text box
        st.write("") 
        st.write("")
        if st.button("Add"):
            if new_task:
                # add to session state memory instead of a normal list
                st.session_state.tasks.append(new_task)
                st.success("Task added!")
                st.rerun()  # refresh the app instantly
            else:
                st.warning("Please enter a valid task.")

    st.subheader("2. Your Tasks")
    
    # check if the list is empty
    if len(st.session_state.tasks) == 0:
        st.info("No tasks available.")
    else:
        # loop through tasks and create a remove button for each
        for i, t in enumerate(st.session_state.tasks):
            colA, colB = st.columns([4, 1])
            with colA:
                st.write(f"**{i + 1}.** {t}")
            with colB:
                # use the index as a unique key for each button
                if st.button("Remove", key=f"remove_{i}"):
                    st.session_state.tasks.pop(i)
                    st.rerun()  # refresh the app instantly

# program entry point
if __name__ == "__main__":
    main()