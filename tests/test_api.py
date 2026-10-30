from pathlib import Path

import joblib
import pytest
from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)

VALID_CUSTOMER = {
    "tenure_months": 12,
    "monthly_fee": 70.0,
    "contract": "month-to-month",
    "internet_service": "fiber",
    "support_calls": 3,
}


def test_api_contract():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    response = client.post("/predict", json=VALID_CUSTOMER)
    assert response.status_code == 200
    assert "churn_probability" in response.json()


def test_model_loads():
    model_path = Path(__file__).resolve().parents[1] / "model.joblib"
    model = joblib.load(model_path)
    assert hasattr(model, "predict_proba")


def test_input_schema():
    invalid_customer = VALID_CUSTOMER.copy()
    invalid_customer["tenure_months"] = -5

    response = client.post("/predict", json=invalid_customer)
    assert response.status_code == 422


def test_edge_case():
    customer = VALID_CUSTOMER.copy()
    customer["tenure_months"] = 0
    customer["support_calls"] = 0

    response = client.post("/predict", json=customer)
    assert response.status_code == 200
    assert 0 <= response.json()["churn_probability"] <= 1


def test_deterministic_prediction():
    response1 = client.post("/predict", json=VALID_CUSTOMER)
    response2 = client.post("/predict", json=VALID_CUSTOMER)

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json() == response2.json()