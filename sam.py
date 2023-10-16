import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the model
model = pickle.load(open('RF_model_RF.pkl', 'rb'))

def text_encoder(word):
    encoder = LabelEncoder()
    return encoder.fit_transform(np.array(word).ravel())
    

st.title('CO2 Emission Prediction')
st.write('This app predicts the CO2 emission of a car based on its features')

st.write('Please enter the following features:')
# car name, 'ENGINESIZE', 'CYLINDERS','TRANSMISSION', 'FUELTYPE', 'FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY', 'FUELCONSUMPTION_COMB','FUELCONSUMPTION_COMB_MPG'

st.write('Enter Your Car Name:')
car_name = st.text_input('Car Name')

st.write('Enter Engine Size: ')
eng_size = st.number_input('Engine Size')

st.write('Enter CEnter no.of Cylinders: ')
clinder_num = st.number_input('Cylinders')

st.write('Select your Type of Transmission: ')
trans = st.selectbox('Transmission',('AS5', 'M6', 'AV7', 'AS6', 'A6', 'AM7', 'AV8', 'AS8', 'A7', 'A8','M7', 'A4', 'M5', 'AV', 'A5', 'AM6', 'AS7', 'A9', 'AS9', 'AV6','AS4', 'AM5'))
if trans == 'AS5':
    bin_trans = 0
elif trans == 'M6':
    bin_trans = 1
elif trans == 'AV7':
    bin_trans = 2
elif trans == 'AS6':
    bin_trans = 3
elif trans == 'A6':
    bin_trans = 4
elif trans == 'AM7':
    bin_trans = 5
elif trans == 'AV8':
    bin_trans = 6
elif trans == 'AS8':
    bin_trans = 7
elif trans == 'A7':
    bin_trans = 8
elif trans == 'A8':
    bin_trans = 9
elif trans == 'M7':
    bin_trans = 10
elif trans == 'A4':
    bin_trans = 11
elif trans == 'M5':
    bin_trans = 12
elif trans == 'AV':
    bin_trans = 13
elif trans == 'A5':
    bin_trans = 14
elif trans == 'AM6':
    bin_trans = 15
elif trans == 'AS7':
    bin_trans = 16
elif trans == 'A9':
    bin_trans = 17
elif trans == 'AS9':
    bin_trans = 18
elif trans == 'AV6':
    bin_trans = 19
elif trans == 'AS4':
    bin_trans = 20
else:
    bin_trans = 21



st.write('Select your Fuel type: ')
# displaying the types of fuel type using dropdown in streamlit
dropdown = st.selectbox('Fuel Type',('Z', 'D', 'X', 'E'))
if dropdown == 'Z':
    fuel = 0
elif dropdown == 'D':
    fuel = 1
elif dropdown == 'X':
    fuel = 2
else:
    fuel = 3

st.write('Enter Fuel consumption in city: ')
con_city = st.number_input('consumption in city')

st.write('Enter Fuel consumption in Highways: ')
con_hwy = st.number_input('consumption in highway')

st.write('Enter Fuel consumption in both city and highway:')
con_both = st.number_input('consumption in city and highway')

st.write('Enter Fuel Consumption comb MPG:')
MPG = st.number_input('MPG')

# button 
res = model.predict([[eng_size,clinder_num,bin_trans,fuel,con_city,con_hwy,con_both,MPG]])
# button 
button = st.button('Predict')
if button:
    st.write('The CO2 emission of the your {} car is: '.format(car_name))
    st.write(res)
    
    
