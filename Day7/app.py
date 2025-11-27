import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# for runing this code on cmd ,  ---  streamlit run filename

st.title("Streamlit app of VGU")
st.text("Welcome to streamlit app")
st.header("i am a header")
st.write("You can write",10+5)

name = st.text_input("Enter your name:")
age = st.number_input("Enter  your age:")
st.write("Your name is:" ,name)
st.write("Your AGE is:" ,age)  

st.selectbox("Enter your course:", ["BCA","B.TECH","BBA"])
if st.button("Click ME"):
    st.success("Clicked Button")

file = st.file_uploader("Upload your file")
if file:
    contect = file.read()
    st.write("your file is Uploaded")


data = {"Name":["Tom","Jack"],"marks":[10,20]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame({
    "Marks":[10,20,20,30]
})

st.line_chart(data)

st.bar_chart(data)


subject = [["python"],["C++"],["Java"]]
marks = [20,10,5]

fig,ax =plt.subplots()
ax.pie(marks, lables = subject, autopct = '%1.1f%%' )
st.pyplot(fig)