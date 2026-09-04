# Telco Customer Churn Prediction Pipeline

This repository contains an end-to-end machine learning pipeline to analyze and predict customer churn using the IBM Telco Customer Churn dataset. The goal of this project is to identify high-risk customers and uncover the primary drivers behind customer loss to inform targeted retention strategies.

## 📌 Project Overview
Customer churn is a critical metric for subscription-based telecom businesses. This is because it is far more expensive to acquire a new customer than to retain an existing one. This project utilizes historical customer data to build a predictive model that estimates the likelihood of a customer leaving (`Churn = Yes`).

---
## Generative AI Usage & Disclosure

Generative AI (e.g., ChatGPT / Claude) was utilized throughout this project to support both technical development and communication:

* **Data Storytelling & Summarization:** AI was used to draft executive summaries, structure business insights, and translate complex statistical churn drivers into actionable recommendations for non-technical stakeholders.
* **Narrative Synthesis:** Assisted in refining the flow and tone of the analytical narrative across the project's final documentation and notebook markdown cells.
* **Code Optimization & Troubleshooting:** Used as a thought partner for debugging data pipelines and refining feature engineering scripts.

## 📊 Dataset Metadata
* **Source:** IBM Sample Datasets (Telco Customer Churn)
* **Format:** CSV
* **Target Variable:** `Churn` (Yes/No - Indicating if the customer left within the last month)

---

### Data Dictionary

| Column Name | Data Type (Raw) | Description |
| :--- | :--- | :--- |
| `customerID` | Object / String | Unique identifier for each customer (Dropped during modeling) |
| `gender` | Object | Customer gender (Male, Female) |
| `SeniorCitizen` | Integer | Indicates if the customer is a senior citizen (1, 0) |
| `Partner` | Object | Whether the customer has a partner (Yes, No) |
| `Dependents` | Object | Whether the customer has dependents (Yes, No) |
| `tenure` | Integer | Number of months the customer has stayed with the company |
| `PhoneService` | Object | Whether the customer has phone service (Yes, No) |
| `MultipleLines` | Object | Whether the customer has multiple lines (Yes, No, No phone service) |
| `InternetService` | Object | Customer’s internet service provider (DSL, Fiber optic, No) |
| `OnlineSecurity` | Object | Whether the customer has online security (Yes, No, No internet service) |
| `OnlineBackup` | Object | Whether the customer has online backup (Yes, No, No internet service) |
| `DeviceProtection` | Object | Whether the customer has device protection (Yes, No, No internet service) |
| `TechSupport` | Object | Whether the customer has tech support (Yes, No, No internet service) |
| `StreamingTV` | Object | Whether the customer has streaming TV (Yes, No, No internet service) |
| `StreamingMovies` | Object | Whether the customer has streaming movies (Yes, No, No internet service) |
| `Contract` | Object | The contract term of the customer (Month-to-month, One year, Two year) |
| `PaperlessBilling` | Object | Whether the customer has paperless billing (Yes, No) |
| `PaymentMethod` | Object | The customer's payment method (Electronic check, Mailed check, etc.) |
| `MonthlyCharges` | Float | The amount charged to the customer monthly |
| `TotalCharges` | Object / Float | The total amount charged to the customer |


## **Project Implementation Plan**

### **Phase 1: Setup & Data Acquisition** *(Estimated Duration: Week 1)*
Establish environment, repository structure, and initial data exploration.
* **Repository Setup:** Structure project directories (`data/`, `notebooks/`, `models/`, `app/`,`plots/`).
* **Data Collection:** Ingest telecom dataset (e.g., Telco Customer Churn - ~7,043 rows, 21 features).
* **Environment:** Define dependencies (`pandas`, `scikit-learn`, `streamlit`, `joblib`, `pytest`).

