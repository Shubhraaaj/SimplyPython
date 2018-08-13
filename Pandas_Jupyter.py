import pandas

df1 = pandas.read_excel("expenses.xlsx")

# df1 = df1.set_index("DATE")

# df2 = df1.loc["23-07-2018":"26-07-2018", "EXPENSES":"REASON"]

# print(list(df1.loc[:, "DATE"]))

# df2 = df1.iloc[1, 3]

# df2 = df1.ix[1,2]

# df2 = df1.drop("DATE", 1)

# df2 = df1.drop(df1.index[0:3], 0)

# df2 = df1.columns

# print(len(df1.index))

# df1["EARNING"] = df1.shape[0]*["No Earnings"]

# df2 = df1.T (Rows <=> Columns)

print(type(df1))