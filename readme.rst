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
- pip install pyinstaller，这一步是为了安装pyinstaller这个工具，若安装，可省略
- pyinstaller *.py，代表你要执行的文件名
- 生成的exe文件在一个dist的文件夹里面