### **Phase 2: EDA & Feature Engineering** *(Estimated Duration: Weeks 2–3)*
Clean, analyse, and transform features for model training.
* **Data Cleaning:** Handle missing values (e.g., `TotalCharges` space strings) and drop non-informative IDs (`customerID`).
* **Feature Transformation:** Apply One-Hot Encoding (`InternetService`, `PaymentMethod`), numeric binning (`tenure`, `MonthlyCharges`), and standard scaling.

### **Phase 3: Model Development & Evaluation** *(Estimated Duration: Weeks 4–5)*
Train classifiers, tune hyperparameters, and evaluate business metrics.
* **Model Experiments:** Train Logistic Regression, Random Forest, and XGBoost baselines.
* **Evaluation:** Measure Precision, Recall (maximizing churn capture), ROC-AUC (> 0.88 target), and Confusion Matrix tradeoffs.
* **Serialization:** Export tuned models and scaler pipelines to `artifacts/`.

### **Phase 4: Implementation & Deployment** *(Estimated Duration: Weeks 6–7)*
Build the user interface and deploy the real-time inference system into production.
* **API / Web Application:** Develop interactive frontend (Streamlit) or REST endpoints (FastAPI) for inputting customer profiles.
* **CI/CD Pipeline:** Configure GitHub Actions for automated unit testing (`pytest`) and linting on push.
* **Hosting:** Deploy app to Streamlit

### **Phase 5: Post-Deployment Evaluation** *(Estimated Duration: Week 8)*
Assess real-world model accuracy and evaluate retention business impact.
* **Business Validation:** Compare predicted high-risk churners against actual customer retention outcomes following marketing intervention.

### **Phase 6: Maintenance & Performance Monitoring** *(Estimated Duration: Ongoing)*
Monitor operational health and detect data/concept drift.
* **Drift Monitoring:** Monitor shifts in feature distributions (Data Drift) or changes in customer churn behavior (Concept Drift).
* **System Health:** Track API latency, uptime, resource utilisation, and prediction throughput.
* **Alerting:** Set automated notifications (e.g., via Slack or email) if key metric thresholds (ROC-AUC drop > 5%) are breached.

### **Phase 7: Model Updates & Retraining** *(Estimated Duration: Periodic - Quarterly / As Needed)*
Keep the model aligned with changing customer behavior and business offerings.
* **Scheduled Retraining:** Re-train models periodically using newly labeled ground-truth customer data.
* **Trigger-Based Retraining:** Automatically run retraining pipelines when drift alerts are triggered.
* **Champion-Challenger Testing:** Benchmark newly trained models ("Challengers") against the live deployed model ("Champion") before shadow deployment.
---

## ⚙️ Pipeline Architecture

The workflow is broken down into structured notebook phases:

1. **`01_data_cleaning.ipynb`**
   * Coerces `TotalCharges` into a numeric format.
   * Handles missing values generated by zero-tenure rows.
   * Drops non-predictive features (`customerID`).

2. **`02_eda.ipynb`**
   * Computes baseline churn rates.
   * Explores relationships between contract terms, internet service types, and churn rates.
   * Identifies multicollinearity via correlation heatmaps.
   * Display charts on Power BI for interactive dashboarding

3. **`03_data_transformation.ipynb`**
   * One-hot encodes multi-class categorical features.
   * Binary encodes flags (`Yes`/`No`).
   * Scales continuous features (`tenure`, `MonthlyCharges`) using standard scaling.

4. **`04_predictive_modelling.ipynb`**
   * Splits data into Stratified Train/Test sets.
   * Handles class imbalance using SMOTE or class-weight balancing.
   * Trains and optimizes Logistic Regression, Random Forest, and XGBoost models.
   * Evaluates performance based on **Recall** and **ROC-AUC**.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.8+ installed. Clone this repository and install the dependencies:

```bash
git clone [https://github.com/Joyy-cloud/TelecomChurning.git](https://github.com/Joyy-cloud/TelecomChurning.git)
cd TelecomChurning
pip install -r requirements.txt