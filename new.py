from telegram import *
from telegram.ext import *
from flask import Flask
import json , requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred,{

    'databaseURL': 'https://weather-station-91122-default-rtdb.firebaseio.com/'
})

Air_Quality = db.reference('Air_Quality').get()
Altitude = db.reference('Altitude').get()
Cng = db.reference('Cng').get()
Humidity = db.reference('Humidity').get()
Ldr = db.reference('Ldr').get()
Lpg = db.reference('Lpg').get()
Pressure = db.reference('Pressure').get()
Rain_Value = db.reference('Rain_Value').get()
Smoke = db.reference('Smoke').get()
Temperature = db.reference('Temperature').get()

a = "Air_Quality " + str(Air_Quality) + " PPM"
b = "Altitude " + str(Altitude) + " M"
c = "Cng " + str(Cng) + " PPM"
d = "Humidity " + str(Humidity) + " %"
e = "Ldr " + str(Ldr) + " LX"
f = "Lpg " + str(Lpg) + " PPM"
g = "Pressure " + str(Pressure) + " PA"
h = "Rain_Value " + str(Rain_Value) + " MM"
i = "Smoke " + str(Smoke) + " PPM"
j = "Temperature " + str(Temperature) + " °C"

bot = Bot("1940119944:AAGDTbCYW6PFCHjgnbKLRCoV3lqu2neWL0Y")

updater=Updater("1940119944:AAGDTbCYW6PFCHjgnbKLRCoV3lqu2neWL0Y",use_context=True)

dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= '''  
       Welcome to ZenoModiff Weather Station. 
       Use the following commands for stats:-
       
       1. /STATUS - Gives all values
       2. /AQ - Air Quality Value
       3. /ALTI - Altitude Value
       4. /CNG - Natural Gas Value
       5. /HUMI - Humidity Value
       6. /LDR - Light Intensity
       7. /LPG - Liquefied petroleum gas Value
       8. /PRESS - Pressure Value
       9. /RV - Rain Value 
       10. /SMKE - Smoke Value
       11. /TEMP - Temperature Value 
       '''       
        
   )
    
@app.route('/')
def Message():
    return '''
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to Telegram BOT 🤖</h1>
      <h2 class="project-tagline">Telegram Bot Which Return Data From Firebase</h2
<h2 id="Serach">Search:</h2>
<ul>
<p>@apicallingbot on Telegram</p>
</ul>
    </main>
  </body>
</html>
    '''

if __name__ == '__main__':
    app.run(port=5000)

start_value=CommandHandler('START',test_function)

dispatcher.add_handler(start_value)

def test_function1(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= a
   )
start_value1=CommandHandler('AQ',test_function1)

dispatcher.add_handler(start_value1)


def test_function2(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= b
   )
start_value2=CommandHandler('ALTI',test_function2)

dispatcher.add_handler(start_value2)

def test_function3(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= c
   )
start_value3=CommandHandler('CNG',test_function3)

dispatcher.add_handler(start_value3)


def test_function4(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= d
   )
start_value4=CommandHandler('HUMI',test_function4)

dispatcher.add_handler(start_value4)

def test_function5(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= e
   )
start_value5=CommandHandler('LDR',test_function5)

dispatcher.add_handler(start_value5)


def test_function6(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= f
   )
start_value6=CommandHandler('LPG',test_function6)

dispatcher.add_handler(start_value6)

def test_function7(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= g
   )
start_value7=CommandHandler('PRESS',test_function7)

dispatcher.add_handler(start_value7)


def test_function8(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= h
   )
start_value8=CommandHandler('RV',test_function8)

dispatcher.add_handler(start_value8)


def test_function9(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= i
   )
start_value9=CommandHandler('SMKE',test_function9)

dispatcher.add_handler(start_value9)


def test_function10(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= j
   )
start_value10=CommandHandler('TEMP',test_function10)

dispatcher.add_handler(start_value10)

def test_function11(update:Update,context:CallbackContext):
    list_Data = a,b,c,d,e,f,g,h,i,j
    bot.send_message(
       chat_id=update.effective_chat.id,

       text = list_Data
   )
start_value11=CommandHandler('STATUS',test_function11)

dispatcher.add_handler(start_value11)

updater.start_polling()
