import base64
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import xml.etree.ElementTree as ET


def b64_to_int(b64_str):
    return int.from_bytes(base64.b64decode(b64_str), byteorder='big')

def rsa_decrypt(private_key: str, encrypted_base64: str) -> str:
    root = ET.fromstring(private_key)
    n = b64_to_int(root.findtext('Modulus'))
    e = b64_to_int(root.findtext('Exponent'))
    d = b64_to_int(root.findtext('D'))
    
    private_key = RSA.construct((n, e, d))
    cipher = PKCS1_v1_5.new(private_key)
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_base64), None)
    
    return decrypted_data.decode('utf-8')


def aes_decrypt(aes_key: str, aes_iv: str, cipher_text: str) -> str:
        cipher_bytes = base64.b64decode(cipher_text)
        cipher = AES.new(base64.b64decode(aes_key), AES.MODE_CBC, base64.b64decode(aes_iv))
        decrypted_padded_data = cipher.decrypt(cipher_bytes)
        unpadded_data = unpad(decrypted_padded_data, AES.block_size)
        return unpadded_data.decode('utf-8')


async def decrypt_idp_token(req_idp_token: str, req_idp_signature: str):
    original_idp_token = base64.b64decode(req_idp_token).decode("utf-8")
    original_signature = base64.b64decode(req_idp_signature).decode("utf-8")

    idp_json = json.loads(original_idp_token)

    ae_key = rsa_decrypt(original_signature, idp_json['privateKey'])
    parts = ae_key.split(',')
    key_part = parts[0]
    iv_part = parts[1]

    idp_data = aes_decrypt(key_part, iv_part, idp_json['data'])

    return json.loads(idp_data)