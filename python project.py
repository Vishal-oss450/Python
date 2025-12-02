import streamlit as st
import sqlite3
import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


MY_EMAIL = "kaizoku7143@gmail.com" 

MY_APP_PASSWORD = "owkr iowt yblb seji" 

DB_NAME = "users_streamlit.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
   
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, email TEXT UNIQUE, role TEXT, is_restricted INTEGER)''')
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS profiles 
                 (email TEXT UNIQUE, name TEXT, roll_no TEXT, dob TEXT, 
                  semester TEXT, gender TEXT, mobile TEXT, address TEXT, attendance REAL)''')
    
   
    c.execute('SELECT count(*) FROM users')
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO users (email, role, is_restricted) VALUES (?, ?, ?)", 
                  (MY_EMAIL, 'admin', 0))
    conn.commit()
    conn.close()


def get_user(email):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    return c.fetchone()

def get_all_users_by_role(role):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if role == 'all':
        c.execute("SELECT * FROM users")
    else:
        c.execute("SELECT * FROM users WHERE role=?", (role,))
    return c.fetchall()

def add_user_to_db(email, role):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO users (email, role, is_restricted) VALUES (?, ?, 0)", (email, role))
        
        c.execute("INSERT OR IGNORE INTO profiles (email, attendance) VALUES (?, 0.0)", (email,))
        conn.commit()
        conn.close()
        return True
    except:
        return False

def delete_user_from_db(user_id, email):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    c.execute("DELETE FROM profiles WHERE email=?", (email,))
    conn.commit()
    conn.close()

def toggle_restriction_db(user_id, current_status):
    new_status = 0 if current_status == 1 else 1
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET is_restricted=? WHERE id=?", (new_status, user_id))
    conn.commit()
    conn.close()


def get_profile(email):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    c = conn.cursor()
    c.execute("SELECT * FROM profiles WHERE email=?", (email,))
    data = c.fetchone()
    conn.close()
    
    if data is None:
        return {"email": email, "name": "", "roll_no": "", "dob": "", "semester": "", 
                "gender": "", "mobile": "", "address": "", "attendance": 0.0}
    return dict(data)

