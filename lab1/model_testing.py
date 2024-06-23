import os 
import pickle 
import pandas as pd 
from sklearn.metrics import mean_squared_error 
from sklearn.ensemble import RandomForestRegressor 
 
base_dir = ''  # Укажите базовую директорию, где находятся ваши данные 
 
# Загрузка тестовых данных 
X_test = pd.read_csv(os.path.join(base_dir, 'test', 'data_test_preprocessed.csv')) 
y_test = pd.read_csv(os.path.join(base_dir, 'test', 'temp_test_preprocessed.csv')).values.ravel() 
 
# Загрузка обученной модели 
with open(os.path.join(base_dir, 'model.pkl'), 'rb') as f: 
    model = pickle.load(f) 
 
# Тестирование модели 
y_pred = model.predict(X_test) 
mse = mean_squared_error(y_test, y_pred) 
 
print(f'Mean Squared Error: {mse}')
