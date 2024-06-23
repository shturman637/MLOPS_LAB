# Импорт необходимых библиотек 
import numpy as np 
import pandas as pd 
import os 
 
# Установка seed для воспроизводимости 
np.random.seed(0) 
 
# Генерация данных о температуре 
num_days = 365 
noise_level = 2.0 
days = np.arange(num_days) 
temperatures = 10 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, noise_level, num_days) 
 
# Создание DataFrame 
data = pd.DataFrame({'day': days, 'temperature': temperatures}) 
 
# Проверка и создание папок 
os.makedirs(os.path.join('train'), exist_ok=True) 
os.makedirs(os.path.join('test'), exist_ok=True) 
 
# Разбиение данных на train и test 
split_ratio = 0.8 
train_size = int(len(data) * split_ratio) 
train_data = data.iloc[:train_size] 
test_data = data.iloc[train_size:] 
 
# Сохранение файлов 
base_dir = '' 
train_data.to_csv(os.path.join('train', 'data_train.csv'), index=False) 
test_data.to_csv(os.path.join('test', 'data_test.csv'), index=False)# Импорт необходимых библиотек 
import numpy as np 
import pandas as pd 
import os 
 
# Установка seed для воспроизводимости 
np.random.seed(0) 
 
# Генерация данных о температуре 
num_days = 365 
noise_level = 2.0 
days = np.arange(num_days) 
temperatures = 10 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, noise_level, num_days) 
 
# Создание DataFrame 
data = pd.DataFrame({'day': days, 'temperature': temperatures}) 
 
# Проверка и создание папок 
os.makedirs(os.path.join('train'), exist_ok=True) 
os.makedirs(os.path.join('test'), exist_ok=True) 
 
# Разбиение данных на train и test 
split_ratio = 0.8 
train_size = int(len(data) * split_ratio) 
train_data = data.iloc[:train_size] 
test_data = data.iloc[train_size:] 
 
# Сохранение файлов 
base_dir = '' 
train_data.to_csv(os.path.join('train', 'data_train.csv'), index=False) 
test_data.to_csv(os.path.join('test', 'data_test.csv'), index=False)
