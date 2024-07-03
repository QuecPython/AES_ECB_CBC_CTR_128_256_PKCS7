# QuecPython AES加解密 API 参考手册

QuecPython aes加解密，用户可以在线程中调用 `aes_pkcs7.new` 方法创建一个加解密对象 `aes_pkcs7`，并调用 `aes_pkcs7.encrypt` `aes_pkcs7.decrypt` 方法实现加解密，demo默认为pkcs7填充，暂不支持其他填充方式。

pkcs7补位规则：
补位的个数: 不足16位字节的倍数,补足变成16位的倍数。
补位的值: 等于补位个数的unicode码, 比如:content有7位,那么补充9个字节,每个字节的值都是\x09。


## 创建 aes 加解密对象

### `aes_pkcs7.new`

```python
aes_pkcs7.new(key, mode, IV)
```

**参数**

- `key` - 加解密需要使用的密码信息，hex字符串。
- `mode` - 选择aes加解密模式。
    - MODE_ECB:用于电子密码本模式。
    - MODE_CBC:用于密码块链接。
    - MODE_CTR:用于计数器模式。
- `IV` - 加解密向量，hex字符串，可选参数。
    - MODE_CTR 和 MODE_CBC模式，必须填写IV向量。

**返回值**

返回aes加解密对象 `cipher`。


## aes加密

### `cipher.encrypt`

```python
cipher.encrypt(data)
```
**参数**

- `data` - 需要加密的用户数据，hex字符串。


**返回值**

返回aes加密数据，hex字符串。


## aes解密

### `cipher.decrypt`

```python
cipher.decrypt(data)
```
**参数**

- `data` - 需要解密的用户数据。

**返回值**

返回aes解密数据，hex字符串。

> - 一般需要结合import ubinascii，做Base64转换。
