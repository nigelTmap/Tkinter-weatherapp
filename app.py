from tkinter import *
from configparser import ConfigParser
import requests
from tkinter import messagebox


url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key'] 
 

def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        data = result.json()
        
        name = data['name']
        description = data['weather'][0]['description']
       # icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        final = (name,description,temp )
        return final
    else:
        None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text']= '{}'.format(weather[0])
     #   img_lbl['bitmap']='images/{}.png'.format(weather[2])
        temp_lbl['text']= '{:.2f}C'.format(weather[3])
        weather_lbl['text']= weather[1]
    
    else:
        messagebox.showerror('Error','cannot find city{}'.format(city))

root = Tk()
root.title("weather app")
root.geometry('700x350')

city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.pack()

search_btn = Button(root,text='search',width=12 ,command=search)
search_btn.pack()

location_lbl = Label(root,text='' ,font={'bold',20})
location_lbl.pack()

#img_lbl = Label(root,bitmap='')
#img_lbl.pack()

temp_lbl = Label(root,text='')
temp_lbl.pack()

weather_lbl = Label(root,text='')
weather_lbl.pack()



root.mainloop()
