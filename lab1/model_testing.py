
import os 
import pickle 
import pandas as pd 
from sklearn.metrics import mean_squared_error, r2_score 
 
# Загрузка данных 
def load_data(file_path): 
    return pd.read_csv(file_path) 
 
# Загрузка модели 
def load_model(file_path): 
    with open(file_path, 'rb') as f: 
        model = pickle.load(f) 
    return model 
 
# Тестирование модели 
def test_model(model, X_test, y_test): 
    y_pred = model.predict(X_test) 
    mse = mean_squared_error(y_test, y_pred) 
     
    print(f'Mean Squared Error: {mse}') 
     
 
def main(): 
    base_dir = ''  # Укажите базовую директорию, где находятся ваши данные 
 
    # Загрузка тестовых данных 
    X_test = load_data(os.path.join(base_dir, 'test', 'data_test_preprocessed.csv')) 
    y_test = load_data(os.path.join(base_dir, 'test', 'temp_test_preprocessed.csv')) 
 
    # Загрузка обученной модели 
    model = load_model(os.path.join(base_dir, 'model.pkl')) 
 
    # Тестирование модели 
    test_model(model, X_test, y_test) 
 
if name == '__main__': 
    main()
