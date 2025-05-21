import requests
import json
import streamlit as st


st.title("Welcome to weather APP")

if "city" not in st.session_state:
    st.session_state.city = ""
city = st.text_input("Enter City Name", key = 'city')

def get_info(data):
    name = data['name']
    temp = data['main']['temp']
    country = data['sys']['country']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    st.markdown("### Current weather :")
    st.info(f"""City : {name} \n
Country : {country} \n
Temperature : {temp}°C ,  Feels Like : {feels_like}°C \n
Humidity : {humidity}% \n
Wind Speed : {wind_speed} km/h \n
Description : {description} 
            """)

    # with st.container():
        # st.markdown("### Current weather :")
        # st.write(f"City : {name}")
        # st.write(f"Temperature : {temp}°C")
        # st.write(f"Humidity : {humidity}")
        # st.write(f"Description : {description}")

if st.session_state.city:
    API_key = "c7a1e5347b9b47dcdcefb11e9ab63ad9"
    url = f'https://api.openweathermap.org/data/2.5/weather?&appid={(API_key)}&q={city}&units=metric'
    response = requests.get(url)

    if response.status_code==200:
        data = json.loads(response.text)
        get_info(data)
    else:
        st.error("City not found or API error")

    

