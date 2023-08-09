
import streamlit as st
import joblib as job
model=job.load("Loan Approval")
st.title("Loan Approval")
st.header("Fill the details below::")
formbtn = st.button("Form")
if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False

if formbtn or st.session_state.formbtn_state:
    st.session_state.formbtn_state = True
    with st.form("form"):
      ID=st.text_input("Enter your LoanID::")
      gender=st.radio("Select your Gender::",("Male","Female"))
      if gender=='Male':
        gender=1
      else:
        gender=0
      mar=st.radio("Select your Marital Status::",("No","Yes"))
      if mar=="Yes":
        mar=1
      else:
        mar=0
      dep=st.selectbox("Number of Dependents::",('0','1','2','3+'))
      if dep=='3+':
        dep=4
      else:
        dep=int(dep)
      se_emp=st.radio("Are you Self_Employed?",("No","Yes"))
      if se_emp=="Yes":
        se_emp=1
      else:
        se_emp=0
      edu=st.radio("Are you a Graduate?",("Graduate","Not Graduate"))
      if edu=="Graduate":
        edu=0
      else:
        edu=1
      applicantincome=st.number_input("Enter your Income::")
      coapplicantincome=st.number_input("Enter your Co-Applicant Income::")
      loanamt=st.number_input("Enter the Loan Amount::")
      loanamtterm=st.number_input("Enter the Loan Amount Term::")
      credit=st.number_input("Enter your Credit History::")
      pro=st.radio("Select your Property Area::",("Urban","Rural","Semiurban"))
      if pro=="Rural":
        pro=0
      elif pro=="Semiurban":
        pro=1
      else:
        pro=2
      x=[[gender,mar,dep,edu,se_emp,applicantincome,coapplicantincome,loanamt,loanamtterm,credit,pro]]
      res=model.predict(x)
      submitted=st.form_submit_button("Submit")
      if submitted:
        if res=="Y":
          st.subheader("There is a possibility for your loan to get approved in the banks...")
        else:
          st.write("Unfortunately, there is no possibility for your loan to get approved with current bank conditions.\n You can contact us for help.")
