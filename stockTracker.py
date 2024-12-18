#KEEP PRIVATE ON GITHUB TO NOT REVEAL KEYS 

from config import *
import customtkinter as CTk
from polygon import RESTClient
import requests
from datetime import date, timedelta
import datetime
from textblob import TextBlob
import json

#initiate newsapi.org API
url = 'https://newsapi.org/v2/everything?'

#initiate polygon API
client = RESTClient(polygonKey)

def getNews(query):
    parameters = {
        'q': str(query), # query phrase
        'pageSize': 100,  # maximum is 100
        'apiKey': newsAPIKey # your own API key
    }
    response = requests.get(url, params=parameters)
    response_json = response.json()
    return json.dumps(response_json)

def getStockData(stocksTicker):
    try:
        if datetime.datetime.today().weekday() == 6:
            information = client.get_daily_open_close_agg(stocksTicker.upper(), str(date.today()- timedelta(days = 2)))
        elif datetime.datetime.today().weekday() == 0:
            information = client.get_daily_open_close_agg(stocksTicker.upper(), str(date.today()- timedelta(days = 3)))
        else:
            information = client.get_daily_open_close_agg(stocksTicker.upper(), str(date.today()- timedelta(days = 1)))
        return str(information).split(", ")[3:7]
    except Exception as e:
        return

def getSentiment(text):
    return TextBlob(text).sentiment.polarity

def getPrediction(sentiment):
    if sentiment <= 0.1 and sentiment >= -0.1:
        return "Not enough reliable data to make a prediction."
    elif sentiment < 0 and sentiment > -0.2:
        return "Prediction: Stock price will fall. Confidence: low"
    elif sentiment <= -0.2 and sentiment > -0.5:
        return "Prediction: Stock price will fall. Confidence: medium"
    elif sentiment <= -0.5:
        return "Prediction: Stock price will fall. Confidence: high"
    elif sentiment > 0 and sentiment < 0.2:
        return "Prediction: Stock price will rise. Confidence: low"
    elif sentiment >= 0.2 and sentiment < 0.5:
        return "Prediction: Stock price will rise. Confidence: medium"
    elif sentiment >= 0.5:
        return "Prediction: Stock price will rise. Confidence: high"
    
def outputToApp():
    global stockTickerVar
    stockTicker=stockTickerVar.get()
    global textOutput
    textOutput.delete(1.0,CTk.END)
    stockTicker=str(stockTicker)
    if stockTicker=="" or len(stockTicker)<3:
        return
    stockData = getStockData(stockTicker)
    stockNews = getNews(stockTicker)
    #value from [-1,1]
    sentiment=getSentiment(stockNews)
    #get prediction
    prediction=getPrediction(sentiment)
    textOutput.insert(CTk.END, stockTicker.upper() + "\n" + str(sentiment) + "\n" + str(stockData) + "\n" + str(prediction))
    mainWindow.update()

#main window
mainWindow=CTk.CTk()
mainWindow.title("Stock Analyzer")
mainWindow.geometry("500x400")
mainWindow.resizable(False, False)
mainWindow.eval('tk::PlaceWindow . center')
    #stock ticker input, output, button and label
stockTickerVar=CTk.StringVar()
stockLabel=CTk.CTkLabel(master=mainWindow, text="Enter a stock ticker: ")
stockInput=CTk.CTkEntry(master=mainWindow, width=65, textvariable=stockTickerVar)
textOutput=CTk.CTkTextbox(master=mainWindow, height = 330, width = 500)
enterButton=CTk.CTkButton(master=mainWindow, text="Enter", width=65, command=outputToApp)
    #place widgets
textOutput.place(x=0,y=0)
stockLabel.place(x=110,y=350)
stockInput.place(x=240, y=350)
enterButton.place(x=320, y=350)

#initialize app
outputToApp()
mainWindow.mainloop()