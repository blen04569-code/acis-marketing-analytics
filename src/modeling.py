import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_and_evaluate_regressors(X_train, X_test, y_train, y_test):
    """
    Trains and evaluates Linear Regression, Random Forest, and XGBoost models.
    Includes explicit error handling for mismatched structural dimensions.
    """
    # Defensive Engineering: Ensure dataset arrays align correctly
    if X_train.shape[0] != y_train.shape[0]:
        raise ValueError(f"❌ Matrix Shape Mismatch: X_train has {X_train.shape[0]} rows, but y_train has {y_train.shape[0]} labels.")

    # Initialize architectures
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
        "XGBoost Regressor": XGBRegressor(n_estimators=100, learning_rate=0.05, random_state=42)
    }
    
    results = []
    trained_models = {}
    
    print("🚀 Initiating Model Training and Evaluation Pipeline...")
    
    for name, model in models.items():
        try:
            # Fit model
            model.fit(X_train, y_train)
            trained_models[name] = model
            
            # Predict & Score
            predictions = model.predict(X_test)
            rmse = np.sqrt(mean_squared_error(y_test, predictions))
            r2 = r2_score(y_test, predictions)
            
            results.append({
                "Model Architecture": name,
                "Test RMSE": round(rmse, 4),
                "Coefficient of Determination (R²)": round(r2, 4)
            })
            print(f"  ✅ {name} trained successfully.")
            
        except Exception as e:
            print(f"  ❌ Failed training on {name}. Error details: {e}")
            results.append({
                "Model Architecture": name,
                "Test RMSE": "FAILED",
                "Coefficient of Determination (R²)": "FAILED"
            })
            
    return pd.DataFrame(results), trained_models