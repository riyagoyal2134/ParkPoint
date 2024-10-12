import streamlit as st
import pandas as py
import streamlit as st

# Set the page title
#st.set_page_config(page_title="ParkPoint", layout="wide")
st.set_page_config(page_title="ParkPoint", layout="centered")
st.title("Welcome to ParkPoint")
# Create a container to hold the columns and center them
st.empty()
st.empty()
st.balloons()
#comments to schange the layout
with st.container(): 
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])  # Equal width for both columns

    # Column for buttons
    with col1:
        st.subheader("Log into your ParkPoint account")
        # Sign In button
        if st.button("Sign In"):
            st.session_state.signin_mode = True
            st.session_state.create_account_mode = False

        # Create Account button
        if st.button("Create Account"):
            st.session_state.signin_mode = False
            st.session_state.create_account_mode = True
    # Column for sign in and create account forms
    with col2:
        if 'signin_mode' in st.session_state and st.session_state.signin_mode:
            
            
            # Ask if the user wants to monitor accounts or create a user account
            monitor_choice = st.radio("Do you want to:", ("Monitor Accounts", "User Account"))
            if monitor_choice:
                st.write(f"You selected: {monitor_choice}")

        if 'create_account_mode' in st.session_state and st.session_state.create_account_mode:
            st.subheader("Create Account")
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type='password')
            confirm_password = st.text_input("Confirm Password", type='password')
            
            # Ask if the user wants to monitor accounts or create a user account
            monitor_choice = st.radio("Do you want to:", ("Monitor Accounts", "User Account"))
            if monitor_choice:
                st.write(f"You selected: {monitor_choice}")

            # Button to submit account creation
            create_account_button = st.button(label='Create Account')
            if create_account_button:
                if new_password == confirm_password:
                    # Placeholder for account creation logic
                    st.success(f"Account for {new_username} created successfully!")
                else:
                    st.error("Passwords do not match!")


# Your app content goes here
if not ('signin_mode' in st.session_state or 'create_account_mode' in st.session_state):
    st.write("This is where your app content will be displayed when not in sign-in or account creation mode.")

