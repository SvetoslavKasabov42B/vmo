import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc
from scipy.stats import shapiro

# Зареждане на данните
data = load_breast_cancer()
X = data.data
y = data.target

# Тест на Шапиро-Уилк
stat, p = shapiro(X)
print('Shapiro-Wilk Test: Statistics=%.3f, p-value=%.3f' % (stat, p))
if p > 0.05:
    print("Data has a normal distribution")
else:
    print("Data does not have a normal distribution")

# Разделяне на данните
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Класификация
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)

# Метрики
accuracy = accuracy_score(y_test, y_pred)
error = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
fpr, tpr, _ = roc_curve(y_test, y_pred)
roc_auc = auc(fpr, tpr)

# Резултати
print("\nРЕЗУЛТАТИ:")
print("Gaussian Naive Bayes Classifier Metrics:")
print("Accuracy:", accuracy)
print("Classification Error:", error)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", confusion_mat)
print("ROC AUC Score:", roc_auc)

# ROC крива
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Breast Cancer Classification')
plt.legend(loc="lower right")
plt.show()

