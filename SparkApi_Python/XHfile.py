import pandas as pd
import requests
import SparkApi
import json

# 以下密钥信息从控制台获取
appid = "935ff112"  # 填写控制台中获取的 APPID 信息
api_secret = "MDRlMDVkNzc2MDBjNTUzMzQ4ODFjZmM3"  # 填写控制台中获取的 APISecret 信息
api_key = "2631b14903cc6f29c0b914e19bc46987"  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“general/generalv2”
domain = "generalv3"  # v1.5版本
# domain = "generalv2"    # v2.0版本
# 云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"  # v1.5环境的地址
# Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

# 读取Excel文件
# def read_excel(filename):
#     df = pd.read_excel(filename)
#     return df['话语']
def read_excel(excel_path, start_row, end_row, column_name):
    # 读取Excel文件
    df = pd.read_excel(excel_path)

    # 确保指定的列名存在于DataFrame中
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # 使用iloc来指定行号范围并读取特定列
    # 从第start_row行开始，到第end_row行结束
    specific_column_content = df.iloc[start_row -2:end_row -1][column_name].values

    return specific_column_content


# def recognize_knowledge():
#     # 准备API请求数据
#     data = {
#         "app_id": appid,
#         "api_key": api_key,
#         "api_secret": api_secret,
#         "domain": domain,
#         "question": [{"role": "user", "content": "请在此处填入您的请求内容"}],
#         # 根据API要求添加其他必要参数
#     }
#     # 发送API请求
#     response = requests.post(Spark_url, json=data)
#     # 处理API响应
#     if response.status_code == 200:
#         result = response.json()
#         # 请根据API返回的数据结构处理结果
#     else:
#         print(f"API请求失败，状态码：{response.status_code}")
#         result = None
#     # 如果API调用成功，将结果存回Excel文件
#     if result:
#         # 需要根据API返回的数据结构来构建DataFrame
#         # 以下是一个示例，实际数据结构可能不同
#         df_with_results = pd.DataFrame(result)
#         df_with_results.to_excel(output_excel_path, index=False)
#         print(f"结果已保存到 {output_excel_path}")
text=[]
def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text
# 主函数
def main():
    # excel_path = 'D:\学习\毕设\标注Excel\标注20-1.xlsx'
    excel_path = './标注20-1.xlsx'
    # 读取的是416-445，excel行号
    start_row = 353  # 起始行号（从1开始）
    end_row = 378  # 结束行号（从1开始）
    column_name = '话语'  # 替换为你的列名
    # 调用函数
    content = read_excel(excel_path, start_row, end_row, column_name)
    result = ''
    for item in content:
        result += str(item)
    que="请问以下内容中，老师强调了哪些知识点？请输出JSON格式，比如{打开：打卡空调}"+result

    question =getText("user",que)

    # question = "以下内容中老师强调了哪些知识点？" + content
    print(question)
    SparkApi.answer = ""
    print("星火:", end="")
    SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
    # print(SparkApi.answer)
    # 将数组转换为JSON格式的字符串# 设置sort_keys=True来确保键的顺序一致
    # 打开一个文件用于写入，如果文件不存在将会被创建
    with open('output.txt', 'w', encoding='utf-8') as file:

        # 将JSON字符串写入文件
        file.write(SparkApi.answer)
    # # 将JSON字符串转换为DataFrame
    # df = pd.DataFrame([SparkApi.answer], columns=['内容'])
    # # 输出到Excel文件
    # df.to_excel('知识点记录.xlsx', index=False, engine='openpyxl')

    # print(content)





if __name__ == '__main__':
    main()

