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
        country = data['sys']['country']
        temp = data['main']['temp']
        temp_cel = temp - 273.15
        temp_f = (temp - 273.15)* 9/5 + 32
        icon = data['weather'][0]['icon']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        final = (name,temp_cel,icon,description,temp_f,humidity,country)
        return final
    else:
        None

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text']= '{}, {}'.format(weather[0],weather[6])
        temp_lbl['text']= '{:.2f}C, {:.2f}F'.format(weather[1],weather[4])
        icon_ref = PhotoImage(file='images/{}.png'.format(weather[2]))
        image['image'] = icon_ref
        image.image=icon_ref
        weather_lbl['text']= '{}, Humidity:{}%'.format(weather[3],weather[5])
    
    else:
        messagebox.showerror('Error','cannot find city{}'.format(city))

root = Tk()
root.title("weather app")
root.geometry('460x560')

city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.pack()
Label(root).pack()

search_btn = Button(root,text='search',width=12 ,command=search)
search_btn.pack()
Label(root).pack()
Label(root).pack()

location_lbl = Label(root,text='' ,font=('arial',26))
location_lbl.pack()

Label(root).pack()

temp_lbl = Label(root,text='',font =('arial',48))
temp_lbl.pack()

image = Label(root,image='')
image.pack()

weather_lbl = Label(root,text='',font=('arial',20))
weather_lbl.pack()



root.mainloop()

