import pandas as pd

df = pd.read_excel('data.xls')
df.rename(columns={'QUARTER 1,2,3,4':'quarter'},inplace=True)
df.rename(columns={'API WELL  NUMBER':'well_number'},inplace=True)
df.rename(columns={'Production Year':'year'},inplace=True)

def calc_oil(well_number):
    return df.query(f'year==2020 and well_number=={well_number}')['OIL'].sum()

def calc_gas(well_number):
    return df.query(f'year==2020 and well_number=={well_number}')['GAS'].sum()

def calc_brine(well_number):
    return df.query(f'year==2020 and well_number=={well_number}')['BRINE'].sum()