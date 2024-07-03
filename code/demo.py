# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
#     http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ubinascii

from usr import aes_pkcs7
from ucryptolib import aes
from uos import urandom


class AES_CBC_PKCS7:
    def __init__(self, key, IV=None):
        if IV is None:
            IV = aes_pkcs7.generate_IV(16)
        self.key = key
        self.IV = IV
        self.cipher = aes_pkcs7.new(self.key, aes_pkcs7.MODE_CBC, IV)

    def encrypt(self, data):
        """
        Encrypts data using AES-CBC and returns the Base64-encoded ciphertext.
        """
        self.cipher.encrypt(data)
        base64_encrypted_data = ubinascii.b2a_base64(data)
        return base64_encrypted_data

    def decrypt(self, base64_encrypted_data):
        """
        Performs AES-CBC decryption on Base64-encoded ciphertext and returns the original data.
        """
        encrypted_data = bytearray(ubinascii.a2b_base64(base64_encrypted_data))
        return self.cipher.decrypt(encrypted_data)


# demo
key = aes_pkcs7.generate_key(16)  # AES-128, using a 16-byte key
data = bytearray("Hello, MicroPython!")

aes_cbc_pkcs5 = AES_CBC_PKCS7(key)

encrypted_data_base64 = aes_cbc_pkcs5.encrypt(data)
print("Encrypted data (Base64 encoding):", encrypted_data_base64)

decrypted_data = aes_cbc_pkcs5.decrypt(encrypted_data_base64)
print("Decrypted original data:", decrypted_data)
