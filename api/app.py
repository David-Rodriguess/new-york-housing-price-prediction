from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI(
    title="API de Previsão de Preços de Imóveis",
    description="Modelo de ML para previsão de preços imobiliários",
    version="1.0"
)

# 🔹 carregamento do modelo
modelo = joblib.load("../models/modelo_preco_imoveis.joblib")


class Imovel(BaseModel):
    BEDS: int
    BATH: int
    PROPERTYSQFT: float
    LOCALITY: str
    TYPE: str


@app.post("/predict")
def predict(imovel: Imovel):
    # 1️⃣ dados crus
    df = pd.DataFrame([imovel.dict()])

    # 2️⃣ feature engineering (ANTES do predict)
    df["BATH_PER_BED"] = df["BATH"] / df["BEDS"]
    df["BEDS_PER_SQFT"] = df["BEDS"] / df["PROPERTYSQFT"]

    # 3️⃣ previsão
    preco_pred = modelo.predict(df)[0]

    return {
        "preco_previsto": round(float(preco_pred), 2)
    }
