@echo off
rem 以管理员身份启动 CMD
start "" "cmd.exe" /c "cd /d %~dp0 && echo UAC Succeded && start cmd /k "

ping 127.0.0.1 -n 2 > nul

rem 切换到 D 盘
d:

ping 127.0.0.1 -n 2 > nul

rem 进入到 D:\02.workplace\myvenv\Scripts 目录
cd D:\02.workplace\myvenv\Scripts

ping 127.0.0.1 -n 2 > nul

rem 启动 Python 虚拟环境并执行 activate.bat
activate.bat

ping 127.0.0.1 -n 2 > nul

rem 切换到 D:\02.workplace 目录
cd D:\02.workplace

ping 127.0.0.1 -n 2 > nul

rem 启动 Python 脚本 flaskserver.py
python flaskserver.py