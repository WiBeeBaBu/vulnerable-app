import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # 演示使用requests库
    response = requests.get('https://api.github.com')
    return f'GitHub API status: {response.status_code}'

@app.route('/fetch')
def fetch_url():
    # 模拟一个可能受影响的请求
    url = input("请输入要请求的URL: ")  # 这里模拟可能的SSRF漏洞场景
    return requests.get(url).text

if __name__ == '__main__':
    app.run(debug=True)
