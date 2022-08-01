#ETL EXMAPLE
#SARAH MCBRIDE
#July 30, 2022

#### EXTRACT DIFERENT FORMS Of DATA

import petl as etl
import pandas as pd
import numpy as np
import glob





consolidated_output.1 = pd.DataFrame(['product_name','quality', 'material_id', 'worth'])
consolidated_output.1 = pd.append(sample1)
consolidated_output.1 = pd.append(sample2)
consolidated_output.1 = pd.append(sample3)


def extract():
    
    #csv file
    for sample_data.1.csv in glob.glob("sample_data.1.csv"):
        sd1 = pd.read_csv(sample_data.1.csv)
        sample1 = pd.DataFrame(sd1)
        addition = [{'Data Source': 'sample_data.1'}]
        sample1 = etl.fromdicts(addition)
    #dat files
    for sample_data.2.dat in glob.glob("sample_data.2.dat"):
        sd2 = np.loadtxt('sample_data.2.dat', unpack=True)
        sample2 = pd.DataFrame(sd2)
        addition2 = [{'Data Source': 'sample_data.2'}]
        sample2 = etl.fromdicts(addition2)
        
    for sample_data.3.dat in glob.glob("sample_data.3.dat"):
        sd3 = np.loadtxt('sample_data.3.dat', unpack=True)
        sample3 = pd.DataFrame(sd3)
        addition3 = [{'Data Source': 'sample_data.3'}]
        sample3 = etl.fromdicts(addition3)
    return sample1, sample2, sample3
    
def sample1_worth(sample1['worth']):
    return 'worth' > 1.00
sample1_new = sample1.convert('worth', sample1_worth)

def sample3_worth(sample3['worth']):
    return 'worth'/'material_id'
sample3_new = sample3.convert('worth', sample3_worth)

consolidated_output.1 = pd.DataFrame(['product_name','quality', 'material_id', 'worth'])
consolidated_output.1 = pd.append(sample1_new)
consolidated_output.1 = pd.append(sample2)
consolidated_output.1 = pd.append(sample3_new)

agg_s2= sample2.aggregate('product_name',axis = 1, sample2.nlargest(1,'quality'), max('material ID'),sum('worth'))



consolidated_output.1 = pd.DataFrame(['product_name','quality', 'material_id', 'worth'])
consolidated_output.1 = pd.append(sample1)
consolidated_output.1 = pd.append(sample2)
consolidated_output.1 = pd.append(sample3)



##################### LOAD DATA ###################
### simply save as a csv
consolidated_output.1.tocsv('consolidated_output.1.csv')

