# London Cycling Insights Dashboard

## Overview

The **London Cycling Insights Dashboard** provides a comprehensive view of cycling patterns in London, aiding urban planners and policymakers in identifying trends, high-traffic areas, and factors influencing cycling activity. Built using **Google Looker Studio**, the dashboard connects directly to the BigQuery processed fact table to visualize data through interactive charts. It features six key visualizations, each offering unique insights into cycling behavior across London boroughs, time periods, weather conditions, and functional areas.

![Dashboard Overview](/images/dashboard-overview.png)

---

## Dashboard Visualizations

### 1. Total Cycling Counts (Scorecard)
- **Description**: Displays the overall sum of cycling counts (`total_count`) across all records, providing a high-level summary of total cycling activity in London.  
- **Insight**: A quick reference for the total volume of cycling activity, useful for benchmarking and tracking overall trends.  
![Total Cycling Counts](/images/total-cycling-counts.png)

---

### 2. Daily Cycling Counts (Line Graph)
- **Description**: A line graph showing the sum of `total_count` by day of the week, with days on the x-axis and counts on the y-axis.  
- **Insight**: Reveals peak cycling days, helping to optimize infrastructure usage or promote cycling on quieter days.  
![Daily Cycling Counts](/images/daily-cycling-counts.png)

---

### 3. Travel Distribution Across London Boroughs (Geo Chart)
- **Description**: A geographical map plotting individual sites using the `Lat_Long` field (derived from latitude and longitude), with points sized by `total_count`. The map is zoomed to London, United Kingdom.  
- **Insight**: Identifies high-traffic areas at a site level, guiding precise infrastructure improvements like adding bike lanes in busy zones.  
![Travel Distribution](/images/travel-distribution.png)

---

### 4. Record Count by Month and Weather (Stacked Bar Chart)
- **Description**: A stacked bar chart showing `total_count` by month, with each bar stacked by weather conditions (e.g., dry, wet, sunny). Months are on the x-axis, and counts are on the y-axis.  
- **Insight**: Highlights how weather impacts cycling activity over time, identifying barriers (e.g., reduced cycling in rainy months) for targeted interventions like weather-protected lanes.  
![Record Count by Month and Weather](/images/record-count-weather.png)

---

### 5. Count by London Functional Area (Donut Chart)
- **Description**: A donut chart showing the proportion of `total_count` by `functional_area` (Central, Inner, Outer London), with each segment labeled with its percentage.  
- **Insight**: Reveals the distribution of cycling activity across London’s functional areas, helping prioritize planning efforts (e.g., focusing on Central London if it has the highest counts).  
![Count by Functional Area](/images/count-functional-area.png)

---

---

## Accessibility

The dashboard is shared via a [public link](https://lookerstudio.google.com/reporting/866ac714-6e0f-4454-a7f9-5b0c58e631aa) for peer review, ensuring stakeholders can access the insights easily.  
