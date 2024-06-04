import requests
import tkinter as tk

root = tk.Tk()
bg_color = "#dcccc0"
root.title("Weather App")
root.geometry("400x400")
root.resizable(height=False, width=False)
root.config(bg=bg_color)

def get_weather():
    city_name = inp_city.get()
    api_key = "86002db922a90c13874a56f8c4f17337"
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(weather_url)
    weather = response.json()

    if weather.get('cod') != 200:
        weather_now.config(text=f"Error: {weather.get('message', 'Unable to get weather')}")
        return

    weather_main = weather['weather'][0]['main']
    temp = weather['main']['temp'] - 273.15
    feels_like = weather['main']['feels_like'] - 273.15
    humidity = weather['main']['humidity']
    max_temp = weather['main']['temp_max'] - 273.15
    min_temp = weather['main']['temp_min'] - 273.15

    weather_now.config(text=f"Weather: {weather_main}\n"
                            f"Temperature: {temp:.2f}°C\n"
                            f"Feels Like: {feels_like:.2f}°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Max Temperature: {max_temp:.2f}°C\n"
                            f"Min Temperature: {min_temp:.2f}°C")

city_head = tk.Label(root, text='Enter City Name', font='Arial 12 bold')
city_head.pack(pady=10)

inp_city = tk.Entry(root, width=24, font='Arial 14 bold')
inp_city.pack()

check_button = tk.Button(root, command=get_weather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5)
check_button.pack(pady=20)

weather_now = tk.Label(root, text="The Weather is:", font='Arial 12 bold')
weather_now.pack(pady=10)

root.mainloop()