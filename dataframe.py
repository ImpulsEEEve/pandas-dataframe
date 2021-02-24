import pandas as pd

cars = {
    'Brand': ['Honda', 'Toyota', 'Ford'],
    'Price': [22000, 25000, 27000]
}

cars_df = pd.DataFrame(cars, columns = ['Brand', 'Price'])
print(cars_df)
