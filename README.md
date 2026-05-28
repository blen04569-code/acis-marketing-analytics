## <div>Task 2: Data Version Control (DVC)</div>
This project utilizes **DVC** to manage large data assets independently from source control. 

- **Local Remote Vault:** `C:\Users\Public\Documents\dvc_local_storage`
- **Tracked Artifacts:** `insurance_data.csv` (managed via `insurance_data.csv.dvc`)

To pull the dataset into your local workspace after cloning:
```bash
dvc pull
### Step 3: Push the Final Documentation to GitHub
Save your README update and push the absolute final version of Task 2 to your repository:

```bash
# 1. Stage the updated README
git add README.md

# 2. Commit the documentation update
git commit -m "docs: finalize task-2 DVC infrastructure documentation"

# 3. Push it to GitHub
git push origin task-2
## 🛠️ Data Engineering & CI/CD Infrastructure

### 📦 Data Version Control (DVC)
To maintain clean repository hygiene and handle large-scale financial records without bloating Git tracking histories, this project utilizes **DVC**.
* **Data Tracking:** Large source datasets are cached locally and tracked via secure `.dvc` pointer metadata files.
* **To reproduce the local data environment:** Ensure you have the remote repository credentials configured, then run:
  ```bash
  dvc pull