import pandas as pd
import pandas_profiling

# 文件存储路径
file_path = '测试数据.xlsx'
# 读取文件
pd_data = pd.read_excel(file_path)
# 一行代码数据分析出报告
data = pandas_profiling.ProfileReport(pd_data, title="My Report")
# 输出结果到页面
data.to_file('测试数据分析报告.html')