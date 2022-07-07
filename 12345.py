import numpy as np
import pandas as pd
def clean(data):
    dataframe= pd.read_excel(data)
    df = dataframe.replace(np.nan, 0)
    #df = df.assign(RegionName = df.get('RegionName').apply(add_top))
    df = df.drop(columns = ['RegionID','SizeRank','RegionType','StateName','StateName','Metro','StateCodeFIPS','MunicipalCodeFIPS'])
    df = df.set_index(['RegionName','State'])
    df.columns = pd.to_datetime(df.columns)
    df = df[df.columns[(df.columns.month == 1)|(df.columns.month == 6)]]
    df = df.pct_change(axis='columns', periods=1).reset_index()
    df.index = df.index +1
    return df
  def add_one(RegionName):
    return str(RegionName)+'_1'

def add_two(RegionName):
    return str(RegionName)+'_2'

def add_three(RegionName):
    return str(RegionName)+'_3'

def add_four(RegionName):
    return str(RegionName)+'_4'

def add_five(RegionName):
    return str(RegionName)+'_5'

df1 = clean('one.xlsx')
df1 = df1.assign(RegionName = df1.get('RegionName').apply(add_one))
df2 = clean('two.xlsx')
df2 = df2.assign(RegionName = df2.get('RegionName').apply(add_two))
df3 = clean('three.xlsx')
df3 = df3.assign(RegionName = df3.get('RegionName').apply(add_three))
df4 = clean('four.xlsx')
df4 = df4.assign(RegionName = df4.get('RegionName').apply(add_four))
df5 = clean('five.xlsx')
df5 = df5.assign(RegionName = df5.get('RegionName').apply(add_five))
df = pd.concat([df1,df2,df3,df4,df5]).sort_index()
df = df.reset_index().set_index(['index','RegionName'])
df
