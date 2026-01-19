import os
import pandas as pd
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Lets get the API Key from the environment

gemini_api_key = os.getenv('Google_API_Key2')

# Lets configure the model
model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    api_key = gemini_api_key,
    temperature = 0.7
)

# Lets design the UI of application

st.title(':orange[HealthifyMe:] :red[Your personal Health Assistance]')
st.markdown(''' <span style="color: #14B8A6; font-size: 17px; font-weight: 600;">
This application will assist you to get better and customized Health advice. You can ask your health related issues and get the personalized 
            guidance.
            </span> 
            <br><br>
''', unsafe_allow_html=True)

tips = '''
Follow these Steps : 
* Enter your details in Sidebar.
* Rate your activity and fitness on the scale of 0-5.
* Submit your details.
* Ask your questions on the main page.
* Click generate and Relax back ypur report will be generated soon.
'''
st.info(f'{tips}')

print('      ')
# Lets design a sidebar for all the user parameter

st.sidebar.header(':red[ENTER YOUR DETAILS]')
name = st.sidebar.text_input('Enter Your Name')
gender = st.sidebar.selectbox('Select Your Gender',['Male','Female','Other'])
age = st.sidebar.text_input('Enter Your Age')
weight = st.sidebar.text_input('Enter Your Weight in kgs')
height = st.sidebar.text_input('Enter Your Height in cms')
BMI = pd.to_numeric(weight)/((pd.to_numeric(height)/100)**2)
Active = st.sidebar.slider('Rate your activity (0-5)',0,5,step=1)
Fitness = st.sidebar.slider('Rate your Fitness (0-5)',0,5,step=1)
if st.sidebar.button('SUBMIT'):
    st.sidebar.write(f'Hey {name} welcome to this Application, Your BMI is {round(BMI,3)}Kg/m^2')


# Lets use the gemini model to generate the report

user_input = st.text_input('Ask me Anything, I will be grateful to assist you: ')

prompt = f'''
<Role> You are an expert in health and wellness with 10+ years of experience in health related guidance to people.
<Goal> Generate the customize the report addressing the problem the user has asked. Here is the Problem that the user has asked {user_input}
<Context> Here are the details that the user has provided  name = {name},age={age},height={height},weight={weight},gender = {gender},BMI = {BMI},
Activity_rating(0-5) = {Active},fitness_rating(0-5) = {Fitness}
<Instruction> 
* Use bullet points where ever possible 
* Create tables to represent any data where ever possible 
* Strcitly Do not advice any medicine
<Format> 
* Start with 2-3 line of comment on the details that the user has provided
* Explain what the real problem could be on the basis of input the user has provided
* Suggest the possible solutions.
* Mention the doctor from which specialization can be visited if required
* Mention any changes in the diet which is required
* In last a final summary of all the things that has been discussed in the report
<Style> it should look clean, and should be easily understandable by a lamen. 
'''

if st.button('Generate'):
    response = model.invoke(prompt)
    st.write(response.content)