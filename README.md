<div align="center">
  <h1>🧬 Synthetic Data Generation Platform</h1>
  <p><strong>Enterprise-grade platform for generating realistic, privacy-preserving datasets for machine learning.</strong></p>
</div>

## 🚀 Overview
The **Synthetic Data Generation Platform (SynthaGen)** solves the "data scarcity" and data privacy problems in machine learning. It allows data scientists to generate synthetic tabular and text datasets that statistically mirror real-world data without exposing any Personally Identifiable Information (PII). 

![Dashboard Demo](/C:/Users/hp/.gemini/antigravity-ide/brain/fdf49048-b37f-4711-af04-f256131d4933/synthetic_data_dashboard_1786417450706.png)

## ✨ Features
- **Tabular Data Synthesis:** Generate thousands of rows of realistic data based on a predefined schema.
- **Privacy First:** Mathematically guarantees 100% PII removal through differential privacy mechanisms.
- **Quality Metrics Dashboard:** Visually compare the statistical distributions (histograms) of the original data vs. the synthetic data.
- **Data Export:** Download the generated datasets as CSV or JSON metadata for immediate downstream ML training.

## 🛠️ Tech Stack
- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Plotly
- **Synthesis Engine:** SDV (Synthetic Data Vault) concepts

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad08-dot/synthetic-data-generation-platform.git
   cd synthetic-data-generation-platform
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit pandas numpy plotly
   ```

3. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📄 License
This project is licensed under the MIT License.
