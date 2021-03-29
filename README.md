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


 会在一个名为dist的文件夹中找到新创建的归档文件，dist文件夹也是由setuptools创建。

3. 安装发布文件

pip表示 Package Installer for Python (Python的包安装工具)


windows 切换到 dist 文件路径下，执行 py -3 -m pip install xxx-.tar.gz

linux   执行 sudo python3 -m pip install xxx-.tar.gz

```


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

# chapter 05

### Python中的函数参数支持按值还是按引用调用语义？

**Python 的函数参数语义即支持按值调用也支持按引用调用**

解释器会查看对象引用（内存地址）指示的那个值类型，如果变量指示一个可变的值，就会应用按引用调用语义；
如果所指示的数据的类型是不可变的，则会应用按值调用语义。

列表、字典和集合（都是可变的）总是会按引用传入函数，函数代码组中对变量数据结构的任何改变都会反映到调用代码中。

字符串、整数和元组（不可变）总是会按值传入函数，函数中对变量的任何修改是这个函数私有的，不会反映到调用代码中。


### 安装pytest和PEP8插件

```
py -3 -m pip install pytest
```

```
py -3 -m pip install pytest-pep8
```

如果在Windows上，要把“py -3”替换未“sudo python3”

安装了pytest和PEP后，不论使用什么操作系统，检查代码的PEP 8 兼容性，都要执行同一个命令
```
py.test --pep8 vsearch.py
```

若出现   
```
Direct construction of Pep8Item has been deprecated, please use Pep8Item.from_parent.
```

[可以尝试使用](https://stackoverflow.com/questions/65713241/pep8-compliance-testing-is-failing)   
```
pep8 vsearch.py
```

或[pycodestyle](https://zhuanlan.zhihu.com/p/90642746)   



### 安装Flask

Python社区维护了一个集中管理第三方模块的网站，名为PyPI（表示Python Package Index）。

Linux
```
sudo -H python3 -m pip install flask
```

windows
```
py -3 -m pip install flask
```

Flask 依赖另外4个模块： Werkzeug, MarkupSafe, Jinja2 和 itsdangerous .


hello_flask.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell() -> str:
    return 'Hello world from Flask!'

app.run()
```

__name__值由Python解释器维护，在程序代码中的任何地方使用这个值时，它会设置为当前活动模块的名字（指出当前活动的命名空间）。

如果要运行应用，最好在操作系统的命令行上直接通过解释器运行代码。


### 函数的参数类型、返回值类型、默认值

```
def search4vowels(phrase :str)->set:
    """ return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase :str,letters :str='aeiou')->set:
    """Return a set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
```



### Method Not Allowed
GET请求是Flask的默认HTTP方法，我们可以修改对应的``` @app.route('/search4', methods=['POST'])```来支持特定的请求方式

当然也可以同时支持GET、POST ``` @app.route('/search4', methods=['GET', POST']) ```


### 避免“编辑/停止/启动/测试循环”

Flask允许再调试模式运行web应用，每次Flask注意到代码已经改变时，就会自动重启你的web应用（当然还不只这些）。

打开调试模式：``` app.run(debug=True) ```

只有你正确地完成了代码修改，才会自动重新加载。如果你的代码有错误，Web应用就会转到命令行提示窗口，要想再次运行，
需要修正代码错误，然后手动重启Web应用。

### chapter05

```
 +-------------+            |    +----------------+
 |   webapp    |  --------  |----| vsearch4web.py |
 +-------------+            |    +----------------+
                            |
                            |
                            |
                            |    +--------+    +--------+
                            |----| static |----| hf.css |
                            |    +--------+    +--------+
                            |
                            |    +-----------+    +-----------+    +------------+    +--------------+
                            |----| templates |----| base.html |----| entry.html |----| results.html |
                            |    +-----------+    +-----------+    +------------+    +--------------+
```


render_template调用中最后还多一个逗号，这个额外的都会看起来有些奇怪，不过，这是一个完全合法的Python语法（可选，没有严格要求必须如此）。   

vsearch4web.py
```
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Wecome to search4letters on the web!')
    

app.run(debug=True)
```


### 重定向来避免不想要的错误

