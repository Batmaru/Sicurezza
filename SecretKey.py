

#Sapendo che la chiave di cifra è: XXXXIsASecretKey

#(non conoscete i primi 4 caratteri della chiave)

#e che il messaggio cifrato è: OgJuOYJZT0FDb47DBOkNgA==

#Trovare la decodifica del messaggio.



from Crypto.Cipher import AES
import base64

# Function to pad the message to be multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Encryption
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text


# prova di decifra brute force
enc = "OgJuOYJZT0FDb47DBOkNgA=="
key = "XXXXIsASecretKey"
expected_message= "Hello, World!"

for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key = p1 + p2 + p3 + p4 + "IsASecretKey"
                try:
                    # Prova a decrittare il messaggio con la chiave corrente
                    dec = decrypt(enc, key)
                    # Aggiungi un controllo per mostrare solo messaggi "validi"
                    if dec.isprintable():  # Verifica che il messaggio sia leggibile
                        print(f"La chiave corretta è: {key}")
                        print(f"Il messaggio decifrato è: {dec}")
                        # Uscire dai cicli una volta trovata la chiave corretta
                        break
                except Exception:
                    # Continua con la prossima combinazione se fallisce la decrittazione
                    continue
            else:
                continue
            break
        else:
            continue
        break

# Example usage
key = "ThisIsASecretKey"
plain_text = "Hello, World!"
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

