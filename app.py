import streamlit as st
import streamlit.components.v1 as components

# Google Tag Manager code for the <head> section
gtm_head_code = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MZRJSLKK');</script>
<!-- End Google Tag Manager -->
"""

# Google Tag Manager code for immediately after the opening <body> tag
gtm_body_code = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MZRJSLKK"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

# Inject the GTM code into the Streamlit app
components.html(gtm_head_code, height=0)
components.html(gtm_body_code, height=0)

# Your Streamlit app code
st.title("My Streamlit App with Google Tag Manager")
st.write("pawanmehra.streamlit.com test")
st.balloons()
