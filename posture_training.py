import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from micromlgen import port

# -----------------------------
# Load Dataset
# -----------------------------
data_raw = pd.read_csv("posture.csv", header=None)
# The first row contains the actual column names
new_columns = data_raw.iloc[0]
# Explicitly make a copy to avoid SettingWithCopyWarning
data = data_raw[1:].copy()
data.columns = new_columns  # Assign column names
# Ensure numeric columns are of the correct type
data[['GX', 'GY', 'GZ']] = data[['GX', 'GY', 'GZ']].astype(float)
print("Dataset Preview:")
print(data.head())

# -----------------------------
# Handle NaN values
# -----------------------------
data.dropna(inplace=True)

# -----------------------------
# Features and Labels
# -----------------------------
X = data[['GX', 'GY', 'GZ']]
y = data['Posture']

# -----------------------------
# Split Data into Training and Test Sets
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTraining set size: {len(X_train)} samples")
print(f"Test set size: {len(X_test)} samples")

# -----------------------------
# Train Model
# -----------------------------
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print("\nModel training completed on training data!")

# -----------------------------
# Evaluate Model on Test Data
# -----------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy:.2f}")

# -----------------------------
# Test Predictions (using the full trained model, not ideal for rigorous evaluation but for demonstration)
# -----------------------------
print("\nTesting predictions with example data points:")
print("Forward Test:", model.predict([[3500, 200, 100]])[0])
print("Backward Test:", model.predict([[-3500, 100, 50]])[0])
print("Left Test:", model.predict([[100, -4000, 30]])[0])
print("Right Test:", model.predict([[200, 4000, 40]])[0])
print("Twist Test:", model.predict([[100, 200, 3500]])[0])

# -----------------------------
# Export Model for Arduino / ESP32
# -----------------------------
c_code = port(model)
with open("posture_model.h", "w") as f:
    f.write(c_code)
print("\nModel exported successfully as posture_model.h")
