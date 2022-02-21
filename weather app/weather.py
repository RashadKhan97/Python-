from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


# __________ Functional Part for __________________________________#

def get_weather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        name.config(text='CURRENT WEATHER')

        # __________ Weather ________________________________#

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9a4d1c05474fd50c648f1304a24babed"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # ____ Showing Temperature and Condition beside Logo ______#

        temperature.config(text=(temp, "°"))
        con.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        # ____ Showing Temperature and Condition beside Logo ______#

        Wind.config(text=wind)
        Hum.config(text=humidity)
        Des.config(text=description)
        Pre.config(text=pressure)
    except Exception as e:
        messagebox.showerror('Weather App', 'Invalid Entry!!')


# __________ GUI ____________________________________#

root3 = Tk()
root3.title('Weather App')
root3.geometry('1000x600+260+130')
root3.resizable(False, False)

# __________ Search Box _____________________________#

search_image = PhotoImage(file='search.png')
search_image_Label = Label(root3, image=search_image)
search_image_Label.place(x=500, y=20)

textfield = tk.Entry(root3, justify='center', width=17, font=('Bulletto Killa', 23, 'bold'), bg='#404040', bd='0',
                     fg='white')
textfield.place(x=630, y=39)
textfield.focus()

# __________ Search Icon ____________________________#

search_icon = PhotoImage(file='search_icon.png')
search_icon_button = Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#404040', command=get_weather)
search_icon_button.place(x=545, y=32)

# __________ Weather Logo ___________________________#

logo_image = PhotoImage(file='logo.png')
logo_image_Lable = Label(root3, image=logo_image)
logo_image_Lable.place(x=325, y=150)

# __________ Bottom Box  _____________________________#

bottom_frame_image = PhotoImage(file='box.png')
bottom_frame_image.Label = Label(root3, image=bottom_frame_image)
bottom_frame_image.Label.pack(padx=5, pady=5, side=BOTTOM)

# __________ TIME  ____________________________________#

name = Label(root3, font=('arial', 15, 'bold'))
name.place(x=99, y=130)
clock = Label(root3, font=('times new roman', 24))
clock.place(x=130, y=160)

# __________ Lable Headline Names _____________________#

Head_Label1 = Label(root3, text='WIND', font=('times new roman', 15, 'bold'), fg='white', bg='#1ab5ef')
Head_Label1.place(x=170, y=501)

Head_Label2 = Label(root3, text='HUMIDITY', font=('times new roman', 15, 'bold'), fg='white', bg='#1ab5ef')
Head_Label2.place(x=310, y=501)

Head_Label3 = Label(root3, text='DESCRIPTION', font=('times new roman', 15, 'bold'), fg='white', bg='#1ab5ef')
Head_Label3.place(x=500, y=501)

Head_Label4 = Label(root3, text='PRESSURE', font=('times new roman', 15, 'bold'), fg='white', bg='#1ab5ef')
Head_Label4.place(x=720, y=501)

# ____ Lable Headline of Temperature and condition _____#

temperature = Label(font=('arial', 70, 'bold'), fg='red')
temperature.place(x=580, y=205)
con = Label(font=('arial', 15, 'bold'))
con.place(x=580, y=305)

Wind = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
Wind.place(x=170, y=531)

Hum = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
Hum.place(x=310, y=531)

Des = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
Des.place(x=500, y=531)

Pre = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
Pre.place(x=720, y=531)

root3.mainloop()
