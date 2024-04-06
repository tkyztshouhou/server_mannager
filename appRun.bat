@echo off

cmd /k start
rem 切换到 D 盘
d:

rem 进入 myvenv 的 Scripts 目录
cd D:\02.workplace\myvenv\Scripts

rem 激活虚拟环境
activate.bat

rem 进入工作目录
cd D:\02.workplace

rem 运行 Flask 服务器脚本
python flaskserver.py

