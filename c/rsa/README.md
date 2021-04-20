from https://github.com/terrantsh/RSA2048.git
RSA2048公钥私钥加密解密
注意默认是2048bit加密，如果用1024bit加密的时候，模和指数需要copy到数组的后部分，参考test函数。

# RSA2048

### Public key encryption, private key decryption;Private key encryption, public key decryption.

Implement RSA algorithm based on C language, support public key encrypted, decrypted, private key encrypted, decrypted.

### among them:

  Function RSA2048 is used to encrypt and decrypt.

  此工程实现了RSA2048利用已有公钥私钥进行加密解密的过程，实现方式是使用PSCK1方式进行填充
