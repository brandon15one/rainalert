import requests
from twilio.rest import Client

# Weather API configuration
weather_api_key = "YOUR_WEATHER_API_KEY"
weather_base_url = "https://api.openweathermap.org/data/2.5/weather"

# Twilio API configuration
twilio_account_sid = "YOUR_TWILIO_ACCOUNT_SID"
twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"
twilio_phone_number = "YOUR_TWILIO_PHONE_NUMBER"
recipient_phone_number = "RECIPIENT_PHONE_NUMBER"

def get_weather(city):
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric"  # You can change the unit to 'imperial' if you prefer Fahrenheit
    }

    response = requests.get(weather_base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return f"The current temperature in {city} is {temperature}°C with {weather_description}."
    else:
        return "Failed to retrieve weather information."

def send_sms(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print("SMS sent successfully!")

# Example usage
city_name = "London"  # Replace with the desired city name
weather_info = get_weather(city_name)
send_sms(weather_info)
