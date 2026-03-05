import streamlit as st
import datetime

# st.markdown("# Hello")
# st.markdown("## Hello")
# st.header("It is a header")
# st.subheader("It is a subheader")
# st.text("It is a text")
# st.caption("It is a Caption")
# st.latex("x^3+x^2+2x+1")
# st.header(list1)
# st.header(dict)
# pythonCode = """
# def myFunc(){
#     print("streamlit")
# }
# """

# st.code(pythonCode,language="python")
list1 = ["Saurabh", "Prasad", "Jaiswal"]
dict = {
    "fName": "Saurabh",
    "mName": "Prasad",
    "lName": "Jaiswal"
}
st.selectbox(
    label="Name",
    options=list1,
    label_visibility="visible",
    help="Select 1 name",
    placeholder="Please select only one name"
)

st.multiselect(
    label="Select name",
    help="Select names which you want to select",
    options=list1,
    max_selections=2,
    placeholder="Please select only two name"
)

basicSlider = st.slider(
    label="Basic Slider",
    min_value=10,
    max_value=100,
    value=50

)

st.write(f"Basic Slider: {basicSlider}")

rangeSlider = st.slider(
    label="Ranger Slider",
    help="Slect two numbers",
    min_value=0,
    max_value=100,
    value=(25, 75),
    step=10
)

st.write(f"Range slider result: {rangeSlider}")

floatSlider = st.slider(
    label="Float Slider",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)

dateSlider = st.slider(
    label="Choose Date by Slider",
    min_value=datetime.date(1992, 9, 14),
    max_value=datetime.date(2026, 5, 3),
    format="DD/MM/YYYY"
)

numberInput = st.number_input(
    label="Number Input",
    min_value=25,
    max_value=100,
    value=50,
    help="Please choose a number between 25 to 100",
    step=5
)

st.write(f"Number input result: {numberInput}")

numberInputSideBar = st.sidebar.number_input(
    label="Input Numbers in sidebar",
    min_value=25,
    max_value=100,
    value=50,
    help="Please enter number in side bar",
    step=5
)
st.sidebar.write(f"Number from side Bar input: {numberInputSideBar}")
st.write(f"Number from side Bar input: {numberInputSideBar}")

form = st.form(
    key="form1",
    clear_on_submit=False,
    enter_to_submit=True,
    border=True
)
dob = form.date_input(
    label="Enter your Date of Birth"
)
submit = form.form_submit_button(
    label="Submit your DOB"
)


if submit:
    st.caption(f"Dob Recieved:{dob}")

form1 = st.sidebar.form(
    key="sidebar",
    clear_on_submit=False,
    border=True
)
fName = form1.text_input(
    label="Please Enter your First Name:",
    placeholder="First Name"
)
lName = form1.text_input(
    label="Please enter your Last Name",
    placeholder="Last Name"

)
submit1 = form1.form_submit_button(label="Submit your full name")
if submit1:
    st.sidebar.caption(f"Your full name is {fName} {lName}")