def update_profile(email, name, roll, dob, sem, gender, mobile, address, attendance):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
   
    c.execute('''INSERT OR REPLACE INTO profiles 
                 (email, name, roll_no, dob, semester, gender, mobile, address, attendance) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
              (email, name, roll, dob, sem, gender, mobile, address, attendance))
    conn.commit()
    conn.close()


def send_real_email(recipient_email, otp_code):
    try:
        clean_password = MY_APP_PASSWORD.replace(" ", "")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(MY_EMAIL, clean_password)
        
        msg = MIMEMultipart()
        msg['From'] = MY_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = "Your Portal Login OTP"
        body = f"Hello,\n\nYour OTP is: {otp_code}\n\n"
        msg.attach(MIMEText(body, 'plain'))
        
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Email Error: {e}")
        return False


if 'page' not in st.session_state: st.session_state.page = 'login'
if 'auth_email' not in st.session_state: st.session_state.auth_email = ''
if 'otp_code' not in st.session_state: st.session_state.otp_code = ''

init_db()



def login_page():
    st.title("🎓 College Portal Login")
    
    email = st.text_input("Enter Email", value=MY_EMAIL)
    
    if st.button("Get OTP"):
        user = get_user(email)
        if user:
            user_id, u_email, role, restricted = user
            if restricted:
                st.error("Account Restricted.")
            else:
                otp = str(random.randint(1000, 9999))
                st.session_state.otp_code = otp
                st.session_state.auth_email = email
                
                with st.spinner('Sending OTP...'):
                    if send_real_email(email, otp):
                        st.success("OTP Sent!")
                        time.sleep(1)
                        st.session_state.page = 'verify_otp'
                        st.rerun()
        else:
            st.error("User not found in system.")

def verify_otp_page():
    st.title("🔐 Verify OTP")
    st.write(f"OTP sent to: {st.session_state.auth_email}")
    otp_input = st.text_input("Enter OTP")
    
    if st.button("Login"):
        if otp_input == st.session_state.otp_code:
            user = get_user(st.session_state.auth_email)
            st.session_state.current_user = user
           
            role = user[2] 
            if role == 'admin':
                st.session_state.page = 'admin_dashboard'
            elif role == 'teacher':
                st.session_state.page = 'teacher_dashboard'
            elif role == 'student':
                st.session_state.page = 'student_dashboard'
            st.rerun()
        else:
            st.error("Incorrect OTP")
    if st.button("Back"): st.session_state.page = 'login'; st.rerun()



def student_profile_form(target_email, can_edit_attendance, can_edit_info):
    """Reusable form for Student, Teacher, and Admin"""
    p = get_profile(target_email)
    
    st.markdown(f"### Profile: {target_email}")
    
    with st.form(f"form_{target_email}"):
        c1, c2 = st.columns(2)
        name = c1.text_input("Name", value=p['name'], disabled=not can_edit_info)
        roll = c2.text_input("Roll No", value=p['roll_no'], disabled=not can_edit_info)
        
        c3, c4 = st.columns(2)
        dob = c3.text_input("DOB (DD/MM/YYYY)", value=p['dob'], disabled=not can_edit_info)
        sem = c4.selectbox("Semester", ["1", "2", "3", "4", "5", "6", "7", "8"], 
                           index=(int(p['semester'])-1) if p['semester'] else 0, disabled=not can_edit_info)
        
        c5, c6 = st.columns(2)
        gender = c5.selectbox("Gender", ["Male", "Female", "Other"], 
                              index=0 if p['gender'] == "Male" else 1, disabled=not can_edit_info)
        mobile = c6.text_input("Mobile Number", value=p['mobile'], disabled=not can_edit_info)
        
        addr = st.text_area("Address", value=p['address'], disabled=not can_edit_info)
        
        st.divider()
        
        st.markdown("#### 📊 Attendance Record")
        if can_edit_attendance:
            att = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=float(p['attendance']))
            st.caption("You have permission to edit this.")
        else:
            
            att = float(p['attendance'])
            st.progress(int(att))
            st.write(f"**Current Attendance:** {att}%")
            
        if st.form_submit_button("Save Changes"):
            update_profile(target_email, name, roll, dob, sem, gender, mobile, addr, att)
            st.success("Profile Updated!")
            time.sleep(1)
            st.rerun()

def student_dashboard():
    st.title("👨‍🎓 Student Dashboard")
    user_email = st.session_state.auth_email
    
    if st.button("Logout"): st.session_state.page = 'login'; st.rerun()
    st.divider()
    
    st.info("You can edit your details, but Attendance is managed by your Teacher.")
    
    student_profile_form(user_email, can_edit_attendance=False, can_edit_info=True)

def teacher_dashboard():
    st.title("👩‍🏫 Teacher Dashboard")
    if st.button("Logout"): st.session_state.page = 'login'; st.rerun()
    st.divider()
    
    st.subheader("Select a Student to Manage")
    students = get_all_users_by_role('student')
    
    student_emails = [s[1] for s in students]
    
    if not student_emails:
        st.warning("No students found in the database.")
    else:
        selected_student = st.selectbox("Select Student Email", student_emails)
        st.divider()
        
        student_profile_form(selected_student, can_edit_attendance=True, can_edit_info=True)

def admin_dashboard():
    st.title("🛠️ Admin Dashboard")
    if st.button("Logout", type="primary"): st.session_state.page = 'login'; st.rerun()
    
    tab1, tab2 = st.tabs(["User Management", "Edit Student Profiles"])
    
   
    with tab1:
        st.subheader("Add New User")
        with st.form("add_u"):
            c1, c2 = st.columns(2)
            ne = c1.text_input("Email")
            nr = c2.selectbox("Role", ["student", "teacher", "admin"])
            if st.form_submit_button("Add User"):
                if add_user_to_db(ne, nr): st.success("User Added!")
                else: st.error("Failed/Duplicate")
                st.rerun()
                
        st.subheader("Existing Users")
        users = get_all_users_by_role('all')
        for u in users:
            uid, uemail, urole, ur = u
            c1, c2, c3, c4 = st.columns([1,2,1,2])
            c1.write(uid); c2.write(uemail)
            c3.markdown(f"**{urole.upper()}**")
            with c4:
                if st.button(f"{'Unrestrict' if ur else 'Restrict'}", key=f"r{uid}"):
                    toggle_restriction_db(uid, ur); st.rerun()
                if st.button("Delete", key=f"d{uid}"):
                    if uemail != MY_EMAIL: delete_user_from_db(uid, uemail); st.rerun()
    
    
    with tab2:
        st.write("Admin has full access to edit any student's data.")
        students = get_all_users_by_role('student')
        s_emails = [s[1] for s in students]
        if s_emails:
            sel_s = st.selectbox("Select Student to Edit", s_emails, key="adm_sel")
           
            student_profile_form(sel_s, can_edit_attendance=True, can_edit_info=True)
        else:
            st.info("Add student users first.")


if st.session_state.page == 'login': login_page()
elif st.session_state.page == 'verify_otp': verify_otp_page()
elif st.session_state.page == 'admin_dashboard': admin_dashboard()
elif st.session_state.page == 'teacher_dashboard': teacher_dashboard()
elif st.session_state.page == 'student_dashboard': student_dashboard()