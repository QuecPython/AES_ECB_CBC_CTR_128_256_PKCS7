# QuecPython AES 加解密

中文 | [English](README.md)

## 概述

QuecPython aes加解密，用户可以在线程中调用 `aes_pkcs7.new` 方法创建一个加解密对象 `aes_pkcs7`，并调用 `aes_pkcs7.encrypt` `aes_pkcs7.decrypt` 方法实现加解密，demo默认为pkcs7填充，暂不支持其他填充方式。

pkcs7补位规则：
补位的个数: 不足16位字节的倍数,补足变成16位的倍数。
补位的值: 等于补位个数的unicode码, 比如:content有7位,那么补充9个字节,每个字节的值都是\x09。


## 用法

- [API 参考手册](./docs/zh/API参考手册.md)
- [示例代码](./code/demo.py)

## 贡献

我们欢迎对本项目的改进做出贡献！请按照以下步骤进行贡献：

1. Fork 此仓库。
2. 创建一个新分支（`git checkout -b feature/your-feature`）。
3. 提交您的更改（`git commit -m 'Add your feature'`）。
4. 推送到分支（`git push origin feature/your-feature`）。
5. 打开一个 Pull Request。

## 许可证

本项目使用 Apache 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。

## 支持

如果您有任何问题或需要支持，请参阅 [QuecPython 文档](https://python.quectel.com/doc) 或在本仓库中打开一个 issue。
