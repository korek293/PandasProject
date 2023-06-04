import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# Creating DataFrame
sales_data = pd.DataFrame({
    'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'month': ['January', 'Fabruary', 'March', 'April', 'May'],
    'sales': [1000, 1500, 1200, 1800, 2000]
})

# Saving DataFrame in CSV format with utf-8 encoding
sales_data.to_csv('sales_data.csv', encoding='utf-8', index=False)

sales_data.dropna(inplace=True) # deleting rows with missing values

sales_by_month = sales_data.groupby('month')['sales'].sum()
print(sales_by_month)

sales_by_month.plot(kind='bar')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()


