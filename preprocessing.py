import numpy as np
import pandas as pd

# data files
data_directory = 'data/'
residential_buildings_file = data_directory + 'EXTR_ResBldg.csv'
seattle_zip_codes_file = data_directory + 'seattle-zip-codes.txt'

# lists for cleaning data
seattle_zip_codes = np.loadtxt('seattle-zip-codes.txt').astype(int).astype(str)
seattle_zip_codes_appended = np.append(np.loadtxt('seattle-zip-codes.txt').astype(int).astype(str), '')
desired_columns = ['Major', 'Minor', 'BldgNbr', 'NbrLivingUnits', 'Address',
                   'BuildingNumber', 'Fraction', 'DirectionPrefix', 'StreetName',
                   'StreetType', 'DirectionSuffix', 'ZipCode', 'HeatSystem',
                   'HeatSource', 'YrBuilt','YrRenovated']
oil_heat_values = [1, 4]

# functions for cleaning up zip codes
def get_five_digit(x):
  if len(x) < 5:
    return ''
    four_digit = ''
  elif len(x) == 5:
    return x
  elif len(x) == 10:
    return x[:5]
  elif len(x) == 9:
    return x[:5]
  elif x == 988122:
    return '98122'
  else:
    return ''

def get_four_digit(x):
  if len(x) == 10:
    return x[6:10]
  elif len(x) == 9:
    return x[5:9]
  else:
    return ''

# upload data and select desired columns
df = pd.read_csv(residential_buildings_file)
df = df[df.columns.intersection(desired_columns)]

# prune data based on zip codes
df['FiveDigitZip'] = df['ZipCode'].astype(str).apply(get_five_digit)
df['FourDigitZip'] = df['ZipCode'].astype(str).apply(get_four_digit)
df = df[df['FiveDigitZip'].isin(seattle_zip_codes)]

# select only homes using oil heat
df = df[df['HeatSource'].isin(oil_heat_values)]