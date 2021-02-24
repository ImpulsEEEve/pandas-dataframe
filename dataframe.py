import pandas as pd

# define the dictionary
cars = {
    'Brand': ['Honda', 'Toyota', 'Ford'],
    'Price': [22000, 25000, 27000]
}

# setup pandas dataframe
cars_df = pd.DataFrame(cars, columns = ['Brand', 'Price'], index=['Car 1', 'Car 2', 'Car 3'])

# adding a new column
year = [2010, 2011, 2008]
cars_df['Year'] = year

# insert a new column
cars_df.insert(1, 'Model', ['Civic', 'Prius', 'Focus'], True)

# add a new car
cars_df.loc['Car 4'] = ['Hyundai', 'Avante', 20000, 2010]
cars_df.loc['Car 3'] = ['Suzuki', 'Swift', 26000, 2013]

# compute the discounted price
cars_df['Discount'] = 0.1*cars_df['Price']
cars_df['Discounted Price'] = 0.9*cars_df['Price']

# display the generated pandas dataframe
print(cars_df)
