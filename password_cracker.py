import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

def hash_password_with_salt(password, salt):
    hash1 = hashlib.sha1((salt + password).encode()).hexdigest()
    hash2 = hashlib.sha1((password + salt).encode()).hexdigest()
    return hash1, hash2

def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def crack_sha1_hash(hash_to_crack, use_salts=False):
    passwords = load_file('top-10000-passwords.txt')

    if use_salts:
        salts = load_file('known-salts.txt')
        for password in passwords:
            for salt in salts:
                hash1, hash2 = hash_password_with_salt(password, salt)
                if hash_to_crack == hash1 or hash_to_crack == hash2:
                    return password
    else:
        for password in passwords:
            hash_val = hash_password(password)
            if hash_val == hash_to_crack:
                return password

    return "PASSWORD NOT IN DATABASE"
