import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(4))
print('Essa é sua senha:{}'.format(password))