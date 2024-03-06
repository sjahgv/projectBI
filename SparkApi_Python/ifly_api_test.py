import time

import requests
import json
import pandas as pd
file_path = "E:/文件/1003班综合课L14-1_1（20221024）示范课.xlsx"
df = pd.read_excel(file_path)    # 查看数据，确保读取无误#
filtered_content = df[df['知识点1'] == '词语']['知识点3']
print(filtered_content )
api_url = 'http://api.example.com/extract_relations'#https://api.example.com/relationship_extraction
api_key = "2b3c9c37c6c925c38ae5097fc942fe4f.9YVQ5GSx8ftDwq1E"
# 设置请求的头部#
headers = {
     'Content-Type': 'application/json',
     'Authorization': f'Token {api_key}'}
# 准备要发送的数据
data_to_send = {
'text': df['话语']}
# 步骤4：循环遍历Excel文件中的每一行，调用API进行关系抽取
# 初始化一个空的DataFrame存储关系抽取的结果
results_df = pd.DataFrame(columns=['Column1', 'Column2','Column3'])
# 根据需要抽取的关系指定列名
# 遍历DataFrame中的每一行
for index, row in df.iterrows():# 从当前行中获取需要抽取关系的文本，这里假设是\'content\'列\\n
  text_to_analyze = row['话语']
  # 准备发送的数据
  data_to_send['text'] = text_to_analyze
       # 发送请求
  response = requests.post(api_url, headers=headers, data=json.dumps(data_to_send),verify=False)

  # 确保响应成功
  if response.status_code == 200:
# 解析响应内容\\n
     response_data = response.json()
# 处理和解析您需要的关系数据，并添加到results_df中\\n
# 这里需要根据API返回的具体格式来处理\\n
     results_df = results_df.append({ 'Column1': response_data['relation1'], 'Column2': response_data['relation2'],'Column3': response_data['relation3'],      }, ignore_index=True)
  else:
       print(f"Error at row {index}: {response.text}")
       #步骤5：保存结果\\n\\n最后，将关系抽取的结果保存到新的Excel文件或其他格式：\\n\\n```python\\n# 保存结果到新的Excel文件\\n
results_df.to_excel('relationship_extraction_results.xlsx', index=False)

