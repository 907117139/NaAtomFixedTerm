========
环境需求
========
- python 3.x
- pandas
- numpy


========
环境配置
========
- 安装Pycharm IDE（http://www.jetbrains.com/pycharm/download/#section=windows），选择community版本
- 安装Anaconda（https://www.anaconda.com/download/），选择python 3.6版本
- Pycharm IDE 配置python解释器
    - 点击File->settings->project interpreter->Anaconda3 python.exe->apply->ok
    - 等待pycharm IDE同步结束，即右下角的process running结束即可


========
运行方式
========
-Windows环境下
    - 若只需要gui界面，则右键gui.pyw选择pythonw运行
    - 若需要看到调试信息，则直接点击运行gui.py

=======
生成exe
=======
打开Anaconda Prompt并按照顺序运行下列命令
- pip install pyinstaller，这一步是为了安装pyinstaller这个工具，若安装，可省略
- pyinstaller -w *.py，代表你要执行的文件名
- 生成的exe文件在一个dist的文件夹里面

================
上传以及下载更新
================
利用git以及github实现代码托管和同步
- 从github上面下载源码
    - 在所要存放源码的目录右键打开Git Bash Here
    - 键入命令 git clone xxx, 其中xxx代表你的github代码仓库地址
- 同步github上面的代码到本地
    - 进入源码的目录
    - 右键打开Git Bash Here
    - 键入命令git pull 即可
- 上传本地代码到github
    - 进入源码的目录
    - 右键打开Git Gui Here
    - 选中修改过的文件
    - 点击stage changed 按钮
    - 在按钮旁边的空白区域编写commit注释
    - 点击push即可