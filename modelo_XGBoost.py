import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Carregar o dataset
df = pd.read_csv(r"C:\Users\enzos\Documents\Programação\TCC\Datasets\dados_filtrados_com_clima.csv")

# Converter colunas categóricas em numéricas com Label Encoding
categorical_columns = ['mandante', 'visitante', 'formacao_mandante', 'formacao_visitante', 'condicao_1', 'condicao_2', 'momento_dia']
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Separar variáveis independentes (X) e variável alvo (y)
X = df.drop(columns=['resultado'])
y = df['resultado']

# Normalizar os dados numéricos
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Dividir os dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Definir o espaço de busca com 12 combinações (para 60 fits com 5 folds)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5],
    'learning_rate': [0.05, 0.1],
    'subsample': [0.8],
    'colsample_bytree': [0.8]
}

# Criar modelo base com balanceamento de classes
modelo_xgb = xgb.XGBClassifier(eval_metric='mlogloss', random_state=42, scale_pos_weight=None)

# Configurar Validação Cruzada com GridSearchCV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid_search = GridSearchCV(modelo_xgb, param_grid=param_grid, scoring='accuracy', cv=cv, verbose=1, n_jobs=-1, return_train_score=True)
grid_search.fit(X_train, y_train)

# Melhor modelo encontrado
best_model = grid_search.best_estimator_

# Avaliar a acurácia do modelo
y_pred_xgb = best_model.predict(X_test)
acuracia_xgb = accuracy_score(y_test, y_pred_xgb)
print("Melhores hiperparâmetros encontrados:", grid_search.best_params_)
print(f"Acurácia do modelo XGBoost otimizado: {acuracia_xgb:.2%}")
print(classification_report(y_test, y_pred_xgb, zero_division=0))

# Mostrar os piores hiperparâmetros (menor score)
results = pd.DataFrame(grid_search.cv_results_)
worst_index = results['mean_test_score'].idxmin()
worst_params = results.loc[worst_index, 'params']
worst_score = results.loc[worst_index, 'mean_test_score']
print("Piores hiperparâmetros encontrados:", worst_params)
print(f"Pior desempenho de validação cruzada: {worst_score:.2%}")

# Salvar o modelo treinado e pré-processadores
modelo_path = r"C:\Users\enzos\Documents\Programação\TCC\XGBoost\modelo_xgboost_V2.pkl"
joblib.dump(best_model, modelo_path)
joblib.dump(label_encoders, r"C:\Users\enzos\Documents\Programação\TCC\XGBoost\encoders_xgb.pkl")
joblib.dump(scaler, r"C:\Users\enzos\Documents\Programação\TCC\XGBoost\scaler_xgb.pkl")
print(f"Modelo treinado salvo em: {modelo_path}")