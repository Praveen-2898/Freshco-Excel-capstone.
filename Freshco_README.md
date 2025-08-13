
# Freshco Hyper Market — Capstone Project (Excel)

**Project type:** Capstone (Excel-centered)  
**Author:** Praveen M (GitHub: Praveen-2898)  
**Contact:** stephanpraveen42@gmail.com · https://www.linkedin.com/in/praveenm755/

---

## 1. Project Overview
This capstone demonstrates a complete Excel-based analysis for **Freshco Hyper Market** using transactional sales data. The workbook includes raw data, aggregation tables (monthly revenue, top categories, sales by state, payment method summary, top products) and a dashboard sheet with charts for quick insights.

**Key objectives:**
- Clean and present transactional data in Excel
- Create summary tables used for business insights
- Build visual charts for monthly revenue, category sales, and payment-method shares
- Provide reproducible Python code to regenerate summaries and Excel file

---

## 2. Files included
- `data_raw_freshco.csv` — synthetic sample transactional dataset (orders).  
- `Freshco_Capstone.xlsx` — Excel workbook with raw data, summary sheet, and a Dashboard (charts included if supported).  
- `analysis.py` — Python script to replicate summaries and reproduce the Excel content locally.  
- `README.md` — this file.

---

## 3. Dataset (sample)
Columns included in `data_raw_freshco.csv`:
- `order_id`, `order_date`, `product_id`, `product_name`, `category`, `unit_price`, `quantity`, `total_price`, `customer_id`, `state`, `payment_method`, `order_status`, `rating`

> Note: The dataset in this repo is synthetic (demo) and intended for learning and showcasing analysis techniques.

---

## 4. What the Excel workbook contains
- **Sheet `raw_data`:** All transaction rows (clean, ready to analyze).
- **Sheet `summary`:** Prepared aggregation tables:
  - Monthly revenue & order count
  - Revenue by category
  - Revenue by state
  - Payment method orders & revenue
  - Top products by revenue
- **Sheet `dashboard`:** Charts showing monthly revenue trend, category revenue, and payment-method share (if charts supported by your Excel engine).

---

## 5. How to open & use the workbook (steps)
1. Download `Freshco_Capstone.xlsx` and `data_raw_freshco.csv` from this repo.  
2. Open the Excel file in Microsoft Excel (Windows/Mac) or LibreOffice Calc (charts may differ).  
3. Explore the **summary** sheet and use Filter on tables to inspect specific months/categories/states.  
4. If you want interactive pivots, create Pivot Tables in Excel from the `raw_data` table (Insert → PivotTable). Use `month` for rows and `sum of total_price` for values to replicate monthly revenue pivot.
5. Use the **dashboard** sheet to view charts. If charts are missing, recreate them using the summary tables (Insert → Chart → choose appropriate range).

---

## 6. How to upload this project to your GitHub (step-by-step)
1. Create a new repository on GitHub (e.g., `freshco-excel-capstone`).  
2. Clone it locally or upload files via the website:
   - On the repo page: **Add file → Upload files** and drag `Freshco_Capstone.xlsx`, `data_raw_freshco.csv`, `analysis.py`, `README.md`.
3. Commit message examples:
   - `Add Freshco capstone initial files (Excel workbook + dataset + script)`
   - `Add dashboard and summary tables`
4. (Optional) Pin the repo on your GitHub profile (Profile → Customize your pins).

---

## 7. Reproduce the Excel file locally using Python
1. Ensure Python 3.x installed with `pandas` and `xlsxwriter` (optional for charts):
```
pip install pandas xlsxwriter openpyxl
```
2. Run the `analysis.py` script to preview summaries, or extend it to write the Excel using `pandas.ExcelWriter` (example included in the repo).

---

## 8. Next steps / ideas for extension
- Add PivotTables in the Excel workbook for interactive slicing.  
- Create calculated measures (e.g., average order value, repeat-customer metrics).  
- Add a `README_images/` folder with screenshot previews of the dashboard.  
- Replace synthetic data with your real Freshco dataset (if available) and repeat the steps.

---

## 9. License
This repo is provided for demonstration and learning purposes. Use as you like.
