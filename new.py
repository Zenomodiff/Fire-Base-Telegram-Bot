from telegram import *
from telegram.ext import *
from flask import Flask
import time , json , requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)


cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred,{

    'databaseURL': 'https://weather-station-91122-default-rtdb.firebaseio.com/'
})

Air_Quality = db.reference('Air_Quality')
Altitude = db.reference('Altitude')
Cng = db.reference('Cng')
Humidity = db.reference('Humidity')
Ldr = db.reference('Ldr')
Lpg = db.reference('Lpg')
Pressure = db.reference('Pressure')
Rain_Value = db.reference('Rain_Value')
Smoke = db.reference('Smoke')
Temperature = db.reference('Temperature')

bot = Bot("1940119944:AAHP9d3XQyMML5ITRsPTwLj5PDno6VWKEAQ")
#print(bot.get_me())

updater=Updater("1940119944:AAHP9d3XQyMML5ITRsPTwLj5PDno6VWKEAQ",use_context=True)

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
       4. /CNG - Compressed Natural Gas Value
       5. /HUMI - Humidity Value
       6. /LDR - Light Intensity
       7. /LPG - Liquefied petroleum gas Value
       8. /PRESS - Pressure Value
       9. /RV - Rain Value 
       10. /SMKE - Smoke Value
       11. /TEMP - Temperature Value '''
   )
    
@app.route('/')
def Message():
    return 'Bot Is Available @ apicallingbot in Telegram'

if __name__ == '__main__':
    app.run(port=5000)

start_value=CommandHandler('start',test_function)

dispatcher.add_handler(start_value)

def test_function1(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Air_Quality.get() 
   )
start_value1=CommandHandler('AQ',test_function1)

dispatcher.add_handler(start_value1)


def test_function2(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Altitude.get()
   )
start_value2=CommandHandler('ALTI',test_function2)

dispatcher.add_handler(start_value2)

def test_function3(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Cng.get()
   )
start_value3=CommandHandler('CNG',test_function3)

dispatcher.add_handler(start_value3)


def test_function4(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Humidity.get()
   )
start_value4=CommandHandler('HUMI',test_function4)

dispatcher.add_handler(start_value4)

def test_function5(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Ldr.get()
   )
start_value5=CommandHandler('LDR',test_function5)

dispatcher.add_handler(start_value5)


def test_function6(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Lpg.get()
   )
start_value6=CommandHandler('LPG',test_function6)

dispatcher.add_handler(start_value6)

def test_function7(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Pressure.get()
   )
start_value7=CommandHandler('PRESS',test_function7)

dispatcher.add_handler(start_value7)


def test_function8(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Rain_Value.get()
   )
start_value8=CommandHandler('RV',test_function8)

dispatcher.add_handler(start_value8)


def test_function9(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Smoke.get()
   )
start_value9=CommandHandler('SMKE',test_function9)

dispatcher.add_handler(start_value9)


def test_function10(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text= Temperature.get()
   )
start_value10=CommandHandler('TEMP',test_function10)

dispatcher.add_handler(start_value10)

def test_function11(update:Update,context:CallbackContext):
    bot.send_message(
       chat_id=update.effective_chat.id,

       text = [Air_Quality.get(), Altitude.get(), Cng.get(), Humidity.get(), Ldr.get(), Lpg.get(), Pressure.get(), Rain_Value.get(), Smoke.get(), Temperature.get() ]

   )
start_value11=CommandHandler('STATUS',test_function11)

dispatcher.add_handler(start_value11)


updater.start_polling()

 # {'Air_Quality': Air_Quality.get(), 'Altitude': Altitude.get(), 'Cng': Cng.get(), 'Humidity': Humidity.get(), 'Ldr': Ldr.get(), 'Lpg': Lpg.get(), 'Pressure': Pressure.get(), 'Rain_Value': Rain_Value.get(), 'Smoke': Smoke.get(), 'Temperature': Temperature.get()}
