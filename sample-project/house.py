import streamlit as st
import pickle

# filename = 
# model = pickle.load(open('model.sav','rb'))

#def predict(Total_Size, House_Age, Quality_score):
    

    
st.write("""

# House Price Prediction!

""")

Total_Size = st.number_input('Insert Total Size')
st.write('The Total Size is ', Total_Size)

House_Age = st.number_input('Insert House Age')
st.write('The House Age is ', House_Age)

Quality_score = st.number_input('Insert Quality Score')
st.write('The Quality Score is ', Quality_score)