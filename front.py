import streamlit as st
import plotly.express as px
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="ParkPoint", layout="centered")
st.markdown('<style>body {background-color: #A9A9A9;}</style>', unsafe_allow_html=True)


# Logo

st.image("200w.gif")
st.image("logo.png", width=150)  # Adjust the width as needed
# Fancy Heading
st.markdown("<h1 style='text-align: center; color: #00796b; font-size: 3em; text-shadow: 2px 2px 4px #004d40;'>ParkPoint</h1>", unsafe_allow_html=True)

# Slogan
st.markdown("<h2 style='text-align: center; color: #00796b;'>P</h2>", unsafe_allow_html=True)



# Main content
st.markdown("""
Park anytime, anywhere at the convenience!
""")

# Custom CSS for styling
css = (
    "<style>"
    "@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');"  # Import Roboto font
    "body { background-color: 'gray'; margin: 0; font-family: 'Arial', sans-serif; }"  # Set background color to green
    ".container { display: flex; justify-content: center; align-items: center; flex-direction: column; padding: 40px; }"
    ".info { text-align: center; margin-top: 20px; font-size: 18px; color: #333; }"
    ".card { background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); margin: 20px; }"
    ".footer { text-align: center; margin-top: 40px; color: #fff; }"  # Change footer text color to white
    ".button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }"
    ".button:hover { background-color: #45a049; }"
    ".input-container { margin: 20px auto; max-width: 500px; }"
    "</style>"
)

st.markdown(css, unsafe_allow_html=True)

# Main container for features
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Button to show features
if st.button("Show Features", key="features_button"):
    st.markdown(
        "<div class='info'>"
        "<h3>Key Features of ParkPoint:</h3>"
        "<div class='card'>"
        "<ul style='list-style-type: none; padding: 0;'>"
        "<li> 🚗 <strong>Real-Time Parking Availability</strong></li>"
        "<li> 💰 <strong>Dynamic Pricing Models</strong></li>"
        "<li> 📊 <strong>Data Collection and Analytics</strong></li>"
        "<li> 🛡️ <strong>Valet Security Services</strong></li>"
        "<li> 📍 <strong>Car Mapping and Location Services</strong></li>"
        "</ul>"
        "</div>"
        "</div>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)  # Close the container div

# Interactive section for user feedback
st.markdown("<h3 style='text-align: center;'>Get Involved</h3>", unsafe_allow_html=True)

# Container for input fields
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
user_name = st.text_input("Enter your name:")
user_feedback = st.text_area("Share your thoughts or suggestions:")
if st.button("Submit Feedback", key="submit_feedback"):
    st.success(f"Thank you, {user_name}! Your feedback has been submitted.")
st.markdown("</div>", unsafe_allow_html=True) 

# Footer with hackathon branding
st.markdown(
    "<footer class='footer'>"
    "<p>Developed during HackHarvard 2024</p>"
    "</footer>",
    unsafe_allow_html=True
)
