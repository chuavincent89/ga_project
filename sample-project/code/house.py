import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.sav','rb'))

def prediction(Total_Size, Quality_score, House_Age):
    price = model.predict([[Total_Size, Quality_score, House_Age]])
    
    return price

 
    
st.write("""

# House Price Prediction!

""")

Total_Size = st.number_input('Insert Total Size', min_value = 1000, max_value = 100_000)
st.write('The Total Size is ', Total_Size)

House_Age = st.number_input('Insert House Age', min_value = 0, max_value = 100)
st.write('The House Age is ', House_Age)

Quality_score = st.number_input('Insert Quality Score', min_value = 0, max_value = 3)
st.write('The Quality Score is ', Quality_score)


# when 'Predict' is clicked, make the prediction and store it 
if st.button("Predict"): 
    result = round(np.exp(prediction(Total_Size, House_Age, Quality_score)[0]))
    st.write(f'Your Price is $ {result}')
    
if st.button("Print Hellow World!"):
    st.write("Hellow World!")
    
