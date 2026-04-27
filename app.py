import streamlit as st

st.set_page_config(page_title="Dhakoli Property Deals", page_icon="🏠", layout="centered")

st.title("🏠 Dhakoli & Old Ambala Road - Premium Flats")
st.subheader("RERA Approved | Ready to Move | 80% Bank Loan")
st.write("📍 *Dhakoli* | *Old Ambala Road* - Chandigarh se 5 Min")

st.markdown("---")
st.subheader("Get Best Price + Floor Plan on WhatsApp")

with st.form("lead_form"):
    name = st.text_input("Name*")
    phone = st.text_input("WhatsApp Number*")
    
    col1, col2 = st.columns(2)
    with col1:
        looking_for = st.multiselect("Looking For*", ["2 BHK", "3 BHK", "4 BHK", "Penthouse"])
    with col2:
        location = st.multiselect("Preferred Location*", ["Dhakoli", "Old Ambala Road"])
    
    budget = st.selectbox("Budget*", ["40-50 Lakh", "50-65 Lakh", "65-80 Lakh", "80 Lakh+"])
    timeline = st.selectbox("Buying Timeline*", ["Immediate - This Month", "1-3 Months", "3-6 Months", "Just Exploring"])
    requirement = st.text_area("Any Specific Requirement?", placeholder="Ex: Park facing, 3+ Parking, Near School/Mall")
    
    submitted = st.form_submit_button("🔥 Get Best Deal on WhatsApp")
    
    if submitted:
        if name and phone and looking_for and location:
            st.success(f"Thanks {name}! Humara expert 10 min me aapko call karega.")
            st.balloons()
            # Yahan Google Sheet ka code add karna hai - main baad me bataunga
        else:
            st.error("Please fill all * fields")

st.markdown("---")
st.caption("✅ 100+ Families Shifted in Dhakoli | RERA: PBRERXXXX | Call: 7696998090")
