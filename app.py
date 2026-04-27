import streamlit as st

st.set_page_config(
    page_title="Dhakoli Flats | Old Ambala Road Property | 2/3 BHK Zirakpur", 
    page_icon="🏠",
    layout="centered",
    menu_items={
        'About': "Dhakoli & Old Ambala Road ke RERA Approved Flats. Call 8968744684"
    }
) 

st.title("🏠 Dhakoli & Old Ambala Road - Premium Flats")
st.subheader("RERA Approved | Ready to Move | 80% Bank Loan")
st.write("📍 Dhakoli | Old Ambala Road - Chandigarh se 5 Min")

st.markdown("---")
st.subheader("Get Best Price + Floor Plan on WhatsApp")

with st.form("lead_form", clear_on_submit=True):
    name = st.text_input("Full Name*")
    phone = st.text_input("WhatsApp Number*")
    
    col1, col2 = st.columns(2)
    with col1:
        looking_for = st.multiselect("Looking For*", ["2 BHK", "3 BHK", "4 BHK", "Penthouse"])
    with col2:
        location = st.multiselect("Preferred Location*", ["Dhakoli", "Old Ambala Road"])
    
    budget = st.selectbox("Your Budget*", ["40-50 Lakh", "50-65 Lakh", "65-80 Lakh", "80 Lakh+"])
    timeline = st.selectbox("Buying Timeline*", ["Immediate - This Month", "1-3 Months", "3-6 Months", "Just Exploring"])
    requirement = st.text_area("Any Specific Requirement?", placeholder="Ex: Park facing, 3+ Parking, Near School/Mall")
    
    submitted = st.form_submit_button("🔥 Get Best Deal on WhatsApp")
    
    if submitted:
        if name and phone and looking_for and location:
            st.success(f"Thanks {name}! Humara expert 10 min me aapko call karega.")
            st.balloons()
            
            # Lead WhatsApp pe bhejne ka button - YE IMPORTANT HAI
            whatsapp_msg = f"New Dhakoli Lead:%0AName: {name}%0APhone: {phone}%0ALooking: {looking_for}%0ALocation: {location}%0ABudget: {budget}%0ATimeline: {timeline}"
            st.link_button("📲 Send Lead to My WhatsApp", f"https://wa.me/918968744684?text={whatsapp_msg}")
            
        else:
            st.error("Please fill all * fields")

st.markdown("---")
st.caption("✅ 100+ Families Shifted in Dhakoli | RERA: PBRERXXXX | Call: 8968744684")
