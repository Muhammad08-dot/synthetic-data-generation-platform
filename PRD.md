# Product Requirements Document (PRD): Synthetic Data Generation Platform

## 1. Overview
The **Synthetic Data Generation Platform** is a tool designed to solve the "data scarcity" problem in machine learning. It allows data scientists and engineers to generate realistic, privacy-preserving synthetic datasets (tabular and text) based on a small seed dataset or schema, without exposing any Personally Identifiable Information (PII).

## 2. Target Audience
- Data Scientists
- Machine Learning Engineers
- Enterprise Data Privacy Teams
- Healthcare and Financial Tech Companies

## 3. Core Features
- **Schema Definition:** Define the structure of the desired tabular data (columns, data types, constraints).
- **Tabular Generation:** Use SDV (Synthetic Data Vault) underlying logic (mocked for demo) to generate thousands of realistic rows.
- **LLM Text Augmentation:** Generate synthetic text data (e.g., customer reviews, support tickets) based on specified personas and topics.
- **Privacy Metrics:** Provide a score on how well the synthetic data preserves the statistical properties of the original data while ensuring 0% PII leakage.
- **Data Export:** Download the generated synthetic data as CSV or JSON.

## 4. Technical Architecture
- **Frontend/UI:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Synthetic Engine:** Mocked SDV (Synthetic Data Vault) / Faker for tabular; mocked LLM for text.
- **Data Visualization:** Plotly for comparing distributions between "Original" and "Synthetic" data.

## 5. UI/UX Design
- **Theme:** Clean, enterprise-focused, light mode (data-centric).
- **Tabs:** "Tabular Data Generator", "Text Data Generator", "Quality Metrics".
- **Visuals:** Side-by-side histograms comparing the original data distribution vs. the synthetic data distribution.

## 6. Development Milestones
1. **M1:** Build the Streamlit layout with the three main tabs.
2. **M2:** Implement the tabular generation logic using `Faker` and `Pandas`.
3. **M3:** Create the Quality Metrics dashboard with Plotly charts.
4. **M4:** Final polish, README generation, and deployment setup.
