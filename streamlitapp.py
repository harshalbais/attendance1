import streamlit as st
from docx import Document
from io import BytesIO

# Cached list of students
@st.cache_data
def get_students():
    return [
    {"Name": "POORVA BETWAR", "Roll Number": "1"},
    {"Name": "KHUSHI BHATIA", "Roll Number": "2"},
    {"Name": "BHUMI BOMEWAR", "Roll Number": "3"},
    {"Name": "CHAITANYA PISE", "Roll Number": "4"},
    {"Name": "THORAVI DAF", "Roll Number": "5"},
    {"Name": "RUTUJA DESHMUKH", "Roll Number": "6"},
    {"Name": "MRUGAKSHI FULZELE", "Roll Number": "7"},
    {"Name": "KAMAKSHI HANVAT", "Roll Number": "8"},
    {"Name": "HARSHITA DAYMA", "Roll Number": "9"},
    {"Name": "TANVI HONADE", "Roll Number": "10"},
    {"Name": "SAYALI JIBHAKATE", "Roll Number": "11"},
    {"Name": "SHRUTI KOSURKAR", "Roll Number": "12"},
    {"Name": "PRIYANKA PARATE", "Roll Number": "13"},
    {"Name": "VRUSHALI PARATKAR", "Roll Number": "14"},
    {"Name": "SANSKRUTI RAUT", "Roll Number": "15"},
    {"Name": "NOOPUR SELOKAR", "Roll Number": "16"},
    {"Name": "NAKSHATRA SHARMA", "Roll Number": "17"},
    {"Name": "APURVA TONGE", "Roll Number": "18"},
    {"Name": "RAKHI VERMA", "Roll Number": "19"},
    {"Name": "GAURI YADAV", "Roll Number": "20"},
    {"Name": "SUHANI YADAV", "Roll Number": "21"},
    {"Name": "ADITYA TIWARI", "Roll Number": "22"},
    {"Name": "HARSH AGREY", "Roll Number": "23"},
    {"Name": "ABHISHEK AKHAND", "Roll Number": "24"},
    {"Name": "VARDHAN ANDRASKAR", "Roll Number": "25"},
    {"Name": "TUSHAR BAGHELE", "Roll Number": "26"},
    {"Name": "HARSHAL BAIS", "Roll Number": "27"},
    {"Name": "TANAY BANAIT", "Roll Number": "28"},
    {"Name": "SAGAR BANDAWAR", "Roll Number": "29"},
    {"Name": "ANIRUDDHA BANGRE", "Roll Number": "30"},
    {"Name": "SARTHAK BANKAR", "Roll Number": "31"},
    {"Name": "BHAVESH BARGAT", "Roll Number": "32"},
    {"Name": "ANUJ BARLAWAR", "Roll Number": "33"},
    {"Name": "MANTHAN BELEKAR", "Roll Number": "34"},
    {"Name": "DURGESH BHAGAT", "Roll Number": "35"},
    {"Name": "BHUVAN BHIOGADE", "Roll Number": "36"},
    {"Name": "RUSHIKESH BURDE", "Roll Number": "37"},
    {"Name": "SUJAY DAS", "Roll Number": "38"},
    {"Name": "DIVYA BANGDE", "Roll Number": "39"},
    {"Name": "ABHISHEK FALTANKAR", "Roll Number": "40"},
    {"Name": "SOHAM GAIKWAD", "Roll Number": "41"},
    {"Name": "ANAND HATMODE", "Roll Number": "42"},
    {"Name": "KAPIL HOKARNE", "Roll Number": "43"},
    {"Name": "ADESH INGLE", "Roll Number": "44"},
    {"Name": "ADARSH JAISWAL", "Roll Number": "45"},
    {"Name": "KAPUR PARDHI", "Roll Number": "46"},
    {"Name": "KUSHAL MEHAR", "Roll Number": "47"},
    {"Name": "SHREE LAROKAR", "Roll Number": "48"},
    {"Name": "VEDANT MESHRAM", "Roll Number": "49"},
    {"Name": "OM MALEWAR", "Roll Number": "50"},
    {"Name": "PRANAV VALLUVAR", "Roll Number": "51"},
    {"Name": "MORESHWAR PACHBHAI", "Roll Number": "52"},
    {"Name": "OM PATIL", "Roll Number": "53"},
    {"Name": "KUNAL RAHANGDALE", "Roll Number": "54"},
    {"Name": "ATHANG RAMTEKE", "Roll Number": "55"},
    {"Name": "KRISHNA SAHU", "Roll Number": "56"},
    {"Name": "SAURABH SHARMA", "Roll Number": "57"},
    {"Name": "AYAN SHEIKH", "Roll Number": "58"},
    {"Name": "HIMANSHU SHUKLA", "Roll Number": "59"},
    {"Name": "ARYA SINGANJUDE", "Roll Number": "60"},
    {"Name": "VINEET SINGH", "Roll Number": "61"},
    {"Name": "ADITYA TEMBHARE", "Roll Number": "62"},
    {"Name": "ATUL THAKRE", "Roll Number": "63"},
    {"Name": "YUVRAJ THAKRE", "Roll Number": "64"},
    {"Name": "CHANDRAKANT THAKUR", "Roll Number": "65"},
    {"Name": "ANSHUL UMBARKAR", "Roll Number": "66"},
    {"Name": "UTKARSH SONSARE", "Roll Number": "67"},
    {"Name": "VAIBHAV ENAME", "Roll Number": "68"},
    {"Name": "VAISHALI STUDDEDU", "Roll Number": "69"},
    {"Name": "VIRAJ WANKHADE", "Roll Number": "70"}
]

students = get_students()

st.set_page_config(page_title="Class Attendance", layout="centered")
st.title("📋 Class Attendance")

present_students = []
absent_students = []

with st.form("attendance_form"):
    st.subheader("Mark Attendance")
    for student in students:
        is_present = st.toggle(f"{student['Name']} ({student['Roll Number']})", value=True, key=student['Roll Number'])
        if is_present:
            present_students.append(student)
        else:
            absent_students.append(student)

    submitted = st.form_submit_button("✅ Submit Attendance")

# Only after form is submitted
if submitted:
    doc = Document()
    doc.add_heading('Attendance Report', 0)

    doc.add_paragraph('✅ Present Students:')
    for s in present_students:
        doc.add_paragraph(f"{s['Roll Number']}. {s['Name']}", style='List Bullet')

    doc.add_paragraph('\n❌ Absent Students:')
    for s in absent_students:
        doc.add_paragraph(f"{s['Roll Number']}. {s['Name']}", style='List Bullet')

    # Create Word file in memory
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.success("✅ Attendance report generated!")
    st.download_button("📄 Download Attendance Report (Word)", data=buffer, file_name="Attendance_Report.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
