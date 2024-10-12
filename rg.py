import streamlit as st
import pandas as pd
from datetime import datetime

st.image('logi1.jpg', use_column_width=True)

# Sample data for parking spots
data = {
    'Spot ID': [1, 2, 3, 4, 5],
    'Location': ['Downtown', 'Uptown', 'Midtown', 'Airport', 'Stadium'],
    'Available': [True, False, True, True, False],
    'Price': [2.00, 2.50, 1.50, 3.00, 2.00],
    'Reports': [0, 2, 0, 1, 0]
}

# Create a DataFrame
parking_spots = pd.DataFrame(data)

# Function to display parking spots
def display_parking_spots():
    st.header("Available Parking Spots")
    for index, row in parking_spots.iterrows():
        st.subheader(f"Spot ID: {row['Spot ID']} - Location: {row['Location']}")
        if row['Available']:
            st.success("Available")
        else:
            st.error("Not Available")
        st.write(f"Price: ${row['Price']} per hour")
        st.write(f"Reports: {row['Reports']}")

# Function to report issues with parking spots
def report_issue(spot_id):
    # Increment the report count for the given spot
    parking_spots.loc[parking_spots['Spot ID'] == spot_id, 'Reports'] += 1
    st.success(f"Issue reported for Spot ID {spot_id}.")

# Main app function
def main():
    st.title("Not Smart Parking (NSP) App")
    
    # Display parking spots
    display_parking_spots()

    # Issue reporting section
    st.header("Report an Issue")
    spot_id = st.number_input("Enter Spot ID to report an issue:", min_value=1, max_value=5)
    
    if st.button("Report Issue"):
        report_issue(spot_id)

if __name__ == "__main__":
    main()
