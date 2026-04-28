import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(".json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iot-ai-security-default-rtdb.firebaseio.com/"
})

def send_data(temp, water, current, status):
    ref = db.reference("sensor_data")
    ref.push({
        "temperature": temp,
        "water": water,
        "current": current,
        "status": status
    })
