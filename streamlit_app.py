import streamlit as st
st.markdown("# Hello")
st.markdown("## Hello")
st.header("It is a header")
st.subheader("It is a subheader")
st.text("It is a text")
st.caption("It is a Caption")
st.latex("x^3+x^2+2x+1")
list1 = ["Saurabh","Prasad","Jaiswal"]
dict = {
    "fName":"Saurabh",
    "mName":"Prasad",
    "lName":"Jaiswal"
}
st.header(list1)
st.header(dict)
pythonCode = """
def myFunc(){
    print("streamlit")
}
"""

st.code(pythonCode,language="python")

st.selectbox(
    label = "Name",
    options = list1,
    label_visibility= "visible"
)