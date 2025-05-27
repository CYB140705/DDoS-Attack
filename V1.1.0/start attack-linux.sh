#!/bin/bash

# 基本安全检查版本
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到python3，请先安装Python 3"
    exit 1
fi

SCRIPT_PATH="./ddos-linux.py"

if [ ! -f "$SCRIPT_PATH" ]; then
    echo "错误：脚本文件 $SCRIPT_PATH 不存在"
    exit 1
fi

# 添加日志记录
echo "$(date): 启动"邪恶"脚本 $SCRIPT_PATH" >> script_log.txt

# 执行并检查返回值
if ! python3 "$SCRIPT_PATH"; then
    echo "错误：脚本执行失败" >&2
    exit 1
fi
