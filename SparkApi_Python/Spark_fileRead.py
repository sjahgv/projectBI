import pandas as pd
import asyncio
import websockets
import json
# 读取Excel文件
excel_file = 'D:\学习\毕设\标注Excel\标注20-1.xlsx'
df = pd.read_excel(excel_file)

async def send_data_to_starfire():
    appid = "935ff112"  # 填写控制台中获取的 APPID 信息
    api_secret = "MDRlMDVkNzc2MDBjNTUzMzQ4ODFjZmM3"  # 填写控制台中获取的 APISecret 信息
    api_key = "2631b14903cc6f29c0b914e19bc46987"  # 填写控制台中获取的 APIKey 信息
    # 设置认证头信息
    extra_headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # 替换为您的访问令牌
        'Content-Type': 'application/json'
    }

    # 设置API的URL和参数
    api_url = 'wss://spark-api.xf-yun.com/v3.5/chat'  # WebSocket地址，注意使用wss协议
    data = df.to_json(orient='records')  # 将DataFrame转换为JSON格式



    try:
        # 创建WebSocket连接
        async with websockets.connect(api_url) as websocket:
            # 发送请求头
            #await websocket.send(json.dumps({'headers': {'Content-Type': 'application/json'}}))

            # 发送数据
            await websocket.send(data)
            print('数据发送成功')
    except Exception as e:
        print('数据发送失败', e)

# 运行协程
asyncio.run(send_data_to_starfire())