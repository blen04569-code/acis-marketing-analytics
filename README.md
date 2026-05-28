Markdown

# 📊 ACIS Insurance Marketing & Risk Analytics Pipeline

An end-to-end data engineering and predictive machine learning pipeline designed to analyze historical automotive insurance policies, optimize premium pricing matrices, and evaluate risk feature dependencies.

---

## 🚀 Repository Architecture & Framework

This repository is built using production-grade MLOps and software engineering principles, prioritizing modularity, reproducibility, and robust error handling.

.
├── .github/workflows/    # CI/CD Automation Workflows
│   └── ci.yml            # GitHub Actions automated linting & testing suite
├── data/                 # Data directory (tracked securely via DVC)
│   └── insurance_data.csv.dvc
├── notebooks/            # Exploratory & Modeling Interfaces
│   ├── 01_EDA.ipynb
│   ├── 03_hypothesis_testing.ipynb
│   └── 04_statistical_modeling.ipynb
├── src/                  # Modular Source Scripts (Reusable Modules)
│   ├── init.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── README.md
└── requirements.txt


---

## 🛠️ Core Infrastructure & Engineering Hygiene

### 📦 1. Data Version Control (DVC)
To prevent repository bloating and ensure strict reproducibility without pushing massive CSV tracking assets to GitHub, this project utilizes **DVC** backed by a remote storage cache.
* **Pointer Tracking:** Raw and processed insurance matrix datasets are tracked via `.dvc` metadata files.
* **Data Retrieval:** To seamlessly synchronize your local data state and pull down the exact matrices required for the notebooks, run:
  ```bash
  dvc pull

🤖 2. Continuous Integration (CI) Pipeline

Automated structural quality control is strictly enforced on this repository via GitHub Actions (.github/workflows/ci.yml). Upon opening a Pull Request or pushing to the main branch, the CI runner automatically triggers:

    Environment Setup: Initializes the runner and restores dependency caches.

    Dependency Resolution: Installs core libraries securely via requirements.txt.

    Linting & Code Style Compliance: Evaluates standard formatting conventions using python syntax checkers to ensure clean, readable peer contributions.

📈 Analytical Deliverables & Core Modules
🧪 Task 3: A/B Hypothesis Testing (src/hypothesis_tests.py)

Implements robust statistical tests verifying key risk discrepancies across distinct profiles. Features include:

    Chi-Square Goodness-of-Fit tests evaluating risk consistency across geographical provinces.

    Two-sample t-tests tracking premium margins across postal codes and gender divisions.

    Full business interpretations hardcoded directly into the analytical markdown wrappers.

🤖 Task 4: Statistical Modeling Suite (src/modeling.py)

Trains, validates, and compares tree-based ensemble architectures to forecast historical claim severity.

    Algorithms Deployed: Linear Regression, Random Forest Regressor, and XGBoost Regressor.

    Error Handling: Built-in array shape assertions and data type conversion modules (float64 casting) preventing downstream runtime pipeline crashes.

    Explainable AI (XAI): Integrated SHAP TreeExplainers to extract directional feature importances, explicitly proving the structural impacts of policy attributes on final predicted severity.






