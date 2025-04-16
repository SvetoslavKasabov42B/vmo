from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Зареждане на данните
digits = datasets.load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target

# Разделяне на данните
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Списък от класификатори
classifiers = [
    KNeighborsClassifier(n_neighbors=3),
    KNeighborsClassifier(n_neighbors=5),
    KNeighborsClassifier(n_neighbors=7),
    SVC(kernel='linear'),
    SVC(kernel='poly'),
    SVC(kernel='rbf'),
    MLPClassifier(hidden_layer_sizes=(64, 32)),
    MLPClassifier(hidden_layer_sizes=(128, 64)),
    MLPClassifier(hidden_layer_sizes=(256, 128)),
]

# Имена за диаграмата
classifiers_names = [
    'k-NN (k=3)', 'k-NN (k=5)', 'k-NN (k=7)',
    'SVM (linear)', 'SVM (poly)', 'SVM (RBF)',
    'MLP (64,32)', 'MLP (128,64)', 'MLP (256,128)'
]

# Обучение и оценка
accuracies = []
for i, classifier in enumerate(classifiers):
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f"{classifiers_names[i]} accuracy: {accuracy}")

# Визуализация
plt.figure(figsize=(10, 6))
plt.bar(classifiers_names, accuracies, color='skyblue')
plt.xticks(rotation=90)
plt.ylabel('Accuracy')
plt.title('Comparison of Classifier Accuracies (MNIST Digits)')
plt.tight_layout()
plt.show()

