import os 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
 
def load_data(file_path): 
    return pd.read_csv(file_path) 
 
def save_data(data, file_path): 
    data.to_csv(file_path, index=False) 
 
def preprocess_data(train_data, test_data): 
    # Определяем признаки и целевую переменную 
    X_train = train_data.drop(columns=['temperature']) 
    y_train = train_data['temperature'] 
    X_test = test_data.drop(columns=['temperature']) 
    y_test = test_data['temperature'] 
 
    # Отделяем числовые признаки для стандартизации 
    numerical_features = X_train.select_dtypes(include=['float64', 'int64']).columns 
 
    # Стандартизируем числовые признаки 
    scaler = StandardScaler() 
    X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features]) 
    X_test[numerical_features] = scaler.transform(X_test[numerical_features]) 
 
    return X_train, y_train, X_test, y_test 
 
def main(): 
    base_dir = ''  # Укажите базовую директорию, где находятся ваши данные 
 
    # Загрузка данных 
    train_data = load_data(os.path.join(base_dir, 'train', 'data_train.csv')) 
    test_data = load_data(os.path.join(base_dir, 'test', 'data_test.csv')) 
 
    # Предобработка данных 
    X_train, y_train, X_test, y_test = preprocess_data(train_data, test_data) 
 
    # Сохранение предобработанных данных 
    save_data(X_train, os.path.join(base_dir, 'train', 'data_train_preprocessed.csv')) 
    save_data(X_test, os.path.join(base_dir, 'test', 'data_test_preprocessed.csv')) 
    save_data(y_train, os.path.join(base_dir, 'train', 'temp_train_preprocessed.csv')) 
    save_data(y_test, os.path.join(base_dir, 'test', 'temp_test_preprocessed.csv')) 
if name == "__main__": 
    main()
