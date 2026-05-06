import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset

data = pd.read_csv('../../dataset/student_behavior.csv')

X = data[[
    'switches',
    'scroll_speed',
    'notifications',
    'focus_duration'
]]

y = data['label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, predictions))

joblib.dump(model, 'distraction_model.pkl')