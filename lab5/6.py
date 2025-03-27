import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Дефиниране на данните
data = {
    'Length': [248, 180, 120, 200, 75, 320, 150, 280, 90],
    'Frequency': [2, 3, 1, 4, 1, 5, 2, 3, 1],
    'Size': [22, 16, 8, 20, 6, 30, 12, 24, 5],
    'Category': ['спам', 'спам', 'не-спам', 'спам', 'не-спам', 'спам', 'не-спам', 'спам', 'не-спам']
}

df = pd.DataFrame(data)

# 8. Преобразуване на категориите в числови стойности
df['Category'] = df['Category'].map({'спам': 1, 'не-спам': 0})

# 9. Разделяне на входни данни (X) и изходни категории (y)
X = df[['Length', 'Frequency', 'Size']]
y = df['Category']

# 10. Разделяне на тренировъчни и тестови данни
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 11. Създаване и обучение на логистичния регресионен модел
model = LogisticRegression()
model.fit(X_train, y_train)

# 27. Прогноза за ново писмо
new_email = np.array([[150, 2, 12]])  # Входни данни за ново писмо
predicted_category = model.predict(new_email)

# 28. Извеждане на резултата
print("Категория на новото писмо:", "спам" if predicted_category[0] == 1 else "не-спам")

# 36. Изчисляване и извеждане на точността на модела
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Точност на модела: {accuracy:.2%}")

