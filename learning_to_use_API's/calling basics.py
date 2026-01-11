import requests

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    try:
        response = requests.get(url, params=params)
    except:
        print("Network error")
        return None
    data = response.json()
    return data["current_weather"]

def get_coordinates(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    response = requests.get(url, params=params, headers={"User-Agent": "MyWeatherApp/1.0"})

    if response.status_code != 200:
        print("Error fetching location")
        return None

    data = response.json()

    if not data:
        print("City not found")
        lat,lon = get_coordinates(input("Please enter a valid city name: "))
    else:
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
    
    return lat, lon

def gpt_request(place, weather):

    url = "https://api.openai.com/v1/chat/completions"
    API_KEY = "your_API_KEY"# Replace with your actual OpenAI API key as sharing mine in the code could lead to fraud.
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "describe the weather in "+place+" at the moment where the weather is "+str(weather)}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    reply = response.json()
    print(reply["choices"][0]["message"]["content"])


#  --main--

place = input("Enter a city name: ")
lat, lon = get_coordinates(place)
weather = get_weather(lat,lon)  
print(weather["temperature"])
gpt_request(place,weather)