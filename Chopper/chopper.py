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
    select_op = option_menu('Chopper', ['Diabetes prediction','Heart disease prediction','Help','About me'],icons = ['activity','heart-pulse-fill','info-circle','person-fill'] ,default_index=0)
    

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
        sex = st.text_input('Gender 1 for male, 0 for female.')
         
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
         
if select_op=='Help':
    st.title("Read about diabetes more here: ")
    ur = 'https://www.who.int/news-room/fact-sheets/detail/diabetes'
    u1 = 'https://www.calculator.net/bmi-calculator.html'
    h_treat = 'https://www.medicalnewstoday.com/articles/237191#treatments'
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(" World Health Organization. ")
        st.markdown(f'''<a href={ur}><button style="background-color:SkyBlue;">W.H.O</button></a>''', unsafe_allow_html=True)
        
    with col2:
        st.write("Calculate Your BMI index here: ")
        st.markdown(f'''<a href={u1}><button style="background-color:SkyBlue;">BMI</button></a>''', unsafe_allow_html=True)
        
    with col1:
        st.write("See About heart disease Treatement here: ")
        st.markdown(f'''<a href = {h_treat}><button style= "background-color:SkyBlue;">Treatment</button></a>''', unsafe_allow_html = True)
        
        
    
    



    
if (select_op=='About me'):
    st.title("Hey I'm Abhishek Paul P")
    col1, col2 = st.columns(2)
    url1 = 'https://github.com/AbhishekPaul08'
    image_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
    insta_url2 = "https://www.svgrepo.com/show/303154/instagram-2016-logo.svg"
    linkedin_logo = 'https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg'
    url3 = 'https://www.linkedin.com/in/abhi-shek-paul-955627282/'
    
    with col1:
        st.write("My Github profile")
        image_html = f'<a href="{url1}"><img src="{image_url}" alt="Icon" width="50" height="50">'

        st.markdown(image_html, unsafe_allow_html=True)
    
    #st.markdown("[![Title]()](https://github.com/AbhishekPaul08)")
    
   #st.markdown(f'''<a href={url1}><button style="background-color:GreenYellow;">GitHub</button></a>''', unsafe_allow_html=True)
    with col2:
        st.write("My linkedin profile")
        link_html = f'<a href="{url3}"><img src="{linkedin_logo}" alt="Icon" width="50" height="50">'

        st.markdown(link_html, unsafe_allow_html=True)
    #st.markdown(f'''<a href={url2}><button style="background-color:GreenYellow;">Linkedin</button></a>''', unsafe_allow_html=True)
        #st.markdown("[![Title](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/abhi-shek-paul-955627282/)")
    st.title('Connect with me on Social Media')
    url2 = "https://instagram.com/abhii_shek_paul?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D"
    insta_html = f'<a href="{url2}"><img src="{insta_url2}" alt="Icon" width="50" height="50">'

    st.markdown(insta_html, unsafe_allow_html=True)
    