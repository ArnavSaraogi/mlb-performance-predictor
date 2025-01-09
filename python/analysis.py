import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 

X = pd.read_csv('out.csv')[['xbadiff (2023)', 'xslgdiff (2023)', 'wobadiff (2023)']]
y = pd.read_csv('out.csv')[['ops_change 2023-2024']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, train_size = 0.8)

lr = LinearRegression()
lr.fit(X_train, y_train)

print(lr.score(X_test, y_test))