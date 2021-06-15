from flask import Flask, request  # python Flask
import pyrebase  # python library for firebase
import telegram  # Python telegram bot library
# Custom library for getting seceret credentials
from credentials.py import bot_token, bot_user_name, URL, firebase_token, firebase_authDomain, firebase_databaseURL, firebase_storageBucket

# For BOT creation
global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

# configuration for connection
configurationForFirebase = {
    "apiKey": firebase_token,
    "authDomain": firebase_authDomain,
    "databaseURL": firebase_databaseURL,
    "storageBucket": firebase_storageBucket,
}

firebaseObject = pyrebase.initialize_app(
    configurationForFirebase)  # firebase connection object
databaseObject = firebaseObject.database()  # firebase database initialisation


# Definition to fetch values from FireBase
def getValuesFromFirebaseList():
    listData = []
    listData.append(databaseObject.child(
        "sensor-values").child("Smoke").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Cng").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Lpg").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Air_Quality").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Rain_Value").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Temperature").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Humidity").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Ldr").get().val())
    listData.append(databaseObject.child(
        "sensor-values").child("Pressure").get().val())    
    listData.append(databaseObject.child(
        "sensor-values").child("Altitude").get().val())  
    return listData


# Definition to get Individual Value
def getValuesFromFirebaseInd(valueName):
    result = []
    result.append(databaseObject.child("sensor-values").child("last_updated").get().val())
    if valueName == "AQUI":
        result.append(databaseObject.child("sensor-values").child("air_quality_index").get().val())
        return result
    elif valueName == "CNG":
        result.append(databaseObject.child("sensor-values").child("cng").get().val())
        return result
    elif valueName == "HI":
        result.append(databaseObject.child("sensor-values").child("dht22_heat_index").get().val())
        return result
    elif valueName == "HUM":
        result.append(databaseObject.child("sensor-values").child("dht22_humidity").get().val())
        return result
    elif valueName == "TEM":
        result.append(databaseObject.child("sensor-values").child("dht22_temperature").get().val())
        return result
    elif valueName == "LPG":
        result.append(databaseObject.child("sensor-values").child("lpg").get().val())
        return result
    elif valueName == "RAIN":
        result.append(databaseObject.child("sensor-values").child("rain_sensor").get().val())
        return result
    elif valueName == "SMKE":
        result.append(databaseObject.child("sensor-values").child("smoke").get().val())
        return result


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()

    individualValue = """
    {} : {} {}
    Last Updated : {}
    """

    # the first time you chat with the bot AKA the welcoming message
    if text == "/start":
        bot_welcome = """
       HOME WEATHER STATION

       Welcome to Sashwat's Home Weather Station. Use the following commands for stats:-
       1. /status - Gives all values
       2. /AQUI (MQ-135) - Air Quality Index in PPM
       3. /CNG (MQ-4) - Compressed Natural Gas in PPM
       4. /LPG (DHT22) - Heat Index in Celsius
       5. /HUM (DHT22) - Humidity in Percentage
       6. /TEM (DHT22) - Temperature in Celsius
       7. /LPG (MQ-5) - LPG in PPM
       8. /RAIN (Rain sensor) - Analog Value
       """

        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome,
                        reply_to_message_id=msg_id)

    elif text == "/stats":
        firebaseResult = getValuesFromFirebaseList()
        resultCommand = """
        The result is as follows:-
        1. CNG: {} PPM
        2. AQI: {} PPM
        3. LPG: {} PPM
        4. SMOKE: {} PPM
        5. RAIN: {}
        6. TEMPERATURE: {} °C
        7. HUMIDITY: {} %
        8. HI: {} °C

        Last Updated : {}
        """.format(firebaseResult[0], firebaseResult[1], firebaseResult[2], firebaseResult[3], firebaseResult[4], firebaseResult[5], firebaseResult[6], firebaseResult[7], firebaseResult[8])

        # Send the stat output
        bot.sendMessage(chat_id=chat_id, text=resultCommand,
                        reply_to_message_id=msg_id)

    elif text == "/AQI":
        firebaseValues = getValuesFromFirebaseInd("AQUI")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("AQUI", firebaseValues[1], "PPM",firebaseValues[0]),
                        reply_to_message_id=msg_id)

    elif text == "/CNG":
        firebaseValues = getValuesFromFirebaseInd("CNG")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("CNG", firebaseValues[1], "PPM", firebaseValues[0]),
                        reply_to_message_id=msg_id)

    elif text == "/HI":
        firebaseValues = getValuesFromFirebaseInd("HI")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("HI", firebaseValues[1], "°C", firebaseValues[0]),
                        reply_to_message_id=msg_id)

    elif text == "/HUM":
        firebaseValues = getValuesFromFirebaseInd("HUM")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("HUM", firebaseValues[1], "%", firebaseValues[0]),
                        reply_to_message_id=msg_id)

    elif text == "/TEM":
        firebaseValues = getValuesFromFirebaseInd("TEM")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("TEM", firebaseValues[1], "°C", firebaseValues[0]),
                        reply_to_message_id=msg_id)

    elif text == "/LPG":
        firebaseValues = getValuesFromFirebaseInd("LPG")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("LPG", firebaseValues[1], "PPM", firebaseValues[0]),
                        reply_to_message_id=msg_id)

    elif text == "/RAIN":
        firebaseValues = getValuesFromFirebaseInd("RAIN")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("RAIN", firebaseValues[1], " ", firebaseValues[0]),
                        reply_to_message_id=msg_id)

    elif text == "/SMKE":
        firebaseValues = getValuesFromFirebaseInd("SMKE")
        bot.sendMessage(chat_id=chat_id, text=individualValue.format("SMOKE", firebaseValues[1], "PPM", firebaseValues[0]),
                        reply_to_message_id=msg_id)

    else:
        bot.sendMessage(
            chat_id=chat_id, text="Unsupported Query requested", reply_to_message_id=msg_id)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "HOME WEATHER STATION WEBHOOK WORKING PROPERLY. STATUS: 200"
    else:
        return "HOME WEATHER STATION WEBHOOK ERROR. STAUS: 400"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
