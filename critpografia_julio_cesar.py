import requests
import json
import string
import hashlib

def shift_string(crypted, n):
    decrypted = ''
    for c in crypted:
        if c in string.ascii_lowercase:
            aux = ord(c) - n
            while(aux < ord('a')):
                aux += 26
            decrypted += chr(aux)
        else:
            decrypted += c
    return decrypted

if __name__ == '__main__':
    result = None
    with requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8a0c970229dba902e68071b86b699c64e4691203") as response:
        result = response.json()

    result["decifrado"] = shift_string(result["cifrado"], result["numero_casas"])
    hash = hashlib.sha1()
    hash.update(result["decifrado"].encode())
    result["resumo_criptografico"]= hash.hexdigest()
    with open('answer.json', 'w') as outfile:
        json.dump(result, outfile)

    files = {'answer': ('answer.json', open('answer.json', 'rb'), 'multipart/form-data')}
    response = requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=8a0c970229dba902e68071b86b699c64e4691203", files=files)
