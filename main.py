#! /usr/bin/python3  # 指定使用 Python 3 解释器执行此脚本
# -*- coding: utf-8 -*-  # 指定源文件的编码为 UTF-8，以支持中文字符

from bot import bot  # 从 bot 模块导入 bot 对象

# 面板模块，处理与面板相关的功能
from bot.modules.panel import *  # 导入面板模块中的所有内容

# 命令模块，处理与命令相关的功能
from bot.modules.commands import *  # 导入命令模块中的所有内容

# 其他模块，可能包含一些额外的功能
from bot.modules.extra import *  # 导入额外模块中的所有内容
from bot.modules.callback import *  # 导入回调模块中的所有内容

from bot.web import *  # 导入 web 模块中的所有内容，用于处理与网络相关的功能

bot.run()  # 运行 bot 对象，启动程序
