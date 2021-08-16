from tkinter import *
import requests 
from PIL import ImageTk, Image
from tkinter import messagebox
from time import strftime 
from datetime import datetime

#44d1e5bd2d689d8817f42550b9e90f6a
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

#Funtions

def weather_res(weather):
    city_name = weather["name"]
    temp = weather["main"] ["temp"]
    desc = weather["weather"] [0] ["description"]
  
    
    city_label["text"] = city_name
    temp_label["text"] = str(int(temp)) + "°C"
    descriptio_label["text"] = desc


def weather_json(city):
    API_key = "44d1e5bd2d689d8817f42550b9e90f6a"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"APPID" : API_key, "q": city, "units": "metric"}
    response = requests.get(URL, params= parameters)
    weather = response.json()    
    
    weather_res(weather)
    
    



#Principal Window
window = Tk()
window.title("The Weather App")
window.geometry("350x500")
window.resizable(0,0)

#Frame up
Frame(window, width=350, height=80, bg="#03989e",).pack()

#Text Entry
city_text = Entry(window, font=("courier", 20, "normal"), justify= "center")
city_text.pack(padx= 30, pady= 30)

#Requests Button
requests_button = Button(window, text= "Enter", font=("courier", 20, "normal"), command= lambda:weather_json(city_text.get()))
requests_button.pack(padx=30, pady=30)

#Label 
city_label= Label(font=("attom", 20, "bold")) 
city_label.pack(padx=20, pady=20)

temp_label= Label(font=("attom", 50, "bold")) 
temp_label.pack(padx=10, pady=10)

descriptio_label= Label(font=("attom", 20, "bold")) 
descriptio_label.pack(padx=10, pady=10)








window.mainloop()

