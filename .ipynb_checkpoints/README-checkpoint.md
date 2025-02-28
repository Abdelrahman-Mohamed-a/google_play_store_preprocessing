# Play Store Apps Data Cleaning and Preprocessing

## Introduction

The Play Store hosts a wide range of applications, and the data associated with these apps offers significant potential for analysis. Developers and businesses can leverage this data to understand market trends, optimize their apps, and maximize user engagement.

In this project, we will perform data cleaning and preprocessing on the Play Store apps dataset, addressing missing values, outliers, and other issues while extracting valuable insights.

## Dataset Overview

The dataset consists of various attributes related to Play Store applications, including:

- **Application Name**: Name of the application
- **Category**: Category the app belongs to
- **Rating**: Overall user rating of the app (as when scraped)
- **Reviews**: Number of user reviews for the app (as when scraped)
- **Size**: Size of the app (as when scraped)
- **Installs**: Number of user downloads/installs for the app (as when scraped)
- **Type**: Whether the app is free or paid
- **Price**: Price of the app (as when scraped)
- **Content Rating**: Age group the app is targeted at (e.g., Children / Mature 21+ / Adult)
- **Genres**: Multiple genres an app can belong to
- **Last Updated**: Date when the app was last updated
- **Current Version**: Current version of the app
- **Android Version**: Minimum Android version required

## Data Cleaning Tasks

The following tasks will be performed for data cleaning and preprocessing:

- Fix **Rating** values
- Fix **Size** values
- Fix **Price** values
- Fix **Category** inconsistencies
- Fix **Android Version** formatting
- Handle **Missing Values**
- **Outlier Detection and Handling**
- Fix any other inconsistencies or errors in the dataset

## Analytical Questions

Once the dataset is cleaned, we will analyze it to answer the following questions:

1. What is the most expensive app on the Play Store?
2. Which genre has the highest number of apps?
3. What is the average size of free vs. paid apps?
4. What are the top 5 most expensive apps with a perfect rating (5)?
5. How many apps have received more than 50K reviews?
6. What is the average price of apps, grouped by genre and number of installs?
7. How many apps have a rating higher than 4.7, and what is their average price?
8. What is Google's estimated revenue from apps with 5,000,000+ installs? (Assuming Google takes a 30% cut from app sales)
9. What are the maximum and minimum sizes of free vs. paid apps?
10. Is there a correlation between an app’s rating, number of reviews, size, and price?
11. How many apps exist for each type (free/paid) across different content ratings?
12. How many apps are compatible with Android version 4.x?

## Tools and Technologies Used

- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Matplotlib & Seaborn** for data visualization
- **Jupyter Notebook** for interactive coding and documentation

## Conclusion

This project aims to clean, preprocess, and analyze Play Store apps data to extract meaningful insights. Proper data cleaning ensures that our analysis is accurate and reliable. We will present our findings through a well-documented notebook and visualizations to make the results easy to understand.
