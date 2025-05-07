import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
 

# Replace this with the path to your dataset
data_file_path = 'aggregated_data.csv'

# Load the dataset
df = pd.read_csv(data_file_path)

# Data Preprocessing
# Check for missing values and handle them (e.g., by filling or dropping)
df.fillna(0, inplace=True)  # Example: fill missing values with 0

# Define features (X) and target variable (y)
# Features can include total amount, fraud count, etc.
X = df[['Total Amount', 'Fraud Count']]  # Add more features as needed
y = df['Fraudulent'].map({'No': 0, 'Yes': 1})  # Map 'Yes' to 1 (fraud) and 'No' to 0 (non-fraud)

# Data scaling for numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the RandomForestClassifier model
rf_model = RandomForestClassifier(random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# AUC-ROC score for model evaluation
y_prob = rf_model.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class
auc_score = roc_auc_score(y_test, y_prob)
print(f"AUC-ROC Score: {auc_score:.4f}")

# Save the trained model using joblib for future use
model_filename = 'fraud_detection_model.pkl'
joblib.dump(rf_model, model_filename)
print(f"Model saved as {model_filename}")

# Save the scaler for future data scaling
scaler_filename = 'scaler.pkl'
joblib.dump(scaler, scaler_filename)
print(f"Scaler saved as {scaler_filename}")
