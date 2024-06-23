import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
base_dir = ''  # Укажите базовую директорию, где находятся ваши данные
# Загрузка предобработанных данных
X_train = pd.read_csv(os.path.join(base_dir, 'train', 'data_train_preprocessed.csv'))
y_train = pd.read_csv(os.path.join(base_dir, 'train', 'temp_train_preprocessed.csv'))
# Обучение модели
model = RandomForestRegressor()
model.fit(X_train, y_train)
# Сохранение модели
with open(os.path.join(base_dir, 'model.pkl'), 'wb') as f:
    pickle.dump(model, f)
