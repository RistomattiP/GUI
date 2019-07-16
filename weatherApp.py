import tkinter as tk
from tkinter import font
import requests
import time
import threading

HEIGHT = 700
WIDTH = 800

def getWeather(city):
    url = f'http://api.apixu.com/v1/forecast.json?key=286dd8a8f7c64f229c360408190805&q={city}&days=5'
    response = requests.get(url)
    label['text'] = formatWeather(response.json())

def formatWeather(weather):
    try:
        location = 'Location: {},{}'.format(weather['location']['name'],weather['location']['country'])
        coordinates = 'Coordinates: lat: {}, lon: {}'.format(weather['location']['lat'],weather['location']['lon'])
        temp = 'Tempature: {} \'C Feels like: {}\'C'.format(weather['current']['temp_c'], weather['current']['feelslike_c'])
        lastUpdated = 'Last uptated: {}'.format(weather['current']['last_updated'])
        info = 'Info: {}'.format(weather['current']['condition']['text'])
        tomorrow = '{}: Avg. Temp: {} Info: {}'.format(weather['forecast']['forecastday'][1]['date'],weather['forecast']['forecastday'][1]['day']['avgtemp_c'], weather['forecast']['forecastday'][1]['day']['condition']['text'])
        tomorrow2 = '{}: Avg. Temp: {} Info: {}'.format(weather['forecast']['forecastday'][2]['date'],weather['forecast']['forecastday'][2]['day']['avgtemp_c'], weather['forecast']['forecastday'][2]['day']['condition']['text'])
        return(f'{location}\n{coordinates}\n{temp}\n{info}\n{lastUpdated}\n{tomorrow}\n{tomorrow2}')
    except:
        return 'Error Incorrect Input!'

def getTime():
    timeLabel['text'] = time.asctime()
    root.after(1000, getTime)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

timeLabel = tk.Label(root,text=time.asctime(), font=('Courier', 13))
timeLabel.place(rely=0.9, relwidth=1)
getTime()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame,text='Get Weather', font=40, command=lambda: getWeather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)



lowerFrame = tk.Frame(root, bg='#80c1ff', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerFrame, font=('Courier', 12), bg='white', anchor='nw', justify='left', bd=10)
label.place(relwidth=1, relheight=1)

root.bind('<Return>',lambda event: getWeather(entry.get()))

root.title('Weather App')
root.mainloop()
