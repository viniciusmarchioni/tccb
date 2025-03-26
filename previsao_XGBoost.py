import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

import warnings


# Função para prever resultado de uma nova partida
def prever_resultado(mandante:str,visitante:str,form_mandante:str,form_visitante:str,cond_1:str,momento_dia:str,):
    warnings.simplefilter("ignore", UserWarning)
    # Carregar modelo, encoders e scaler
    modelo = joblib.load("modelo_xgboost_V2.pkl")
    label_encoders = joblib.load("encoders_xgb.pkl")
    scaler = joblib.load("scaler_xgb.pkl")


    # Lista de colunas categóricas
    categorical_columns = ['mandante', 'visitante', 'formacao_mandante', 'formacao_visitante', 'condicao_1', 'condicao_2', 'momento_dia']

    #print("\n==== Previsão de Resultado - Modelo XGBoost ====")
    mandante = mandante
    visitante = visitante
    form_mandante = form_mandante
    form_visitante = form_visitante
    cond_1 = cond_1
    momento_dia = momento_dia
    cond_2 = "Nenhuma"  # valor padrão para condicao_2

    # Montar DataFrame de entrada
    dados = pd.DataFrame([{ 
        'mandante': mandante,
        'visitante': visitante,
        'formacao_mandante': form_mandante,
        'formacao_visitante': form_visitante,
        'condicao_1': cond_1,
        'condicao_2': cond_2,
        'momento_dia': momento_dia
    }])

    # Aplicar Label Encoding
    for col in categorical_columns:
        le = label_encoders[col]
        if dados[col][0] not in le.classes_:
            le.classes_ = list(le.classes_) + [dados[col][0]]
        dados[col] = le.transform(dados[col])

    # Normalizar os dados
    dados_scaled = pd.DataFrame(scaler.transform(dados), columns=dados.columns)

    # Fazer predição
    probs = modelo.predict_proba(dados_scaled)[0]


    return probs[0],probs[1],probs[2]
    print("\n>>> Probabilidades de resultado:")
    print(f"Empate: {probs[0]:.2%}")
    print(f"Vitória do mandante: {probs[1]:.2%}")
    print(f"Vitória do visitante: {probs[2]:.2%}")
