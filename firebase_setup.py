import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("C:/Users/user/Downloads/iot-ai-security-firebase-adminsdk-fbsvc-f23cc51222.json")

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
