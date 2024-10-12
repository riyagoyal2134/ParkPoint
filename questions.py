import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to get suggestions from OpenAI
def get_chatgpt_suggestions(responses):
    prompt = f"""
    Based on the following user responses related to parking:
    1. Parking Usage: {responses['parking_usage']}
    2. Preferred Parking Location: {responses['parking_location']}
    3. Parking Permit Type: {responses['permit_type']}
    4. Peak Parking Times: {responses['peak_time']}
    5. Accessibility Needs: {responses['accessibility_needs']}
    6. Complaints or Issues: {responses['complaints']}
    7. Satisfaction with Parking Cost: {responses['cost_satisfaction']}
    8. Feedback on Parking Cost: {responses['cost_feedback']}
    9. Electric Vehicle Needs: {responses['ev_needs']}
    10. Future Parking Needs: {responses['future_needs']}
    
    Please provide suggestions for improving parking services and user experience.
    """

    # Updated API call for chat completion
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or use "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are an expert assistant for improving parking services."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    # Extract and return the message from OpenAI
    return response['choices'][0]['message']['content'].strip()

# Streamlit UI
st.title("Parking Feedback and Suggestions")

st.write("Please fill out the form to help us improve parking services.")

# Create a form for user inputs
with st.form(key='parking_form'):
    parking_usage = st.selectbox("How often do you use parking?", ["Daily", "Weekly", "Occasionally"])
    parking_location = st.text_input("Preferred Parking Location", "e.g., Near office entrance")
    permit_type = st.selectbox("What type of parking permit do you use?", ["General", "VIP", "Temporary"])
    peak_time = st.selectbox("When do you most frequently park?", ["Morning", "Afternoon", "Evening", "Night"])
    accessibility_needs = st.selectbox("Do you have any accessibility needs?", ["No", "Yes"])
    complaints = st.text_area("Do you have any complaints or issues with parking?", "e.g., Sometimes there are no spots available.")
    cost_satisfaction = st.selectbox("Are you satisfied with the parking cost?", ["Yes", "No"])
    cost_feedback = st.text_area("Do you have any feedback regarding parking costs?", "e.g., Lower the cost for general permits.")
    ev_needs = st.selectbox("Do you need electric vehicle (EV) charging stations?", ["No", "Yes"])
    future_needs = st.text_area("Any future parking needs?", "e.g., More EV stations, larger parking spots.")

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# If the user submits the form
if submit_button:
    # Store the user responses in a dictionary
    responses = {
        "parking_usage": parking_usage,
        "parking_location": parking_location,
        "permit_type": permit_type,
        "peak_time": peak_time,
        "accessibility_needs": accessibility_needs,
        "complaints": complaints,
        "cost_satisfaction": cost_satisfaction,
        "cost_feedback": cost_feedback,
        "ev_needs": ev_needs,
        "future_needs": future_needs
    }
    
    # Show the responses for verification
    st.write("Your responses:")
    st.json(responses)
    
    # Get suggestions from OpenAI based on user responses
    with st.spinner("Generating suggestions based on your input..."):
        suggestions = get_chatgpt_suggestions(responses)
    
    # Display the suggestions
    st.subheader("Parking Suggestions:")
    st.write(suggestions)