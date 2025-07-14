import streamlit as st

st.title("🚀 Test App")

students = [
    {"Name": "POORVA BETWAR", "Roll Number": "1"},
    {"Name": "KHUSHI BHATIA", "Roll Number": "2"},
]

for s in students:
    st.toggle(f"{s['Name']} ({s['Roll Number']})", key=s['Roll Number'])

st.success("App loaded fine.")
