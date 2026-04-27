import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Zirakpur Property Deals", page_icon="🏙️", layout="wide")

st.title("🏙️ Zirakpur Premium Property Deals")
st.subheader("VIP Road | Airport Road | Patiala Highway - Chandigarh se 10 Min")
st.caption("GMADA Approved | Ready to Move + Under Construction | 80% Bank Loan")

with st.form("lead_form", clear_on_submit=True):
    st.markdown("### Get Best Price + Floor Plan on WhatsApp")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name*")
        phone = st.text_input("WhatsApp Number*")
        budget = st.selectbox("Your Budget*",
            ["₹35L-₹50L", "₹50L-₹75L", "₹75L-₹1Cr", "₹1Cr-₹1.5Cr", "₹1.5Cr-₹2.5Cr", "₹2.5Cr+"])

    with col2:
        prop_type = st.multiselect("Looking For*",
            ["2BHK Flat", "3BHK Flat", "4BHK/Penthouse", "Shop/SCO", "Plot", "Kothi/Villa"])
        location = st.multiselect("Preferred Location*",
            ["VIP Road", "Airport Road", "Patiala Road", "Ambala-Chd Highway",
             "Peer Muchalla", "Dhakoli", "Gazipur", "Singhpura", "Any Prime Location"])
        timeline = st.selectbox("Buying Timeline*",
            ["Immediate - This Month", "Within 1-3 Months", "3-6 Months", "Just Exploring"])

    requirements = st.text_area("Any Specific Requirement?",
        placeholder="e.g., Ready to move, Park facing, 3+ Parking, Near School/Mall...")

    submitted = st.form_submit_button("🔥 GET FREE SITE VISIT + BEST DEALS", use_container_width=True, type="primary")

    if submitted:
        if name and phone and budget and prop_type and location:
            new_lead = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name, "Phone": phone,
                "Budget": budget, "Type": ", ".join(prop_type),
                "Location": ", ".join(location), "Timeline": timeline,
                "Requirements": requirements, "Status": "New Lead"
            }

            file = "zirakpur_leads.csv"
            if os.path.exists(file):
                df = pd.read_csv(file)
                df = pd.concat([df, pd.DataFrame([new_lead])], ignore_index=True)
            else:
                df = pd.DataFrame([new_lead])

            df.to_csv(file, index=False)
            st.success("✅ Done! Humare expert aapko 10 min me call karenge. Floor plans WhatsApp par bhej diye jaayenge.")
            st.balloons()
        else:
            st.error("Bhai sare * wale fields bhar do please")

st.divider()
st.subheader("🔒 Agent Dashboard - Zirakpur Leads")

if os.path.exists("zirakpur_leads.csv"):
    leads_df = pd.read_csv("zirakpur_leads.csv")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Leads", len(leads_df))
    with col2: st.metric("Hot Leads", len(leads_df[leads_df['Timeline'].str.contains('Immediate')]))
    with col3: st.metric("1Cr+ Budget", len(leads_df[leads_df['Budget'].str.contains('1Cr|1.5Cr|2.5Cr')]))
    with col4: st.metric("Today", len(leads_df[pd.to_datetime(leads_df['Timestamp']).dt.date == pd.Timestamp.now().date()]))
    st.dataframe(leads_df.sort_values("Timestamp", ascending=False), use_container_width=True, height=400)
    csv = leads_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download All Leads", csv, "Zirakpur_Leads.csv", "text/csv", use_container_width=True)
else:
    st.info("Abhi tak koi lead nahi aayi. Facebook ad chalaoge to yahan dikhne lagenge.")