# Python-Course
## Useful Link

### Python Related
* https://www.programcreek.com/python/
* https://pymotw.com/3/
* https://github.com/Legrandin/pycryptodome
* https://pythonguidecn.readthedocs.io/zh/latest/

### Mysql Connector

* https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html
* https://github.com/PyMySQL/mysqlclient

## Virtual Environments
* https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

## Poetry Related
* https://python-poetry.org/docs/
* https://zhuanlan.zhihu.com/p/490103248
* https://www.kancloud.cn/madxzb/python-guide/2248089

### 安装 
```bash
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
### 创建项目 
如果你是在一个已有的项目里使用 Poetry，你只需要执行 poetry init 命令来创建一个 pyproject.toml 文件：
$ poetry init
而如果是新建 一个项目，可以使用这个命令
$ poetry new demo

### 创建虚拟环境
使用 poetry install 命令创建虚拟环境（确保当前目录有 pyproject.toml 文件）：
$ poetry install


### 使用虚拟环境
创建虚拟环境后，如果想要在虚拟环境下执行命令，比如去执行脚本，去使用 pip list 等等。

可以在项目目录下，使用如下命令

$ poetry run <commands>
比如我查看该虚拟环境中安装了哪些包

$ poetry run pip list
再比如我想在该虚拟环境下执行 app.py

$ poetry run python app.py
每次在虚拟环境下做点啥事，命令前面都要加上 poetry run，有点太麻烦了。

这时可以使用下面这条命令，直接激活当前的虚拟环境

$ poetry shell

### 包的管理
安装包
$ poetry add <pkg>
添加 --dev 参数可以指定为开发依赖

$ poetry add pytest --dev
查看所有安装的依赖包

$ poetry show
加上 --tree 可以查看他们的依赖关系

$ poetry show --tree
加上 --outdated 可以查看可以更新的依赖

$ poetry show --outdated
如果要更新依赖可以执行这个命令

更新全部
$ poetry update

更新某个依赖
$ poetry update foo
想卸载某个包，用这个命令

$ poetry remove foo
