
import pandas as pd

df = pd.read_excel("on.xlsx")
# df = pd.read_excel("on.xlsx",usecols=["日期","時間"],nrows=21)


# print(df)
# print(df[0:10])

# 取資料內容
d2 = df.at[0, "日期"]
print(d2)


print(type(df.index)) # 'pandas.core.indexes.range.RangeIndex

#資料的形狀
print((df.shape))

#行資料數
print((df.shape[0]))
#資料列數
print((df.shape[1]))

# print(type(df.keys()))
# print(type(df.columns)) # pandas.core.indexes.base.Index

# # excel 欄位名稱
# sheet_names = list(df.keys())
# print("_______________",sheet_names)

# # 轉 list
# print(df.keys().tolist())
# print(df["同學"].tolist())

# # print( df[:] )
# print(df[0:6]["同學"])

# # 篩選math大於80的資料集
# print(df[df["math"] >5] )

# # 篩選 同學 欄位包含 許 的資料集
# print(df[df["同學"].isin(["許"])])

# #排序
# new_df = df.sort_index(ascending=False)
# new_df = df.sort_values(["math"], ascending=False)
# print("遞增排序")
# print(new_df)