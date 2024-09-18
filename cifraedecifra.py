
# creazione environment
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generating RSA Key Pair
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
spubkeycollega='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6Cqr81Z6cnMGqTGScdt8\nMkQLj4myO/2g153m4s891i7n2jIqyS57nd/00BR9swVKeCzfPDFppeNn62N7wtAm\n5dk3gk1wcEm96fHzjmDxQhM+eDXFutdyEwLENQ3JfhrsSsXjiJsDotBCmRPo2V7E\nnflMib12E/bWf3oDAPxv10t9HHMun9HL8q1f6YyfdWgFGGW1q1/ZFfEPFxtL5xXI\n+m5FoRihqfscjYndPwCbgS2xTKD6W8dt7rroYLGO+TbPi/JbdIMgPO08Ve6I+Qom\nz7a9UhBYlu5I2cSTvLslIUBw45l/yLguq4dyNPixzl47KSbMcgxzdw08phEwYZ6T\nxQIDAQAB\n-----END PUBLIC KEY-----'
sPriv='-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA0xF3p+YjlDhipXdSOESvkYr0LeL1Tanzp93UiNjVzWZY8HZL\nmdvqEcO9e7CAq4PiXiaBjaSYRTmams2GnccdcLFvrKUPGQuWaUBwAfBN6D9uyXCm\n4V1V0HeQ7sO3hTrKQWWE8GkHFazf5aTGSqXKd2Sj0h1iHiSd5Xf3Ni/7jaDSZtwU\npClODY/eCgo02zUbiVFvNZ0sQs/f4RLY2TPALbOO4JLPPTfOtl8eGMNpBq8zTzdJ\niCBCmfLVgdFH23IuOWrP42f+qDM9ik1UwD+iNrmJ0ynerTHnQJNV/ZugSHshallK\nvvRXMNs2TWVr/B3HJx6+ZW6ZlZLI4OcjhGa6yQIDAQABAoIBACQ0uNvaRHwmd/V+\nVGJGlf9XYK+GYSHjZ2KCUPTwjSxgxBzrjehkqvBFLXnMOyYwx2HzJQIRG/Wz/etU\nGiVyhIBST5/D6KUZMcH4Rb5vZE3Uo8J2SooaIqBSAlCSziZSgWNacMV0nrx/HSEd\ndM5VRjfY0ak3VR9qlJNKUuO+s14FymfcsEPbancNwb2EbcBr5kVmXaCsXsnvmDKf\nClRtqiPx8Vl6wb5newIPXEBC82PS4FeBqasuj+ZCa141TdDYgNw/ZXTEJTieM0KK\nbJFuWfL54Ru4BiC7iAfwrDXUAQUUNs0sCqmZ2HHRmpzqDqsPg267UzxSebOBujgz\nf8dVfKkCgYEA2fnzQwz2f2LBWSfqsuC3YrYigBTyvyqE9Rs0mrdysefLUynnsqlG\nPWJSQnbhqsMrbJ8CM5TF9ZXNbtAHtFkt92yIH5I8rRYCJ8s3OU3sZo64cyJ6CpZN\nLzpgLW7F+8kehYg4hHLW1RYwTR+ZIlFJdhd33ba32XgMisXQiuQk/0MCgYEA9+MG\nPKalHTgT3R4Zmo13yRmUPrbG8tljapvNpKmQoUvfGFbjVHqX85N74sqSASZFDxgA\nOoC26WTT4wORd1Bjmah9ixq1UNMyC0zTLbZ7mUNyt727ZmdJFE6wZk2z1HnHAFIZ\nrG/PTxpkrEaDSoHWCTvEKbJdKnW1qNyElY48/wMCgYBt+W6jUKH5CTE1sy71iuzb\nL7teVbNXgbNNGqnCuXVzjtgFoGnWuRLIG5gXEnWuuwNorRzmO1RZIHhiRTDt6+SG\nJcrT6usUBLuXqi61ibwQzkb/R9C9ELHmdxRZN79J1mHAy0aAhJQhNC2wa5XOO6bN\nnu+J/Arr/GaPiVg7CvojkwKBgQDp8t1ECJL0jKRSn8HSV4mhxf5fYelJ8VkemITw\nzwes8wpO0lIivMEEJUFavYwmgZPTtvcgP7Jhe8NuEUQMs1YNAzPZQQ+2hFxKxerY\nzczAzSNLvklLUFdsTwe0xcje0z+5UcLhN3UUVviEjtgCTZ9Pf5SXNbswA3+7KsQG\n0gNHOQKBgQDJMUQ2XYsYk4c0lU+7ZJ1iAOwQytw1EkbwhlOE4TkD1J5a5HtujeMI\nIxgMTrksIRyBItFQrmGIypA/cq10GqmBi8xRGDYn7h4SCR45q+x5C9+uIwjlV72r\nIPCIoe2uSxnCTNQ814WvF7/cYVjqzo/hsv8ADK3wea0u6Vi0vEgfKA==\n-----END RSA PRIVATE KEY-----'
sPub='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0xF3p+YjlDhipXdSOESv\nkYr0LeL1Tanzp93UiNjVzWZY8HZLmdvqEcO9e7CAq4PiXiaBjaSYRTmams2Gnccd\ncLFvrKUPGQuWaUBwAfBN6D9uyXCm4V1V0HeQ7sO3hTrKQWWE8GkHFazf5aTGSqXK\nd2Sj0h1iHiSd5Xf3Ni/7jaDSZtwUpClODY/eCgo02zUbiVFvNZ0sQs/f4RLY2TPA\nLbOO4JLPPTfOtl8eGMNpBq8zTzdJiCBCmfLVgdFH23IuOWrP42f+qDM9ik1UwD+i\nNrmJ0ynerTHnQJNV/ZugSHshallKvvRXMNs2TWVr/B3HJx6+ZW6ZlZLI4OcjhGa6\nyQIDAQAB\n-----END PUBLIC KEY-----'

#ora ricreiamo le chiavi partendo da queste due stringe
key_pair=RSA.import_key(sPriv)
public_key=  RSA.import_key(sPub)

# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "This is a secret message"
noncifrato= "io sono batman"
messaggiogab='v1PhSzyHzWfvPRkPhvaNAaApF3CQKxKE/UUUUZJV7g595Y8DaZmuXTmMbah1t4rq4kkzdmaLAs/1Piure2QMf91uRpPK2T6xbqPpp9NmftNqkuNSGJ3mf83yMWWFHPFQ4j5rVnWkw4UnsWMzLdjgvTWcWQ0TlqBGjg0iwU35dmOt4bm0Ex3g0d8CtNmV9pXXRpck2+Pq7FQhKOCgcACPGNC0Wl6zWSO9J5l2WA/zpWXZd9mr13h7NgSSPR+siCqfyJId+hfoSTHrcW4De2XiQtgEfZV5faBQSD8+bG3cPf1agUSb6Gvr/JTjRHh3UbFvYEX4Nc17OalD9U5oKtaCUw=='
# decrypted_message = decrypt_message(encrypted_message, key_pair)

# # batman
# print("Original Message:", noncifrato)
# print("Encrypted Message:", encrypted_message)

# messaggio gabriele
print(decrypt_message(messaggiogab, key_pair))
# print("Decrypted Message:", decrypted_message)
