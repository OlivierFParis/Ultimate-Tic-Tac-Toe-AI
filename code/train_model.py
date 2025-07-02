

import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# Loading training data
df = pd.read_csv("..\\training_X.csv")


# Separating features and labels
X = df.iloc[:, :-1] # The 81 board positions
y = df.iloc[:, -1]  # The following move made

# Train/test split to check accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
# model = RandomForestClassifier(n_estimators=100, random_state=42)
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"Validation Accuracy: {accuracy:.2f}")


# Save the trained model
joblib.dump(model, "model_X.pkl")
print("Model saved as model_X.pkl")



