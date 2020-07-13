# All letters required for the ROT-13
alphabet_rot_13 = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a','o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}
msg_encrypt = []
msg_decrypt = []

# Function to encrypt a message without symbols or numbers
def Encrypt(msg):
    for c in range(0, len(msg)):
        if msg[c] == ' ':
            msg_encrypt.append(' ')
            continue
        msg_letter = msg[c]
        msg_encrypt.append(alphabet_rot_13[msg_letter])
        msg_encrypted = ''.join(msg_encrypt)
    print(msg_encrypted)

# Function to decrypt a message without symbols or numbers
def Decrypt(msg):
    for c in range(0, len(msg)):
        if msg[c] == ' ':
            msg_decrypt.append(' ')
            continue
        msg_letter = msg[c]
        msg_decrypt.append(alphabet_rot_13[msg_letter])
        msg_decrypted = ''.join(msg_decrypt)
    print(msg_decrypted)

# User's choice
option = 0
while option != 1 and option != 2:
    option = int(input('''Choose only one:
[1] Encrypt
[2] Decrypt
Your option: '''))
    if option != 1 and option != 2:
        print('[ \033[0;31mERROR\033[0;0m ] Invalid number, try again.')
    print('-=+=-'*5)

# Calling the necessary functions
if option == 1:
    message = str(input('Enter the message to be encrypted: '))
    msg = message.lower()
    Encrypt(msg)
else:
    message = str(input('Enter the message to be decrypted: '))
    msg = message.lower()
    Decrypt(msg)