import numpy as np 
import pandas as pd 
import os 
 
def generate_temperature_data(num_days, noise_level=0.5, anomaly=False): 
    np.random.seed(0) 
    days = np.arange(num_days) 
    temperatures = 10 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, noise_level, num_days)  
 
    return pd.DataFrame({'day': days, 'temperature': temperatures}) 
 
def save_datasets(base_dir, data, prefix, split_ratio=0.8): 
    # Проверяем наличие необходимых папок 
    os.makedirs(os.path.join('train'), exist_ok=True) 
    os.makedirs(os.path.join('test'), exist_ok=True) 
 
    # Разбиение данных на train и test 
    train_size = int(len(data) * split_ratio) 
    train_data = data.iloc[:train_size] 
    test_data = data.iloc[train_size:] 
 
    # Сохраняем файлы 
    train_data.to_csv(os.path.join('train', f'{prefix}_train.csv'), index=False) 
    test_data.to_csv(os.path.join('test', f'{prefix}_test.csv'), index=False) 
 
def main(): 
    base_dir = '' 
 
    # Генерация разных типов наборов данных 
    dataset_noisy_anomalies = generate_temperature_data(365, noise_level=2.0, anomaly=True) 
 
    # Сохранение наборов данных 
 
    save_datasets(base_dir, dataset_noisy_anomalies, 'data') 
 
if name == "__main__": 
    main()
