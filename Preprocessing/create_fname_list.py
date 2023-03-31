# Marc Garcia
#import libraries
from pathlib import Path
import numpy as np
import os
from collections import namedtuple
import pandas as pd

File = namedtuple('File','fname')

#empty list
files =[]

#create starting path
p = Path('/path/to/directory')


#Iterate through path to find all seed files
for item in p.glob('**/*'):
    if item.suffix in ['.mseed']:
        fname = item.name
        #path = Path.resolve(item).parent
    
        files.append(File(fname))

 

#Creating a dataframe        
df = pd.DataFrame(files)

#Sort Files
sorted_df = df.sort_values(by=["fname"], ascending=True)

#Saving dataframe as a CSV
sorted_df.to_csv(r'/path/to/directory/fnames.csv', index = False)
