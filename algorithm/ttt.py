import streamlit as st
# from mycomponent import mycomponent
# import streamlit.components.v1 as components
from streamlit.components.v1 import html

# value = mycomponent()
# st.write("Received", value)
st.sidebar.header('Lewy')
token_text = st.sidebar.text_input('aaa', key='eeee_api')
st.sidebar.text_input('bbb', key='bbbb_api')
st.sidebar.button('Add')

print(token_text)

html("<script>window.parent.document.getElementsByTagName('input')[0].onchange = function(){window.parent.document.getElementsByTagName('input')[0].value = window.parent.document.location.href;}</script>")
html("<script>window.parent.document.getElementsByTagName('input')[0].value = window.parent.document.location.href</script>")
# html("<script>window.parent.setTimeout(function() { window.parent.document.getElementsByTagName('input')[0].value = window.parent.document.location.href }, 0)</script>")
# st.sidebar.markdown("<script>document.getElementsByTagName('input')[0].value = 'www'</script>", unsafe_allow_html=True)
# html("<script>document.getElementsByTagName('input')[0].value = 'www'</script>")