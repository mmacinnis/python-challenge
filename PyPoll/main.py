#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import contextlib
import pandas as pd
from pathlib import Path

csvpath = Path("Resources/election_data.csv")

poll_df = pd.read_csv(csvpath)
                


# In[ ]:





# In[2]:


# The total number of votes cast

totalvotes = poll_df.shape[0]


# In[3]:


# The total number of votes each candidate won

count = poll_df["Candidate"].value_counts()
anal_df=pd.DataFrame(count)


# In[4]:


# The percentage of votes each candidate won
#percent = (count / totalvotes )*100 
#percent
perc = (anal_df["count"]/totalvotes)*100
anal_df['percent'] = perc



# In[5]:


#fix columns

cleananal_df = anal_df[["percent", "count"]]
cleananal_df["percentage_form"] = cleananal_df['percent'].apply(lambda x: '{:.3f}%'.format(x))
cleaner_df = cleananal_df[["count", "percentage_form"]]
cleaner_df.rename(columns={"percentage_form" : "percent"}, inplace=True )
cleaner_df.reset_index(inplace=True)
cleaner_df.sort_values("count", ascending=False)

winner=cleaner_df.iloc[0,0]






# In[6]:


#output to text file

output_file = open("analysis/vote_analysis.txt", "w")
with contextlib.redirect_stdout(output_file):
    
    print("Election Results")
    print("----------------------------------")
    print("Total Votes:", totalvotes)
    print("----------------------------------")
    print(cleaner_df.to_string(index=False))
    print("----------------------------------")
    print("Winner: ",winner)
    print("----------------------------------")

output_file.close()


# In[7]:


#output to terminal


print("Election Results")
print("----------------------------------")
print("Total Votes:", totalvotes)
print("----------------------------------")
print(cleaner_df.to_string(index=False))
print("----------------------------------")
print("Winner: ",winner)

print("----------------------------------")





# In[ ]:




