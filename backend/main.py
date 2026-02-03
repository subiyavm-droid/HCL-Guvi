from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

app = FastAPI(
    title="SME Financial Health API",
    docs_url="/docs",
    openapi_url="/openapi.json"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("backend/credit_risk_dataset.csv")

ID_COL = df.columns[0]

NUMERIC_COLS = df.select_dtypes(include=np.number).columns.tolist()

if not NUMERIC_COLS:
    raise RuntimeError("No numeric columns found in dataset")

CREDIT_COL = NUMERIC_COLS[0]  # safe fallback

@app.get("/")
def root():
    return {"message": "SME Financial Health API Running"}

@app.get("/business_ids")
def get_business_ids():
    return df[ID_COL].astype(str).unique().tolist()

@app.get("/analyze/{business_id}")
def analyze_sme(business_id: str):
    row = df[df[ID_COL].astype(str) == business_id]

    if row.empty:
        raise HTTPException(status_code=404, detail="Business ID not found")

    credit_value = float(row[CREDIT_COL].values[0])

    # Normalize logic for demo
    risk = "Low Risk" if credit_value >= df[CREDIT_COL].median() else "High Risk"

    return {
        "business_id": business_id,
        "credit_metric_used": CREDIT_COL,
        "credit_value": round(credit_value, 2),
        "risk_level": risk,
        "recommendation": (
            "Eligible for MSME loan"
            if risk == "Low Risk"
            else "Improve financial ratios & cash flow"
        )
    }

