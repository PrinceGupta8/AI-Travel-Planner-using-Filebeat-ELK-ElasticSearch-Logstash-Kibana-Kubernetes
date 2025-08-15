import streamlit as st
from src.planner import TravelPlanner
from dotenv import load_dotenv
load_dotenv()

with st.form("planner_form"):
    city=st.text_input("Enter your city name for your trip")
    interests=st.text_input("Enter your interest (comma-separated)")
    submitted=st.form_submit_button("Generate Itinary")

    if submitted:
        if city and interests:
            planner=TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinary=planner.create_itinary()

            st.subheader("Your Itinary : ")
            st.markdown(itinary)
        else:
            st.warning("Please fill city and interests to move forward")
