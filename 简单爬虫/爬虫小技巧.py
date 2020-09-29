import requests

# 1、reqeusts.util.dict_from_cookiejar  把cookie对象转化为字典
url = 'http://www.baidu.com'
response = requests.get(url)
print(response.cookies)
cookjar = response.cookies

# 将cookjar对象转换成字典类型数据
dict_cookies = requests.utils.dict_from_cookiejar(cookjar)
print(dict_cookies)
# 将字典类型数据转换成cookjar对象
print(requests.utils.cookiejar_from_dict(dict_cookies))


# 2、quote url编码
response = requests.get("http://www.baidu.com?kw='黑马程序员'")
print(response.url)
url = requests.utils.unquote(response.url)
print(url)
encode_url = requests.utils.quote(url)
print(encode_url)

# 3、https证书
response = requests.get("https://www.12306.cn/mormhweb", verify=False)
print(response.status_code)
print(response.content.decode())
