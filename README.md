# head-first-python

### 1. 函数返回值 

```
空列表返回[]  空字典返回{}  空集合返回set()  空元组返回()
```
### 2. 发布文件

```
1. 创建文件发布描述（生成setup.py,README.txt）

2. 生成一个发布文件

需要发布的文件与 setup.py、README.txt 放在同一个文件夹下

windows 切换到当前需要发布的文件路径下，执行 py -3 setup.py sdist

linux   执行 python3 setup.py sdist

```

 会在一个名为dist的文件夹中找到新创建的归档文件，dist文件夹也是由setuptools创建。

3. 安装发布文件

pip表示 Package Installer for Python (Python的包安装工具)


windows 切换到 dist 文件路径下，执行 py -3 -m pip install xxx-.tar.gz

linux   执行 sudo python3 -m pip install xxx-.tar.gz



setup.py   
```
from setuptools import setup

setup(
    name = 'vsearch',
    version = '1.0',
    description = 'The Head First Python Search Tools',
    author = 'xiechong',
    author_email = 'xiechongyn@163.com',
    url = 'headfirstlabs.com',
    py_modules = ['vsearch'],
    )
```

README.txt 可为空文件