需要从Flask中导入redirect，修改vsearch4web.py中的hello函数，其它不用改动

vsearch4web.py
```
from flask import Flask, render_template, request, redirect
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Wecome to search4letters on the web!')
    

app.run(debug=True)

```

重定向有些浪费，一个请求指向"/" URL，Web应用首先响应一个302重定向，然后Web浏览器会发送另一个请求指向"/entry" URL。
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [26/Mar/2021 14:57:48] "[32mGET / HTTP/1.1[0m" 302 -
127.0.0.1 - - [26/Mar/2021 14:57:48] "[37mGET /entry HTTP/1.1[0m" 200 -
```

### 函数可以有多个URL

Flask可以为一个给定的函数关联多个URL。Flask会尝试依次与各个URL匹配，如果找到一个匹配，就会执行这个函数。

vsearch4web.py
```
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Wecome to search4letters on the web!')
    

app.run(debug=True)
```

现在访问"/" URL时，Web应用的状态消息只会有一个请求。

```
 * Detected change in 'D:\\learn\\python\\mymodules\\webapp\\vsearch4web.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 826-699-626
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [26/Mar/2021 15:02:58] "[37mGET / HTTP/1.1[0m" 200 -
```

### __name__  __main__

dunder.py
```
print('We start off in:', __name__)
if __name__ == '__main__':
    print('And end up in:', __name__)
```

命令窗口执行输出：
```
================= RESTART: D:/learn/python/mymodules/dunder.py =================
We start off in: __main__
And end up in: __main__
```

如果你的程序代码直接由Python执行，dunder.py 中的if语句会返回True，因为活动命名空间时__main__。不过，如果你的
程序作为一个模块导入，if语句总是返回False，因为__name__的值不是__main__，而时所导入的模块名字。

vsearch4web.py
```
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Wecome to search4letters on the web!')
    

if __name__ == '__main__':
    app.run(debug=True)
```

### Web应用部署到 PythonAnywhere



# chapter 06 存储和管理数据


### Python 打开、处理、关闭 文件
打开文件写入：
```
>>> todos = open('todos.txt', 'a')
>>> print('Put out the trash.', file=todos)
>>> print('Feed the cat.', file=todos)
>>> print('Prepare tax return.', file=todos)
>>> todos.close()
```

输出文件内容：
```
>>> tasks = open('todos.txt')
>>> for chore in tasks:
	print(chore, end='')

>>> tasks.close()
```

**open** 的第一个参数是要处理的文件名，第二个参数是可选的（关于open的更多详细内容可以参考Python文档）。
* 'r' 打开一个文件来读数据（默认）；
* 'w' 打开一个文件来写数据；
* 'a' 打开一个文件来追加数据；
* 'x' 打开一个新文件来写数据。

### 比“打开、处理、关闭”更好的“with”

```
with open(todos.txt) as tasks:
	for chore in tasks:
		print(chore, end='')
```

with语句会管理其代码组运行的上下文，结合使用with和open时，解释器会为你完成收尾的清理工作，在需要时调用close。

vsearch4web.py 增加日志输出到vsearch.log文件
```
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file = log)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Wecome to search4letters on the web!')
    

if __name__ == '__main__':
    app.run(debug=True)
```

vsearch4web.py 增加查看日志文件的方法
```
from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file = log)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Wecome to search4letters on the web!')
    

@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)

```

解释器提供了一个read()方法，它会一次性返回文件的全部内容。

escape用来专用特殊符号。


### 更多的了解请求对象

要了解Python中某个对象包含什么时，可以把这个对象提供给dir内置方法，查看它的方法和属性列表。

```
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(str(dir(req)), res, file = log)
```


* req.form: 从Web应用的HTML表单提交的数据   
* req.remote_addr: 运行Web浏览器的IP地址   
* req.user_agent: 提交数据的浏览器的标识   


### 记录特定的Web请求属性

```
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, file=log)
        print(req.remote_addr, file=log)
        print(req.user_agent, file=log)
        print(res, file=log)
```

```
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, file=log, end='|')
        print(req.remote_addr, file=log, end='|')
        print(req.user_agent, file=log, end='|')
        print(res, file=log)
```


```
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
```
