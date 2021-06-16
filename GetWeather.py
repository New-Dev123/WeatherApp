import tkinter as tk
import os
import requests

HEIGHT=500
WIDTH=400

def test(entry):
    print('This is:', entry)

# 760246f97f952eb9a2b9793645eb0b68
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature: %s Farenheit' % (name,desc,temp)
    except:
        final_str = 'There was an error getting that information'

    return final_str
def get_weather(city):
    weather_key = '760246f97f952eb9a2b9793645eb0b68'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,'q': city,'units':'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] =  format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


background = tk.PhotoImage(file='pic.gif')
backgroundLabel = tk.Label(root, image=background)
backgroundLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#Top Box
frame = tk.Frame(root, bg='turquoise',bd=10)
frame.place(relx=.5, rely=0.1, relwidth=.75, relheight=.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=.65, relheight=1)

button = tk.Button(frame, text='Get Weather', bg='grey', command= lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=.3, relheight=1)

#Lower Box
lowerFrame = tk.Frame(root,bg='turquoise',bd=10)
lowerFrame.place(relx=.5, rely=0.25, relwidth=.75, relheight=.6, anchor='n')

label = tk.Label(lowerFrame, font=60)
label.place( relwidth=1, relheight=1)


root.mainloop()