from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2 #Can perform key derivation according to the PKCS#5 standard (v2.0).


# === Salt ===

#This salt was generated using the 'get_random_bytes func. 
salt = get_random_bytes(32)
#salt = b'\xf6\xef\ny\xa8Ht\xcdZ\xa8-f\x18\x1d\xac2\x06\xaee\xbd,\xb3V>%\x8a\xa5I\xdc\x15\x8ag' 
password = 'password123' # Password provided by the user, can use input() to get this

# === Key ===
 

key = PBKDF2(password, salt, dkLen=32) # Your key that you can encrypt with

# === Data ===

# This is your data
data_to_encrypt = 'This is the confidential string!, Do not share.' 

# === Encrypt ===

# First make your data a bytes object.
data = data_to_encrypt.encode('utf-8')

# Create the cipher object and encrypt the data
cipher_encrypt = AES.new(key, AES.MODE_CFB)
ciphered_bytes = cipher_encrypt.encrypt(data)

# This is now our data
iv = cipher_encrypt.iv #
ciphered_data = ciphered_bytes

# From here we now assume that we do not know data_to_encrypt or data (we will use it for proof afterwards)
# We do know the iv, data and the key you have stored / generate

# === Decrypt ===

# Create the cipher object and decrypt the data
cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
deciphered_bytes = cipher_decrypt.decrypt(ciphered_data)

# Convert the bytes object back to the string
decrypted_data = deciphered_bytes.decode('utf-8')

# === Demonstrate ===
print()
print(f'Data to encrypt: {data_to_encrypt}')
print()
print(f'HC-salt used: {salt}')
print()
print(f'Key used: {key}')
print()
print(f'Data result/encrypt: {ciphered_data}')
print()
print(f'Data result/decrypt: {decrypted_data}')
print()
print(decrypted_data == data_to_encrypt)

def crypttxt():
    f = open('cyphertext.txt','wb')
    f.write(ciphered_data)
    f.close

crypttxt()

def decrypttxt():
    f = open('decrypttext.txt', 'w')
    f.write(decrypted_data)
    f.close
 
decrypttxt()


