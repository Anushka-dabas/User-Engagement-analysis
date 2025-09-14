# User Engagement Analysis 

## 1. Project Overview  
This project leverages structured data from Yelp to perform a comprehensive analysis of restaurant performance by evaluating customer engagement and sentiment. Using SQL for data extraction and Python for advanced analytics and visualisation, the project provides actionable insights into customer behaviour, satisfaction levels, and peak operational hours. The analysis aims to support restaurant stakeholders in making data-driven decisions that enhance service delivery, customer experience, and business growth.

## 2. Tech Stack  

  **SQLite** – Used as the core database engine to query and manipulate large datasets efficiently with optimised SQL scripts.  
 **Python (Pandas, Plotly, NLTK)** – Used for advanced data manipulation, sentiment analysis, and dynamic visualisations.  
 **VADER Sentiment Analysis** – Applied to user reviews to quantify customer sentiment (positive, negative, neutral) and link it with engagement metrics.  
 **Jupyter Notebook (.ipynb)** – Interactive environment combining code, visualisations, and insights for exploratory data analysis.  
 **Data Processing Techniques** – Chunk-based data handling, summary statistics, correlation analysis, and trend visualisation tailored for large datasets.

## 3. Data Source  

The data used in this project was downloaded from the [Yelp Dataset](https://www.yelp.com/dataset) in the form of JSON files. These files include structured information about businesses, reviews, user tips, check-ins, and user profiles across the United States. The dataset is particularly focused on restaurants and contains details such as:

- Business attributes (ratings, categories, location)  
- Customer interactions (reviews, tips, check-ins)  
- User demographics and behaviour  

The JSON files were processed and imported into an SQLite database for efficient querying and analysis.

## 4. Key Objectives  

- Analyse how customer engagement metrics—such as review counts, tip interactions, and check-ins—impact restaurant ratings and overall performance.  
- Perform sentiment analysis on customer reviews to understand satisfaction trends and emotional tone.  
- Identify patterns in customer behaviour across different times of the day and days of the week.  
- Provide practical recommendations to improve customer service, operational efficiency, and marketing strategies.  

## 5. Features & Insights  

### 1. SQL-Based Data Modelling  
- Complex queries are used to join multiple tables—business, review, tip, and check-in—to extract relevant metrics and create aggregated views.  
- Efficient data aggregation techniques ensure the handling of large datasets without compromising performance.

### 2. Sentiment Analysis  
- Reviews are processed using Python’s NLTK library and VADER sentiment scoring to categorize feedback as positive, negative, or neutral.  
- The sentiment distribution helps businesses understand customer satisfaction levels at scale.

### 3. Engagement Trends  
- Peak hours are visualized to identify customer behaviour patterns, guiding staffing and service improvements.  
- Heatmaps reveal correlations between engagement metrics and customer ratings, supporting deeper performance evaluation.

### 4. Actionable Business Insights  
- Higher engagement correlates with better customer ratings, but insights highlight areas for improvement.  
- Monitoring customer feedback trends over time empowers restaurants to respond proactively and enhance customer loyalty.

## 6. Recommendations  

-  **Enhance Engagement Channels**: Actively encourage reviews, tips, and check-ins to better understand customer preferences.  
-  **Utilize Sentiment Insights**: Use sentiment trends to fine-tune marketing strategies and customer service efforts.  
-  **Optimize Operations**: Allocate resources during peak hours for improved customer experience and operational efficiency.  
-  **Data-Driven Decision Making**: Regularly analyse customer feedback and engagement metrics to drive service improvements and competitive advantage.

## 7.  Project Deliverables  

- **SQLite Database** (.db) – Contains structured data with relational tables for restaurants, reviews, tips, and check-ins.  
- **Jupyter Notebook** (.ipynb) – Interactive Python-based analysis including data cleaning, sentiment scoring, correlation analysis, and visualizations.  
- **Visual Reports** – Dynamic bar charts, heatmaps, and time-based trend analysis using Plotly and Matplotlib.  
- **Documentation** – A detailed walkthrough of objectives, methods, and insights for stakeholders and business users.

## 8. 🔍 Potential Use Cases  

- Restaurant chains can benchmark their performance against competitors.  
- Customer feedback trends can guide service improvements and loyalty programs.  
- Marketing teams can optimise campaigns based on sentiment and engagement patterns.  
- Operational teams can plan staffing and inventory management during high-demand periods.


