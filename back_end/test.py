import base64, os, random, string

# 随机生成字符
print(base64.b64encode(os.urandom(48)))
print(''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 48)))
