import random
import string

def generar_password():
    longitud=32
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    contraseña += [random.choice(caracteres) for _ in range(longitud - len(contraseña))]
    random.shuffle(contraseña)
    return ''.join(contraseña)