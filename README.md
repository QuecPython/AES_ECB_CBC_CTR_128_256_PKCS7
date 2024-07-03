# QuecPython AES encryption and decryption

[中文](README_ZH.md) | English

## Overview

QuecPython aes encryption and decryption, users can call the `aes_pkcs7.new` method in the thread to create an encryption and decryption object `aes_pkcs7`, and call the `aes_pkcs7.encrypt` `aes_pkcs7.decrypt` methods to implement encryption and decryption. The demo defaults to pkcs7 padding and does not support other padding methods.

PKCS7 padding rules:
Number of padding: If it is less than a multiple of 16-bit bytes, it will be padded to become a multiple of 16 bits.
Value of padding: Unicode code equal to the number of paddings, for example: if content has 7 bits, then 9 bytes are padded, and the value of each byte is \x09.

## Usage

- [API Reference Manual](./docs/en/API_Reference.md)
- [Example Code](./code/demo.py)

## Contribution

We welcome contributions to improve this project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need support, please refer to the [QuecPython documentation](https://python.quectel.com/doc/en) or open an issue in this repository.