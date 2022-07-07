import numpy as np
import pandas as pd
def add_top(RegionName):
    return str(RegionName)+'_top'
def add_middle(RegionName):
    return str(RegionName)+'_middle'
def add_bottom(RegionName):
    return str(RegionName)+'_bottom'
dataframe_t= pd.read_excel('top.xlsx')
df_t = dataframe_t.replace(np.nan, 0)
df_t = df_t.assign(RegionName = df_t.get('RegionName').apply(add_top))
df_t = df_t.drop(columns = ['RegionID','SizeRank','RegionType','StateName','StateName','Metro','StateCodeFIPS','MunicipalCodeFIPS'])
df_t = df_t.set_index(['RegionName','State'])
df_t.columns = pd.to_datetime(df_t.columns)
df_t = df_t[df_t.columns[(df_t.columns.month == 1)|(df_t.columns.month == 6)]]
df_t = df_t.pct_change(axis='columns', periods=1).reset_index()
df_t.index = df_t.index +1
dataframe_m= pd.read_excel('middle.xlsx')
df_m = dataframe_m.replace(np.nan, 0)
df_m = df_m.assign(RegionName = df_m.get('RegionName').apply(add_middle))
df_m = df_m.drop(columns = ['RegionID','SizeRank','RegionType','StateName','StateName','Metro','StateCodeFIPS','MunicipalCodeFIPS'])
df_m = df_m.set_index(['RegionName','State'])
df_m.columns = pd.to_datetime(df_m.columns)
df_m = df_m[df_m.columns[(df_m.columns.month == 1)|(df_m.columns.month == 6)]]
df_m = df_m.pct_change(axis='columns', periods=1).reset_index()
df_m.index = df_m.index +1
dataframe_b= pd.read_excel('bottom.xlsx')
df_b = dataframe_b.replace(np.nan, 0)
df_b = df_b.assign(RegionName = df_b.get('RegionName').apply(add_bottom))
df_b = df_b.drop(columns = ['RegionID','SizeRank','RegionType','StateName','StateName','Metro','StateCodeFIPS','MunicipalCodeFIPS'])
df_b = df_b.set_index(['RegionName','State'])
df_b.columns = pd.to_datetime(df_b.columns)
df_b = df_b[df_b.columns[(df_b.columns.month == 1)|(df_b.columns.month == 6)]]
df_b = df_b.pct_change(axis='columns', periods=1).reset_index()
df_b.index = df_b.index +1
df = pd.concat([df_b,df_m,df_t]).sort_index()
df = df.reset_index().set_index(['index','RegionName'])
df
