import requests
from bs4 import BeautifulSoup

def get_weather(city_name):
    try:
        # URL of the wttr.in website for weather
        url = f'https://wttr.in/{city_name}?format=%C+%t+%w+%h+%P+%l'
        
        # Send the GET request to the site
        response = requests.get(url)
        
        if response.status_code == 200:
            # Print the weather information directly from wttr.in
            print(f"Weather information for {city_name}:")
            print(response.text)
        else:
            print("City not found or invalid input.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
