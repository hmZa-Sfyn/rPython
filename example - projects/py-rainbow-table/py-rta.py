import hashlib
import json

# List of common passwords (you can expand this list up to 12,000 passwords or more)
common_passwords = [
    "123456", "password", "123456789", "12345", "1234", "qwerty", "abc123", "password1", "123123", "welcome",
    "letmein", "monkey", "123321", "qwerty123", "123qwe", "dragon", "sunshine", "iloveyou", "princess", "football"
]

# List of hash algorithms to use
hash_algorithms = [
    'sha256', 'sha1', 'md5', 'sha512', 'sha384', 'sha224', 'blake2b', 'blake2s', 'ripemd160'
]

# Function to generate the hash of a password using a given algorithm
def generate_hash(password, algorithm):
    hash_object = hashlib.new(algorithm)
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()

# Dictionary to store password and their hash results for each algorithm
password_hashes = {}

# Generate hashes for each password and algorithm
for password in common_passwords:
    password_hashes[password] = {}
    for algorithm in hash_algorithms:
        password_hashes[password][algorithm] = generate_hash(password, algorithm)

# Save the results in a .json file
with open('password_hashes_top_10.json', 'w') as json_file:
    json.dump(password_hashes, json_file, indent=4)

print("Password hashes have been saved to 'password_hashes_top_10.json'")
