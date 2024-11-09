import hashlib
import time
import json

# List of common passwords (you can expand this list)
common_passwords = [
    "123456", "password", "123456789", "12345", "1234", "qwerty", "123123", 
    "abc123", "password1", "123qwe", "admin", "letmein", "welcome", "monkey", 
    "dragon", "sunshine", "iloveyou", "trustno1", "123321", "qwertyuiop"
]

# List of hash algorithms
hash_algorithms = [
    hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512,
    hashlib.sha224, hashlib.blake2b, hashlib.blake2s, hashlib.sha3_256,
    hashlib.sha3_512, hashlib.shake_128
]

# Time tracking dictionary to store times for each password and algorithm
time_tracking = {}

# Function to hash a password with multiple algorithms and track time
def hash_passwords(passwords, algorithms):
    for password in passwords:
        password_hashes = {}
        total_time = 0  # Initialize total time for the password
        for algo in algorithms:
            start_time = time.time()  # Record start time
            
            # Handle specific cases for algorithms like shake_128
            if algo == hashlib.shake_128:
                # Shake algorithms require an output length to be defined (e.g., 32 bytes)
                hashed = algo(password.encode()).hexdigest(64)  # Here we specify the length of the hash
            else:
                hashed = algo(password.encode()).hexdigest()

            end_time = time.time()  # Record end time
            time_taken = (end_time - start_time) * 1000  # Time in milliseconds
            password_hashes[algo.__name__] = {"hash": hashed, "time_taken_ms": time_taken}
            total_time += time_taken  # Add time for this algorithm to total time
        
        password_hashes["total_time_ms"] = total_time  # Store total time for the password
        time_tracking[password] = password_hashes

# Hash the common passwords and track time
hash_passwords(common_passwords, hash_algorithms)

# Save the time tracking data into a JSON file
with open("hashed_passwords_with_time.json", "w") as json_file:
    json.dump(time_tracking, json_file, indent=4)
