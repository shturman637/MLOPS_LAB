import osimport pandas as pd
from sklearn.preprocessing import StandardScaler
# Укажите базовую директорию, где находятся ваши данныеbase_dir = ''
# Загрузка данных
train_data = pd.read_csv(os.path.join(base_dir, 'train', 'data_train.csv'))test_data = pd.read_csv(os.path.join(base_dir, 'test', 'data_test.csv'))
# Определяем признаки и целевую переменную
X_train = train_data.drop(columns=['temperature'])y_train = train_data['temperature']
X_test = test_data.drop(columns=['temperature'])y_test = test_data['temperature']
# Отделяем числовые признаки для стандартизации
numerical_features = X_train.select_dtypes(include=['float64', 'int64']).columns
# Стандартизируем числовые признакиscaler = StandardScaler()
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])X_test[numerical_features] = scaler.transform(X_test[numerical_features])
# Сохранение предобработанных данных
X_train.to_csv(os.path.join(base_dir, 'train', 'data_train_preprocessed.csv'), index=False)X_test.to_csv(os.path.join(base_dir, 'test', 'data_test_preprocessed.csv'), index=False)
y_train.to_csv(os.path.join(base_dir, 'train', 'temp_train_preprocessed.csv'), index=False)y_test.to_csv(os.path.join(base_dir, 'test', 'temp_test_preprocessed.csv'), index=False)
