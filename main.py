#!/usr/bin/env python
# coding: utf-8

# In[115]:


import os
import csv
import contextlib
import pandas as pd

csvpath = os.path.join("Resources", "budget_data.csv")

book_df = pd.read_csv('resources/budget_data.csv')


# In[116]:


#total up net total of profits/losses
total = book_df["Profit/Losses"].sum()


# In[117]:


# Create a new column to store the changes in 'Profit/Losses'
book_df['Change'] = book_df['Profit/Losses'].diff()

# Calculate the average of the changes
average_change = book_df['Change'].mean()


# In[118]:


#greatest increase in profits over the period (date + amount)
profit = book_df.nlargest(1,"Change")
profitdate = profit.loc[:,"Date"].values[0]
profitamount = profit.loc[:, "Change"].values[0]




# In[119]:


#greatest loss over the period (date, amount)
loss = book_df.nsmallest(1,"Change")
lossdate = loss.loc[:,"Date"].values[0]
lossamount = loss.loc[:, "Change"].values[0]


# In[120]:


#get total number of months
#this is just the number of rows minus the header
totalmonths = book_df.shape[0]



# In[121]:


#output to text file

output_file = open("analysis/budget_analysis.txt", "w")
with contextlib.redirect_stdout(output_file):
    
    print("Financial Analysis")
    print("--------------------")
    print("Total Months:", totalmonths)
    print("Total: $", total)
    print("Average Change: ${:,.2f}".format(average_change))
    print("Greatest Increase in Profits: $", profitdate, profitamount)
    print("Greatest Decrease in Profits: $", lossdate, lossamount)

output_file.close()


# In[122]:


#output to terminal


print("Financial Analysis")
print("--------------------")
print("Total Months:", totalmonths)
print("Total: ", total)
print("Average Change: ${:,.2f}".format(average_change))
print("Greatest Increase in Profits: ", profitdate, "$",profitamount)
print("Greatest Decrease in Profits: ", lossdate, "$",lossamount)


    


# In[ ]:




