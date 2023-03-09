import streamlit as st

def printHelloWorld():
    print("Hello World")

st.title('Uber Pickups in New York City')
st.markdown('# Header')

if st.button('Say hello'):
    st.write('Why hello there')
    printHelloWorld()
else:
    st.write('Goodbye')