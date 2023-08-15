# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:10:03 2023

@author: asp00
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diab_model = pickle.load(open('C:/Users/asp00/OneDrive/Documents/Chopper/saved_model/diabetic_chopper.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/asp00/OneDrive/Documents/Chopper/saved_model/heart_chopper.sav', 'rb'))


with st.sidebar:
    select_op = option_menu('Chopper', ['Diabetes prediction','Heart disease prediction','help','About me'],icons = ['activity','heart-pulse-fill','info-square-fill','person-fill'] ,default_index=0)
    

#dia page
if(select_op=='Diabetes prediction'):
    st.title('Diabetes prediction')
    
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        Pregnancies = st.text_input('No of prenencies')
        
    with col2:
         Glucose = st.text_input('Glucose level')
         
    with col3:
         BloodPressure = st.text_input('Blood Pressure level')
         
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
         
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI Index')
          
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
           
    with col2:
        Age = st.text_input('Age')    
         
    
    outcome = ''
    
    if st.button('Diabetes result'):
        dia_pred = diab_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if dia_pred[0] == 1:
            outcome = 'The person is Diabetic'
        else:
            outcome = 'The person is not Diabetic'
            
    st.success(outcome)
         
        
    
    
    
    
    
if (select_op == 'Heart disease prediction'):
    st.title('Heart disease prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Your age')
        
    with col2:
        sex = st.text_input('Gender Male/Female only')
         
    with col3:
        cp = st.text_input('Chest Pain type')
         
    with col1:
        trestbps = st.text_input('Resting Blood Presure')
         
    with col2:
        chol = st.text_input('Colestral level in mg/dL')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
          
    with col1:
        restecg = st.text_input('Resting ECG Results')
           
    with col2:
        thalach = st.text_input('Max Heart Rate')  
    with col3:
        exang = st.text_input('Exercise induced Angina')  
        
    with col1:
        oldpeak  = st.text_input('Depression Caused By exercise')
           
    with col2:
        slope = st.text_input('slope of peak segment')  
    with col3:
        ca = st.text_input('Major vessels colored by flourasapy')  
    with col1:
        thal = st.text_input('Thal: 0 = normal,1 = fixed 2 = reversable ')
         
    
    heart_outcome = ''
    
    if st.button('heart result'):
        heart_pred = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_pred[0] == 1:
            heart_outcome = 'Please Check Up'
        else:
            heart_outcome = 'The person has healthy heart'
            
    st.success(heart_outcome)
         
if select_op=='help':
    st.title("Read about diabetes more here: ")
    ur = 'https://www.who.int/news-room/fact-sheets/detail/diabetes'
    st.markdown(f'''<a href={ur}><button style="background-color:GreenYellow;">W.H.O</button></a>''', unsafe_allow_html=True)
    st.write("Above blog is officially from World Health Organization. ")
    u1 = 'https://www.calculator.net/bmi-calculator.html'
    st.write("Calculate Your BMI index here: ")
    st.markdown(f'''<a href={u1}><button style="background-color:GreenYellow;">BMI</button></a>''', unsafe_allow_html=True)



    
if (select_op=='About me'):
    st.title("Hey I'm Abhishek Paul P")
    st.write ('My Github Repo')
    url1 = 'https://github.com/AbhishekPaul08'
    image_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
    insta_url2 = "https://www.svgrepo.com/show/303154/instagram-2016-logo.svg"
    image_html = f'<a href="{url1}"><img src="{image_url}" alt="Icon" width="50" height="50">'

    st.markdown(image_html, unsafe_allow_html=True)
    
    #st.markdown("[![Title]()](https://github.com/AbhishekPaul08)")
    
   # st.markdown(f'''<a href={url1}><button style="background-color:GreenYellow;">GitHub</button></a>''', unsafe_allow_html=True)
    st.write('Linkedin')
    #st.markdown(f'''<a href={url2}><button style="background-color:GreenYellow;">Linkedin</button></a>''', unsafe_allow_html=True)
    st.markdown("[![Title](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/abhi-shek-paul-955627282/)")
    st.title('Connect with me on Social Media')
    url2 = "https://instagram.com/abhii_shek_paul?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D"
    insta_html = f'<a href="{url2}"><img src="{insta_url2}" alt="Icon" width="50" height="50">'

    st.markdown(insta_html, unsafe_allow_html=True)