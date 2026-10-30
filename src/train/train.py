from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import f1_score, roc_auc_score

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "lab1-starter" / "churn_v2.csv"
MODEL_PATH = ROOT / "model.joblib"

numeric = ["tenure_months", "monthly_fee", "support_calls"]
categorical = ["contract", "internet_service"]

df = pd.read_csv(DATA_PATH)
X = df[numeric + categorical]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ("prep", ColumnTransformer([
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
    ])),
    ("clf", LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)

proba = model.predict_proba(X_test)[:, 1]
print("F1:", round(f1_score(y_test, proba > 0.5), 3))
print("AUC:", round(roc_auc_score(y_test, proba), 3))

joblib.dump(model, MODEL_PATH)
print("Saved model.joblib successfully!")