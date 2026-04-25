# Sales Data Analysis Dashboard

## Overview

This project analyzes a sales dataset to understand how revenue changes across time, regions, and products. The goal was to take raw sales data and turn it into clear insights that can support business decisions.

I initially built this as a simple analysis script and later improved it by adding structured insights, clearer visualizations, and practical recommendations.

---

## Problem

The dataset contains sales records, but it does not directly answer important business questions:

* When does the business perform best?
* Which regions generate the most revenue?
* Which products drive sales?
* Where is performance weak?

Without analysis, the data has limited value.

---

## Approach

### Data Preparation

* Converted date column to datetime
* Handled missing values in `Units_Sold` and `Price`
* Created a `Revenue` column:

  Revenue = Units_Sold × Price × (1 − Discount)

---

### Analysis

Used Pandas `groupby` to analyze:

* Monthly revenue trends
* Revenue by region
* Revenue by product

---

### Visualization

Created bar charts to clearly present:

* Monthly revenue (with labels and highlighted best month)
* Revenue by region
* Revenue by product

---

## Key Findings

* Revenue varies across months, with a clear peak period
* Some regions consistently generate more revenue
* A few products contribute most of the total sales
* Certain periods show lower performance

---

## Recommendations

* Focus marketing during high-performing months
* Improve strategy for low-performing months
* Promote top-selling products
* Expand in high-performing regions

---

## Visualizations

### Monthly Revenue

![Monthly Revenue](monthly_revenue.png)

### Revenue by Region

![Revenue by Region](region_revenue.png)

### Revenue by Product

![Revenue by Product](product_revenue.png)

---

## Tools Used

* Python
* Pandas
* Matplotlib

---

## What I Improved

* Added multi-level analysis (month, region, product)
* Improved charts with labels and highlights
* Structured insights and recommendations
* Focused on explaining results clearly

---

## Limitations

* Uses static dataset
* No interactive dashboard

---

## Future Work

* Convert to interactive dashboard (Streamlit)
* Add filters (date, region, product)
* Explore forecasting

---

## Takeaway

This project demonstrates my ability to clean data, analyze trends, and communicate insights in a clear and structured way.

---

