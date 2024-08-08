import streamlit as st

# Inject the GTM script that usually goes in the <head> section
st.markdown("""
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-MZRJSLKK');</script>
    <!-- End Google Tag Manager -->
    """, unsafe_allow_html=True)

# Inject the GTM noscript that usually goes right after the <body> tag
st.markdown("""
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MZRJSLKK"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    """, unsafe_allow_html=True)

# Your Streamlit app content
st.title("My Streamlit App with Google Tag Manager")
st.write("This is a sample app with GTM integrated.")
