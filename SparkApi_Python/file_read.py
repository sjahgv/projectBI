import requests
import pandas as pd
from datetime import time,datetime

# 替换为你的智谱API密钥
API_KEY = 'b6a23472ae61d3d8b97515536643dae2.xN8JW3BsMDIiA2Mo'

# 智谱API的URL
API_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'

# 读取Excel文件
excel_path = 'D:\学习\毕设\标注Excel\标注20-1.xlsx'
df = pd.read_excel(excel_path)

# 假设我们要读取的特定三列是 'Column1', 'Column2', 'Column3'
target_columns = ['说话人', '话语']


# 创建要发送到智谱API的数据列表
data_to_send = []
for index, row in df.iterrows():
    data_entry = {
        '说话人': row['说话人'],

        '话语': row['话语']
    }
    # # 确保时间帧是字符串类型
    # time_str = str(row['时间帧'])
    # # 使用time.fromisoformat解析时间字符串
    # time_obj = time.fromisoformat(time_str)
    # data_entry = {
    #     '说话人': row['说话人'],
    #     '时间帧': time_obj,  # 使用time对象
    #     '话语': row['话语']
    # }
    # data_to_send.append(data_entry)

    # 使用time.fromisoformat解析时间字符串
    # try:
    #     time_str = str(row['时间帧'])
    #     time_obj = time.fromisoformat(time_str)
    #     data_entry = {
    #         '说话人': row['说话人'],
    #         '时间帧': time_obj,  # 使用time对象
    #         '话语': row['话语']
    #     }
    #     data_to_send.append(data_entry)
    # except ValueError as e:
    #     print(f"Error parsing time frame at row {index}: {e}")

# 构造请求头
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

# 发送请求
response = requests.post(API_URL, json=data_to_send, headers=headers)

# 检查响应
if response.status_code == 200:
    print('数据成功发送到智谱API')
    print('响应内容：', response.json())
else:
    print('发送数据到智谱API失败')
    print('状态码：', response.status_code)
    print('响应内容：', response.text)
