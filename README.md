# 量化交易实验室（Quant Lab）

本项目旨在为量化交易策略的开发、回测与实盘提供一站式实验环境。

## 目录结构

- `data/`         —— 数据存储与处理
- `strategies/`   —— 策略开发与管理
- `backtest/`     —— 回测框架与结果
- `utils/`        —— 工具函数与通用模块
- `notebooks/`    —— 研究与分析 Jupyter 笔记本

## 快速开始

1. 创建并激活环境：
   ```bash
   uv venv
   source .venv/bin/activate
   ```

2. 安装依赖（使用阿里云镜像源）：
   ```bash
   uv pip install --index-url https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
   ```

3. 运行示例回测：
   ```bash
   python backtest/sample_backtest.py
   ```

## 依赖环境
本项目使用 uv 进行环境管理，详细依赖列表见 requirements.txt。 