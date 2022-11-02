import pandas as pd

df = pd.read_excel('data.xls')
df.rename(columns={'QUARTER 1,2,3,4':'quarter'},inplace=True)
df.rename(columns={'API WELL  NUMBER':'well_number'},inplace=True)
df.rename(columns={'Production Year':'year'},inplace=True)
well_number=34059243030000
oil = df.query(f'year==2020 and well_number=={well_number}')['OIL'].sum()
gas = df.query("year==2020 and well_number==34013212500000")['GAS'].sum()
brine = df.query("year==2020 and well_number==34059243030000")['BRINE'].sum()