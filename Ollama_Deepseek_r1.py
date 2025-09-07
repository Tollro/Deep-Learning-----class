import requests
import json

#/api/generate文本生成
ollama_url = "http://localhost:11434/api/generate"

#请求的数据
data = {
    "model" : "deepseek-r1:1.5b",   #模型名称
    "prompt" : "你好",                 #提示词
    "stream" : False                #是否以流式方式返回结果
}

#发送post请求
response = requests.post(ollama_url, json=data)
#检查响应状态码
if response.status_code == 200:

    print(response)
    #解析jason数据
    result = response.json()
    #打印生成文本
    print(result)
    # print(result["response"])
else:
    print(f"请求失败，状态码：{response.status_code},错误信息：{response.text}")