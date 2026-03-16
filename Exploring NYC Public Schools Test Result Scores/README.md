# NYC Public Schools Performance Analysis

## Project Overview

Every year, school test results influence the college admissions outcomes of millions of students.

This project analyzes standardized test performance data from New York City public schools to uncover meaningful academic insights. Using Python for data analysis, the project focuses on identifying schools with the highest math performance, exploring how results vary across boroughs, and determining the top ten overall performing schools in the city.

## Objectives

The main goals of this project are:

- Identify the NYC public schools with the best math results.
- Analyze how standardized test performance differs by borough.
- Find the top ten performing schools based on overall SAT results.
- Practice data cleaning, exploration, and aggregation using Python and pandas.

## Technologies Used

- Python
- pandas
- Jupyter Notebook

## Project Tasks

This project answers the following questions:

1. **Which schools have the best math results?**  
   Schools are considered top math performers if their average math SAT score is at least 80% of the maximum possible score.

2. **What are the top ten performing schools in NYC?**  
   Schools are ranked by total SAT score, calculated as:

   `total_SAT = average_math + average_reading + average_writing`

3. **Which borough has the largest variation in SAT performance?**  
   For each borough, the project calculates:
   - Number of schools
   - Average total SAT score
   - Standard deviation of total SAT score

   This helps determine which borough shows the greatest performance variability.
