import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    'дължина': [7, 10, 8, 9, 10],
    'широчина': [5, 4, 5, 5, 6],
    'височина': [5, 5, 5, 5, 5],
    'цена': [6.5, 6.55, 6.31, 5.51, 4.44],
})

X = df[['дължина','широчина','височина']]
y = df['цена']

model = LinearRegression().fit(X, y)

new_data = pd.DataFrame({
    'дължина': [7],
    'широчина': [6],
    'височина': [5],
})

predicted_price = model.predict(new_data)

print(f'Множествена линейна регресия на данните:')
print(f'Коефициент на детерминация: {model.score(X, y):.2f}')
print(f'Множествени коефициенти на регресия: {[f"{coef:.2f}" for coef in model.coef_]}')
print(f'Свободен член на регресията: {model.intercept_:.2f}')
print(f'Прогнозирана цена на дома: {predicted_price[0]:.2f}')

