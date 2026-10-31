import streamlit as st

st.set_page_config(page_title="Deal Poster AI", layout="centered")

st.title("🚀 Deal Hunter & Auto-Poster")

keyword = st.text_input("Product Category / Keyword:", placeholder="e.g. Best smartwatch under 2000")

if st.button("Generate Deal Post"):
    with st.spinner("Finding best deal..."):
        st.session_state['ready'] = True
        st.session_state['title'] = "Noise ColorFit Pulse 2 Max Smartwatch"
        st.session_state['deal_price'] = "₹1,499 (Flat 70% Off)"
        st.session_state['caption'] = "🔥 Loot Deal! Noise Smartwatch at lowest price ever. Battery up to 10 days, 1.85'' display.\n\nGrab here: https://earnkaro.com/example"
        st.session_state['image_url'] = "https://placehold.co/600x400/png?text=Smartwatch+Offer"

if st.session_state.get('ready'):
    st.subheader("📋 Review & Approval")
    st.image(st.session_state['image_url'], caption="AI Generated Image")
    st.write(f"**Product:** {st.session_state['title']}")
    st.write(f"**Price:** {st.session_state['deal_price']}")
    
    caption_box = st.text_area("Caption & EarnKaro Link:", st.session_state['caption'], height=120)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Approve & Post Now"):
            st.success("Boom! Telegram, Insta aur FB par upload ho gaya! 🎉")
    with col2:
        if st.button("❌ Reject / Cancel"):
            st.warning("Post cancel kar diya gaya.")
            st.session_state['ready'] = False
