import pandas as pd
from pprint import pprint

df = pd.read_csv("Starting_salaries_by_college_major.csv")

# df.head()
# This will show us the first 5 rows of our dataframe.
# pprint(df.head())  # head take row number as input like 2

# # How many rows and columns does our dataframe have?

# pprint(df.shape)

# # What are the labels for the columns? Do the columns have names?

# pprint(df.columns)

# # Missing Values and Junk Data

# pprint(df.isna())

# # df.tail()
# # This will show us the last 5 rows of our dataframe.

# pprint(df.tail())  # tail take row number as input like 2

# # Delete the Row with atleast one or more NaN character

clean_df = df.dropna()
# pprint(clean_df.tail())

# # Find College Major with Highest Starting Salaries
# # To access a particular column from a data frame we can use the square bracket notation

# pprint(clean_df["Starting Median Salary"].head(3))

# # To get Max Value in Columns

# print(clean_df["Starting Median Salary"].max())

# # To get the Row ID number of the max data in columns

# print(clean_df["Starting Median Salary"].idxmax())

# # Getting Particular one valur by giving location

# print(clean_df["Undergraduate Major"].loc[43])
# print(clean_df["Mid-Career Median Salary"][43])

# # Q1
# # What college major has the highest mid-career salary?
# # How much do graduates with this major earn?
# # (Mid-career is defined as having 10+ years of experience).

# print(clean_df["Mid-Career Median Salary"].max())
# pprint(
#     f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}"
# )
# pprint(
#     clean_df["Undergraduate Major"].loc[clean_df["Mid-Career Median Salary"].idxmax()]
# )

# # Q2
# # Which college major has the lowest starting salary and
# # how much do graduates earn after university?

# print(clean_df["Starting Median Salary"].min())
# pprint(clean_df["Undergraduate Major"].loc[clean_df["Starting Median Salary"].idxmin()])

# # Q3
# # Which college major has the lowest mid-career salary and
# # how much can people expect to earn with this degree?

# print(clean_df["Mid-Career Median Salary"].min())
# pprint(clean_df["Undergraduate Major"].loc[clean_df["Starting Median Salary"].idxmin()])

# # Lowest Risk Majors (Substracting Two columns)

# pprint(
#     clean_df["Mid-Career 90th Percentile Salary"]
#     - clean_df["Mid-Career 10th Percentile Salary"]
# )

#second type and easy one to understand with wording

# pprint(
#     clean_df["Mid-Career 90th Percentile Salary"].subtract(
#         clean_df["Mid-Career 10th Percentile Salary"]
#     )
# )

# # The output of this computation will be another
# # Pandas dataframe column.
# # We can add this to our existing dataframe
# # with the .insert() method:

spread_col = (
    clean_df["Mid-Career 90th Percentile Salary"]
    - clean_df["Mid-Career 10th Percentile Salary"]
)
clean_df.insert(1, "Spread", spread_col)
# pprint(clean_df.head())

# # Sorting by the Lowest Spread

# low_risk = clean_df.sort_values("Spread")
# pprint(low_risk[["Undergraduate Major", "Spread"]].head())

# # Q4
# # Using the .sort_values() method,
# # can you find the degrees with the highest potential?
# # Find the top 5 degrees with
# # the highest values in the 90th percentile.

# highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary',ascending=False)
# print(highest_potential[['Undergraduate Major','Mid-Career 90th Percentile Salary']].head())

# # Q5
# # find the degrees with
# # the greatest spread in salaries. 
# # Which majors have the largest 
# # difference between high and 
# # low earners after graduation

# highest_spread = clean_df.sort_values('Spread', ascending=False)
# pprint(highest_spread[['Undergraduate Major', 'Spread']].head())

# # Grouping

# pprint(clean_df.groupby('Group').count())

# # Mini Challenge
# # Now can you use the .mean()
# # method to find the average salary by group? 
Group_by = clean_df.groupby('Group')
pprint(Group_by.pd.mean())

# # Number formats in the Output

# pd.options.display.float_format = '{:,.2f}'.format 
# pprint(clean_df.groupby('Group').mean())