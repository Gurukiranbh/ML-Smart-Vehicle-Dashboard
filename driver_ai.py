import requests
import time
import joblib

# =====================================
# BLYNK TOKEN
# =====================================

TOKEN = "vPcZXGJuQzQkNT0MVp3BENxOsyYI6Xz9"

# =====================================
# LOAD MODEL
# =====================================

print("Loading model...")

model = joblib.load("driver_model.pkl")
encoder = joblib.load("label_encoder.pkl")

print("Model Loaded")

# =====================================
# TEST INPUT
# =====================================

speed = 60
brake = 0
left = 0
right = 0
reverse = 0
battery = 80

last_prediction = ""

# =====================================
# MAIN LOOP
# =====================================

while True:

    sample = [[
        speed,
        brake,
        left,
        right,
        reverse,
        battery
    ]]

    prediction = model.predict(sample)

    driving_style = encoder.inverse_transform(prediction)[0]

    if driving_style != last_prediction:

        url = (
            f"https://blynk.cloud/external/api/update"
            f"?token={TOKEN}"
            f"&V8={driving_style}"
        )

        r = requests.get(url)

        print("Status:", r.status_code)
        print("Response:", r.text)
        print("Driving Style:", driving_style)

        last_prediction = driving_style

    time.sleep(2)