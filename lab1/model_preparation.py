import os 
import pickle 
import pandas as pd 
 
from sklearn.ensemble import RandomForestRegressor 
 
def load_data(file_path): 
    return pd.read_csv(file_path) 
 
def save_model(model, file_path): 
    with open(file_path, 'wb') as f: 
        pickle.dump(model, f) 
 
def train_model(X_train, y_train): 
    model = RandomForestRegressor() 
    model.fit(X_train, y_train) 
    return model 
 
def main(): 
    base_dir = ''  # Укажите базовую директорию, где находятся ваши данные 
 
    # Загрузка предобработанных данных 
    X_train = load_data(os.path.join(base_dir, 'train', 'data_train_preprocessed.csv')) 
    y_train = load_data(os.path.join(base_dir, 'train', 'temp_train_preprocessed.csv')) 
 
    # Обучение модели 
    model = train_model(X_train, y_train) 
 
    # Сохранение модели 
    save_model(model, os.path.join(base_dir, 'model.pkl')) 
 
if name == '__main__': 
    main()
