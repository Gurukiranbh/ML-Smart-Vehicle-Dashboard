print("SCRIPT STARTED")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

print("Loading dataset...")

df = pd.read_csv("driver_data.csv")

print(df.head())

X = df.drop("label", axis=1)
y = df["label"]

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Accuracy =", accuracy)

joblib.dump(model, "driver_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("Model Saved Successfully")