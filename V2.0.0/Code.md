# DDoS 攻击演示工具 - 说明文档

## 📌 免责声明

⚠️ **重要提示**：此程序仅用于教育目的，展示基本的网络概念。实际使用DDoS攻击技术违反大多数国家的法律。未经授权对任何网络或系统发起攻击是非法行为。

开发者不承担任何因使用此程序导致的直接或间接法律责任。使用者应自行承担所有风险。

## 🖥️ 程序信息

- **名称**: DDoS Attack
- **版本**: V2.0.0
- **开发者**: CYB140705
- **GitHub**: [https://github.com/CYB140705/DDoS-Attack](https://github.com/CYB140705/DDoS-Attack)
- **开发语言**: Python 3
- **平台**: Windows / Mac / Linux

## 🔧 功能说明

此程序是一个简单的UDP洪水攻击(DDoS)演示工具，主要用于教学目的，展示:
- 基本的socket编程
- UDP数据包发送
- 简单的用户交互界面

## 📦 依赖项

本程序使用Python标准库，无需额外安装依赖:
- `socket`
- `random`
- `time`
- `os`
- `sys`
- `datetime`

## 🚀 使用方法

1. 确保已安装Python 3环境
2. 运行程序:
   ```bash
   python ddos-windows.py(适用于Windows) / ddos-linux.py(适用于Linux/Mac)
   ```
3. 按照提示输入:
   - 目标IP地址
   - 目标端口号
   - 攻击速度(1~1000)

## ⚠️ 注意事项

1. **合法使用**：仅可在自己拥有或获得明确授权的网络上测试
2. **道德考量**：滥用此技术可能导致严重后果
3. **性能影响**：高速发送可能导致本地网络拥堵

## 📜 License

此代码可自由转载，但必须:
1. 保留原始作者信息
2. 注明来源(GitHub链接)
3. 包含完整的免责声明

---

> 💡 **教育目的**：建议将此程序用于学习网络安全防御技术，了解攻击原理才能更好地防护系统。






> __**V1.1.0的最后一次更新!!!(CYB的笑**__








## 更新内容(Windows)

1. **添加了攻击日志(Date)**
    ```python
            # 每100000个包记录一次日志，避免过于频繁的日志写入
        if sent % 100000 == 0:
            logger.info(f"已发送 {sent} 个数据包到 {ip}:{port}")
    except KeyboardInterrupt:
        logger.info(f"攻击被用户中断 - 总共发送了 {sent} 个数据包")
    except Exception as e:
    logger.error(f"发生错误: {str(e)} - 总共发送了 {sent} 个数据包")
    finally:
    # 记录攻击结束信息
    duration = (datetime.now() - now).total_seconds()
    logger.info(f"攻击结束 - 持续时间: {duration:.2f}秒, "
                f"总数据包: {sent}, "
                f"平均速率: {(sent/duration):.2f}包/秒"
                if duration > 0 else "攻击结束")
    ```

2. **这是日志保存逻辑**
    ```python
    # 设置日志配置
    def setup_logging():
        log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # 创建logs目录如果不存在
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # 设置回滚日志文件，每个最大1MB，保留3个备份
    log_file = 'logs/ddos_attack.log'
    file_handler = RotatingFileHandler(
        log_file, mode='a', maxBytes=1024*1024, 
        backupCount=3, encoding='utf-8', delay=False)
    file_handler.setFormatter(log_formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
        return logger

    logger = setup_logging()
    ```

3. **添加了端口号输入提示**
    ```python
    port = int(input("IP的开放端口(端口号必须在1~65535之间)          :"))
    ```

    ```MarkDown
    - 先后对比
    *先*
    port = int(input("IP的开放端口          :"))

    *后*
    port = int(input("IP的开放端口(端口号必须在1~65535之间)          :"))

    ```
    *_看懂了吗?_*

## 更新内容(Linux / Mac)

1. **添加了攻击日志(Date)**
    ```python
            # 每100000个包记录一次日志，避免过于频繁的日志写入
        if sent % 100000 == 0:
            logger.info(f"已发送 {sent} 个数据包到 {ip}:{port}")
    except KeyboardInterrupt:
        logger.info(f"攻击被用户中断 - 总共发送了 {sent} 个数据包")
    except Exception as e:
    logger.error(f"发生错误: {str(e)} - 总共发送了 {sent} 个数据包")
    finally:
    # 记录攻击结束信息
    duration = (datetime.now() - now).total_seconds()
    logger.info(f"攻击结束 - 持续时间: {duration:.2f}秒, "
                f"总数据包: {sent}, "
                f"平均速率: {(sent/duration):.2f}包/秒"
                if duration > 0 else "攻击结束")
    ```

2. **这是日志保存逻辑**
    ```python
    # 设置日志配置
    def setup_logging():
        log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # 创建logs目录如果不存在
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # 设置回滚日志文件，每个最大1MB，保留3个备份
    log_file = 'logs/ddos_attack.log'
    file_handler = RotatingFileHandler(
        log_file, mode='a', maxBytes=1024*1024, 
        backupCount=3, encoding='utf-8', delay=False)
    file_handler.setFormatter(log_formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
        return logger

    logger = setup_logging()
    ```

3. **添加了端口号输入提示**
    ```python
    port = int(input("IP的开放端口(端口号必须在1~65535之间)          :"))
    ```

    ```log
    - 先后对比
    *先*
    port = int(input("IP的开放端口          :"))

    *后*
    port = int(input("IP的开放端口(端口号必须在1~65535之间)          :"))

    ```

4. **将文字颜色更改为 更科技的绿色(**
    ```python
    os.system("\033[92m")
    ```
    *_看懂了吗?_*
# THE END.