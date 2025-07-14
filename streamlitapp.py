import streamlit as st
from docx import Document
from io import BytesIO

@st.cache_data
def get_students():
    return [
        {"Name": "POORVA BETWAR", "Roll Number": "1"},
        {"Name": "KHUSHI BHATIA", "Roll Number": "2"},
        {"Name": "BHUMI BOMEWAR", "Roll Number": "3"},
        {"Name": "CHAITANYA PISE", "Roll Number": "4"},
        {"Name": "THORAVI DAF", "Roll Number": "5"},
        # 🔄 Add all remaining students here
    ]

def main():
    st.set_page_config(page_title="Class Attendance", layout="centered")
    st.title("📋 Class Attendance App")

    students = get_students()
    present_students = []
    absent_students = []

    with st.form("attendance_form"):
        st.subheader("Mark Attendance Below 👇")
        for student in students:
            is_present = st.toggle(f"{student['Name']} ({student['Roll Number']})", value=True, key=student['Roll Number'])
            if is_present:
                present_students.append(student)
            else:
                absent_students.append(student)

        submitted = st.form_submit_button("✅ Submit Attendance")

    if submitted:
        doc = Document()
        doc.add_heading('Attendance Report', 0)

        doc.add_paragraph('✅ Present Students:')
        for s in present_students:
            doc.add_paragraph(f"{s['Roll Number']}. {s['Name']}", style='List Bullet')

        doc.add_paragraph('\n❌ Absent Students:')
        for s in absent_students:
            doc.add_paragraph(f"{s['Roll Number']}. {s['Name']}", style='List Bullet')

        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        st.success("✅ Attendance report generated successfully!")
        st.download_button(
            "📄 Download Attendance Report (Word)",
            data=buffer,
            file_name="Attendance_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

# ✅ Entry point
if __name__ == "__main__":
    main()
