import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

diabetese_model = pickle.load(open('diabetese_trained_model.sav', 'rb'))
heartAttack_model = pickle.load(open('heart_attack_trained_model.sav', 'rb'))
calories_model = pickle.load(open('calories_burnt_trained_model.sav', 'rb'))




#creating the side-bars
with st.sidebar:
    selected=option_menu("Predcition System",
                         ["Diabetese Prediction",
                          "Heart Attack Prediction",
                          "Calories Burnt Prediction"],
                         icons=['activity','heart','heart'],
                         default_index=0)
#default_index denotes at what index does the page load with, if 0 then Diabetese, if 1 then heart attack, if 2 then calories will be selected by default when loading the page





#Diabetese Prediction Page
if (selected=='Diabetese Prediction'):
    st.title('Diabetese Prediction using ML')
    st.write('Sample data : {1,189,60,23,846,30.1,0.398,59}')
    st.write('Expected Output: 1 (The person is Diabetic.)')
    
    #taking the inputs
    pregnencies=st.text_input("No. of pregnencies:")
    glucose=st.text_input("Glucose Level:")
    bloodPressure=st.text_input("Blood Pressure Level:")
    skinThickness=st.text_input("Skin Thickness:")
    insulin=st.text_input("Insulin Level:")
    bmi=st.text_input("BMI Value:")
    diabetesePedigreeFunction=st.text_input("Enter the Diabetese Pedigree Fucntion:")
    age=st.text_input("Age of the person")
    
    #code for prediction
    diabetese_diagnosis=''
    
    #creating a button to execute the prediction
    if st.button("Disbetese Test Result"):
        diabetese_prediction=diabetese_model.predict([[pregnencies,glucose,bloodPressure,skinThickness,insulin,bmi,diabetesePedigreeFunction,age]])
        if(diabetese_prediction[0]==1):
            diabetese_diagnosis="1 (The person is Diabetic)"
        else:
            diabetese_diagnosis="0 (The person is Non-Diabetic)"
    
    st.success(diabetese_diagnosis)
    st.markdown('**NOTE:** You can generate other sameple data using ChatGpt, Gemini or other preffered AI apps.')
    
 
    
 
    
    
#Heart Attack Prediction Page
if (selected=='Heart Attack Prediction'):
    st.title('Heart Attack Prediction using ML')
    st.write('Sample data : {68,1,0,144,193,1,1,141,0,3.4,1,2,3}')
    st.write('Expected Output: 0 (The person does not have Heart Attaack.)')
    
    #taking the inputs
    age=st.text_input("Age of the Person:")
    sex=st.text_input("Sex:")
    cp=st.text_input("CP value:")
    trestbps=st.text_input("TrestBps Value:")
    chol=st.text_input("Cholestrol Level:")
    fbs=st.text_input("FBS Value:")
    restecg=st.text_input("ResteCG value:")
    thalach=st.text_input("Thalach value:")
    exang=st.text_input("Exang Value:")
    oldpeak=st.text_input("Old Peak Index:")
    slope=st.text_input("Slope:")
    ca=st.text_input("CA index:")
    thal=st.text_input("THAL index:")
    #code for prediction
    heartAttack_diagnosis=''
    
    #creating a button to execute the prediction
    if st.button("Heart Attack Test Result"):
        heartAttack_data_list=[[float(age),int(sex),int(cp),float(trestbps),float(chol),int(fbs),int(restecg), float(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]]
        heartAttack_prediction=heartAttack_model.predict(heartAttack_data_list)
        if(heartAttack_prediction[0]==1):
            heartAttack_diagnosis="1 (The person has unhealty heart i.e Chances of Heart Attack)"
        else:
            heartAttack_diagnosis="0 (The person has healthy heart i.e Will not have Heart Attack)"
    
    st.success(heartAttack_diagnosis)  
    
    st.markdown('**NOTE:** You can generate other sameple data using ChatGpt, Gemini or other preffered AI apps.')    
    
    
 
    
 
    
#Calories Burnt Prediction Page
#smaple data :'female',27,165.0,65.0,6.0,85.0,39.2
if (selected=='Calories Burnt Prediction'):
    st.title('Calories Burnt Prediction using ML')
    st.write('Sample data : {Female,27,165.0,65.0,6.0,85.0,39.2}')
    st.write('Expected Output:Calories lost =23.0Kcal')
            
        #taking the inputs
    gender=st.text_input("Enter Gender (Male,Female):")
    age=st.text_input("Age of the Person:")
    height=st.text_input("Height of the person in cm:")
    weight=st.text_input("Weight of the person:")
    duration=st.text_input("Duration of exercise in minutes:")
    heartRate=st.text_input("Average Heart Rate during exercise:")
    bodyTemp=st.text_input("Body Temperature during the exercise:")
        
      
    #columns =	gender,age,height,weight,duration,hearRate,bodyTemp  
    #creating a button to execute the prediction
    
    #encoding the gender
    if(gender==0 or gender=='Female' or gender=='female' or gender=='F' or gender=='f'):
        gender=0
    else:
        gender=1
    calories_result=''
    if st.button("Exercise Calories Loss Result"):
        exerciseStats=[[int(gender),int(age),float(height),float(weight),float(duration),float(heartRate),float(bodyTemp)]]
        calories_prediction=calories_model.predict(exerciseStats)
        calories_result =f"Calories Lost During Exercise = {calories_prediction[0]:.2f} KCal"
    st.success(calories_result)  
    st.markdown('**NOTE:** You can generate other sameple data using ChatGpt, Gemini or other preffered AI apps.')    
       














