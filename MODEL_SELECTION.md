# Model Selection

## The question

The model predicts the probability that a customer will leave a telecom company (customer churn). Incorrect predictions may cause the company to miss customers who need retention support or spend resources on customers who are unlikely to leave.

## Candidates


### 1. Logistic Regression
- **Why I tried it:** Simple and fast baseline.
- **AUC:** 0.798
- **F1:** 0.495
- **Lowest slice F1:** 0.250
- **p95 latency:** 8.85 ms
- **Model size:** 3.55 KB
- **MLflow run ID:** `afaeb98a3adf426993f311cf3515c00a`

### 2. Random Forest
- **Why I tried it:** Captures nonlinear patterns.
- **AUC:** 0.759
- **F1:** 0.454
- **Lowest slice F1:** 0.220
- **p95 latency:** 35.64 ms
- **Model size:** 3160.10 KB
- **MLflow run ID:** `bb05f8c870814ac2995f7c2f92d0a4a1`

### 3. Gradient Boosting
- **Why I tried it:** Tests sequential boosting.
- **AUC:** 0.7476
- **F1:** 0.4167
- **Lowest slice F1:** 0.2222
- **p95 latency:** 9.1025 ms
- **Model size:** 141.6445 KB
- **MLflow run ID:** `60dbaaa675f94cada4b82308d694b930`


## The champion

I selected **Logistic Regression** as the champion because it achieved the highest overall F1 score (0.495) and AUC (0.798).

Its p95 prediction latency was approximately 8.85 ms, which is below the 25 ms latency budget. It was also the smallest model at approximately 3.55 KB.

Random Forest had a higher latency of 35.64 ms, exceeding the budget, while Gradient Boosting had a lower F1 score of 0.4167.

Logistic Regression was not perfect across all customer groups. Its lowest slice F1 was 0.250, so I accepted some variation in performance between contract types in exchange for better overall F1, lower latency, and a smaller model.

## My promotion rules

- **Latency budget (p95): 25 ms**, because the API should respond quickly, and models exceeding this threshold should not be deployed.
- **Minimum gain to replace the champion: 0.005 F1 points**, because a new model should demonstrate a measurable improvement before replacing the existing champion.

The promotion gate first filters candidates by latency, then selects the eligible model with the highest F1. It promotes the model only when its F1 improves by at least 0.005 over the current champion.

## What I would check next

I would monitor model performance for different contract types, especially groups with lower F1 scores. I would also monitor data drift because customer behavior may change over time and reduce the model's performance.