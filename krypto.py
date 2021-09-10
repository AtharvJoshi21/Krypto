import requests
import tkinter as tk
from datetime import datetime, time
#FOR FETCHING DATA
def trackCrypto():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_d'
    response = requests.get(url).json()
    price = response['current_price']
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=price)
    labelTime.config(text="Updated at : "+time)


    # canvas.after(1000,trackCrypto)

#FOR API
canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Crypto Tracker")

#fonts
f1 = ("poppins" ,24,"bold") #(font name,font size,font style)
f2 = ("poppins" ,20,"bold")
f3 = ("poppins" ,18,"normal")

#lables
label = tk.Label(canvas,text="Crypto Price",font=f1)
#padding for y co-ordinate
label.pack(pady=20) #padding

#store price of our crypto
labelPrice = tk.Label(canvas,font=f2)
labelPrice.pack(pady=20)

#store time at the time of price
labelTime = tk.Label(canvas,font=f3)
labelTime.pack(pady=20)

trackCrypto()

canvas.mainloop()

