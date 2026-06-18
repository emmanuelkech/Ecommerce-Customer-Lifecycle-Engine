# E-Commerce Customer Lifecycle & Cohort Retention Engine

## Project Overview
This project builds a relational analytics engine tracking 15,000 transaction events to compute historical Month-over-Month cohort retention rates, identify user lifecycle decay milestones, and evaluate Customer Lifetime Value (CLV) performance by marketing channel.

## Technology Stack
- **Data Engine Layer:** PostgreSQL
- **Data Engineering Modeling:** Python (Pandas, NumPy, SQLAlchemy)
- **Business Intelligence & Visual Reporting:** Power BI Desktop

## Analytical Architecture Highlight (SQL Cohort Processing)
The pipeline features advanced multi-stage CTE windowing algorithms that calculate structural time lapses between a consumer's initial conversion baseline and recurring purchase transactions. This creates a matrix that lets business leaders visualize exactly when and where customer churn happens.

## Strategic Executive Recommendations Derived From Insights
1. **Month-2 Re-engagement Priority:** The retention heatmap highlights a structural drop-off in returning users during their second lifecycle month. Targeted email marketing should be deployed automatically at day 30.
2. **Channel Realignment:** Paid Search channels deliver the largest raw customer volume, but Organic Social cohorts exhibit a 20% higher Average Order Value (AOV), making social channels a more profitable area for marketing investments.
