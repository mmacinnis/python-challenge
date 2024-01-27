#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import contextlib
import pandas as pd

csvpath = os.path.join("Resources", "budget_data.csv")

book_df = pd.read_csv('resources/budget_data.csv')


# In[2]:


#total up net total of profits/losses
total = book_df["Profit/Losses"].sum()


# In[3]:


# Create a new column to store the changes in 'Profit/Losses'
book_df['Change'] = book_df['Profit/Losses'].diff()

# Calculate the average of the changes
average_change = book_df['Change'].mean()


# In[4]:


#greatest increase in profits over the period (date + amount)
profit = book_df.nlargest(1,"Change")
profitdate = profit.loc[:,"Date"].values[0]
profitamount = profit.loc[:, "Change"].values[0]




# In[5]:


#greatest loss over the period (date, amount)
loss = book_df.nsmallest(1,"Change")
lossdate = loss.loc[:,"Date"].values[0]
lossamount = loss.loc[:, "Change"].values[0]


# In[6]:


#get total number of months
#this is just the number of rows minus the header
totalmonths = book_df.shape[0]



# In[ ]:





# In[7]:


#output to terminal


print("Financial Analysis")
print("--------------------")
print("Total Months:", totalmonths)
print("Total: ", total)
print("Average Change: ${:,.2f}".format(average_change))
print("Greatest Increase in Profits: ", profitdate, "$",profitamount)
print("Greatest Decrease in Profits: ", lossdate, "$",lossamount)


    


# In[8]:


#output to text file

with open("analysis/budget_analysis.txt", "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write("Total Months: ")
    totalmonthsstr = str(totalmonths)
    output_file.write(totalmonthsstr)
    output_file.write("\n")
    
    output_file.write("Total: $")
    totalstr = str(total)
    output_file.write(totalstr)
    output_file.write("\n")
    
    output_file.write("Average Change: ")
    average_change = "${:,.2f}".format(average_change)
    avgchangestr = str(average_change)
    output_file.write(avgchangestr)
    output_file.write("\n")
    
    output_file.write("Greatest Increase in Profits: ")
    profitdatestr = str(profitdate)
    profitamtstr = str(profitamount)
    output_file.write(profitdatestr)
    output_file.write("  $")
    output_file.write(profitamtstr)
    output_file.write("\n")
    
    output_file.write("Greatest Decrease in Profits: ")
    lossdatestr = str(lossdate)
    lossamtstr = str(lossamount)
    output_file.write(lossdatestr)
    output_file.write("  $")
    output_file.write(lossamtstr)
    output_file.write("\n")
    
output_file.close()   




# In[ ]:




