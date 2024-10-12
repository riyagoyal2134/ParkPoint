import streamlit as st
import openai

# Title of the form
st.title("Parking Office Questionnaire")

# Question 1: Parking Usage
parking_usage = st.selectbox(
    "How frequently do you use the parking facilities?",
    ("Daily", "Weekly", "Occ asionally")
)

# Question 2: Parking Location Preferences
parking_location = st.text_input(
    "Do you have a preferred parking location (e.g., near your office, close to the entrance, or any specific lot)?"
)

# Question 3: Parking Permit Type
permit_type = st.selectbox(
    "What type of parking permit do you currently have?",
    ("General", "Reserved", "Employee", "Visitor", "Other")
)

# Question 4: Peak Parking Times
peak_time = st.selectbox(
    "During what times of the day do you typically need parking?",
    ("Morning", "Afternoon", "Evening", "Varies")
)

# Question 5: Accessibility Needs
accessibility_needs = st.text_input(
    "Do you have any specific accessibility requirements for parking (e.g., handicap parking or proximity to building entrances)?"
)

# Question 6: Complaints or Issues
complaints = st.text_area(
    "Have you experienced any issues with parking availability, lot access, or parking management? If so, please describe them."
)

# Question 7: Parking Cost
cost_satisfaction = st.selectbox(
    "Are you satisfied with the cost of parking permits or daily rates?",
    ("Yes", "No")
)

cost_feedback = st.text_area(
    "If not, what changes would you like to see regarding parking costs?"
)

# Question 8: Electric Vehicles
ev_needs = st.selectbox(
    "Do you need or prefer parking spots with electric vehicle (EV) charging stations?",
    ("Yes", "No", "Not Applicable")
)

# Question 9: Future Parking Needs
future_needs = st.text_area(
    "Do you foresee any changes in your parking needs in the near future (e.g., additional vehicles, change in commuting habits)?"
)

# Submit button
if st.button("Submit"):
    st.write("Thank you for your responses!")
    
    # Display the collected data
    st.write("Your parking usage:", parking_usage)
    st.write("Preferred parking location:", parking_location)
    st.write("Parking permit type:", permit_type)
    st.write("Peak parking times:", peak_time)
    st.write("Accessibility needs:", accessibility_needs)
    st.write("Complaints or issues:", complaints)
    st.write("Satisfaction with parking cost:", cost_satisfaction)
    st.write("Feedback on parking cost:", cost_feedback)
    st.write("Electric vehicle needs:", ev_needs)
    st.write("Future parking needs:", future_needs)