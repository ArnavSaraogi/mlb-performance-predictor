# mlb-performance-predictor
This project uses Ridge Regression in order to predict MLB players' 2025 OPS's. Independent variables are baseball statistics that are used as indicators of luck, while the target variable is the % Change in OPS from one season to the next. The idea is that if a player got lucky in 2024, they will experience worse outcomes in 2025.

## Features
* Data Aggregation: Collects necessary data from multiple input CSV files downloaded from Baseball Savant
* Focus on Luck Indicators: Utilizes BABIP and the difference in actual and Statcast's "expected stats" to make predictions
* Pre-Processing: Data is standardized and missing values are filled with the median using Python library scikit-learn's Pipeline.
* Ridge Regression: Mitigates effects of multicollinearity in features and reduces the chance of overfitting to the 2024 season.

## Reading This Repository
1. [input_csvs/](input_csvs/) : CSVs downloaded from baseball Savant
1. [create_csv.py](create_csv.py) : Collects relevant data from input csvs into [out.csv](out.csv)
1. [exploration.ipynb](exploration.ipynb) : Looks at relationships of features with each other and with OPS change
1. [regression.csv](regression.ipynb) : Creates regression model and makes 2025 predictions, seen in [predictions.csv](predictions.csv)

## Improvements to Make
* Improve the model's coefficient of determination (0.18) by introducing additional features, such as injuries
* Explore year-to-year trends in league-wide OPS changes to incorporate into individual players' predictions