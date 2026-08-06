import requests
import time
import joblib

TOKEN = "vPcZXGJuQzQkNT0MVp3BENxOsyYI6Xz9"

print("Loading model...")

model = joblib.load("driver_model.pkl")
encoder = joblib.load("label_encoder.pkl")

print("Model Loaded")

last_prediction = ""
last_health = -1
last_maintenance = ""

while True:

    try:

        # =========================
        # READ FROM BLYNK
        # =========================

        speed = int(float(requests.get(
            f"https://blynk.cloud/external/api/get?token={TOKEN}&V0"
        ).text))

        battery = int(float(requests.get(
            f"https://blynk.cloud/external/api/get?token={TOKEN}&V3"
        ).text))

        left = int(float(requests.get(
            f"https://blynk.cloud/external/api/get?token={TOKEN}&V4"
        ).text))

        right = int(float(requests.get(
            f"https://blynk.cloud/external/api/get?token={TOKEN}&V5"
        ).text))

        brake = int(float(requests.get(
            f"https://blynk.cloud/external/api/get?token={TOKEN}&V6"
        ).text))

        reverse = int(float(requests.get(
            f"https://blynk.cloud/external/api/get?token={TOKEN}&V7"
        ).text))

        # =========================
        # DRIVER BEHAVIOUR ML
        # =========================

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

        # =========================
        # PREDICTIVE MAINTENANCE
        # =========================

        health_score = 100

        # Battery impact
        if battery < 50:
            health_score -= 20

        if battery < 30:
            health_score -= 20

        # Driving style impact
        if driving_style == "aggressive":
            health_score -= 15

        elif driving_style == "reckless":
            health_score -= 30

        # Brake usage impact
        if brake == 1:
            health_score -= 5

        # Limit between 0 and 100
        health_score = max(0, min(100, health_score))

        # Maintenance recommendation
        if health_score >= 80:
            maintenance_status = "Healthy"

        elif health_score >= 50:
            maintenance_status = "Service Soon"

        else:
            maintenance_status = "Immediate Maintenance Required"

        # =========================
        # DISPLAY IN TERMINAL
        # =========================

        print("\n--------------------------------")
        print("Speed:", speed)
        print("Battery:", battery)
        print("Left:", left)
        print("Right:", right)
        print("Brake:", brake)
        print("Reverse:", reverse)

        print("Driving Style:", driving_style)

        print("Vehicle Health:", health_score)
        print("Maintenance:", maintenance_status)

        # =========================
        # UPDATE BLYNK
        # =========================

        if driving_style != last_prediction:

            requests.get(
                f"https://blynk.cloud/external/api/update?token={TOKEN}&V8={driving_style}"
            )

            last_prediction = driving_style

        if health_score != last_health:

            requests.get(
                f"https://blynk.cloud/external/api/update?token={TOKEN}&V9={health_score}"
            )

            last_health = health_score

        if maintenance_status != last_maintenance:

            requests.get(
                f"https://blynk.cloud/external/api/update?token={TOKEN}&V10={maintenance_status}"
            )

            last_maintenance = maintenance_status

        time.sleep(2)

    except Exception as e:

        print("ERROR:", e)
        time.sleep(2)