# VDL 自动化测试项目

## 项目简介
本项目是 VDL 软件的自动化测试框架，基于 Python 开发，使用 Airtest 和 Pytest 进行自动化测试实现。

## 环境要求
- Python 3.7+
- Windows 10/11
- VDL 软件

## 快速开始

### 1. 环境配置
```bash
# 克隆项目
git clone [项目地址]

# 进入项目目录
cd VDL_autotest

# 安装依赖
pip install -r requirements.txt
```

### 2. 依赖安装
项目依赖已通过 `requirements.txt` 管理，主要包含以下核心依赖：
- airtest: UI 自动化测试框架
- pytest: 测试框架
- easyocr: OCR 文字识别
- allure-pytest: 测试报告生成
- nvidia-ml-py3: GPU 监控
- psutil: 系统资源监控
- pandas: 数据处理

### 3. 运行测试
```bash
# 运行所有测试用例
python run.py

# 运行指定测试用例
pytest testcase/test00_smoke.py
```

## 项目结构
```
VDL_autotest/
├── common/          # 公共类和方法
├── configs/         # 配置文件
├── drafts/          # 草稿箱
├── elements/        # UI 控件元素定义
├── logs/           # 日志文件
├── pages/          # 页面对象模型
├── report/         # 测试报告
├── testcase/       # 测试用例
├── tools/          # 工具类
└── run.py          # 测试运行入口
```

## 测试用例说明
测试用例按功能模块划分：
- test00_smoke.py: 单模块方案冒烟测试
- test01_management.py: 方案管理tab功能测试
- test02_data.py: 数据管理tab功能测试
- test03_label.py: 图像标注tab功能测试
- test04_training.py: 模型训练tab功能测试
- test05_evaluate.py: 模型评估tab功能测试
- test06_infer.py: 模型推理tab功能测试
- test07_menu.py: 菜单功能测试
- test08_unite_judgement.py: 综合判定功能测试
- test09_pipelines.py: 串联方案冒烟测试
- test10_compatible.py: 算法对比测试
- test11_autolabel.py: 自动标注功能测试
- test12_dark.py: 深色版本测试
- test13_generation.py: 缺陷生成功能测试

## 测试报告
测试执行完成后，可通过以下命令查看测试报告：
```bash
allure serve report
```

## 开发指南

### 添加新的测试用例
1. 在 `testcase` 目录下创建新的测试文件
2. 在 `elements` 目录下定义所需的 UI 元素
3. 在 `pages` 目录下实现页面操作方法
4. 在 `run.py` 中添加新的测试用例路径

### 编写测试用例规范
- 使用 Pytest 的 fixture 进行测试前置和后置处理
- 使用 Allure 装饰器添加测试步骤和描述
- 遵循页面对象模型设计模式
- 保持测试用例的独立性和可重复性

## 常见问题
1. 环境配置问题
   - 确保 Python 版本兼容
   - 检查依赖安装是否完整
   - 验证 VDL 软件版本

2. 测试执行问题
   - 检查日志文件排查错误
   - 确认 UI 元素定位是否准确
   - 验证测试环境是否正常

## 维护者
[yun.liu]

