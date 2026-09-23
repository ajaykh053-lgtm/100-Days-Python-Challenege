# Congratulations on completing another challenging data science project! Today we've seen how to grab some raw data and create some interesting charts using Pandas and Matplotlib. We've

# used .groupby() to explore the number of posts and entries per programming language

# converted strings to Datetime objects with to_datetime() for easier plotting

# reshaped our DataFrame by converting categories to columns using .pivot()

# used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()

# created (multiple) line charts using .plot() with a for-loop

# styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.

# added a legend to tell apart which line is which by colour

# smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.


# Well done for completing today's lessons! Have a good rest. I'll see you tomorrow!

import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
# print(df.head())

df["DATE"] = pd.to_datetime(df["DATE"])
# print(df.head())

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
# print(reshaped_df.head())

reshaped_df.fillna(0, inplace=True)
reshaped_df = reshaped_df.fillna(0)
# print(reshaped_df.head())

plt.figure(figsize=(16,10))  # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)

# plt.plot(reshaped_df.index, reshaped_df.java)
# plt.plot(reshaped_df.index, reshaped_df.python)

# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column],
#              linewidth=3, label=reshaped_df[column].name)
# plt.legend(fontsize=16)
# plt.show()

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

# plot the roll_df instead

for column in roll_df.columns:
    plt.plot(
        roll_df.index,
        roll_df[column],
        linewidth=3,
        label=roll_df[column].name,
    )
plt.legend(fontsize=16)
plt.show()
