import hashlib
import hmac
import secrets


secret_key = b"cyber123"


def generate_response(nonce):
    return hmac.new(
        secret_key,
        nonce.encode(),
        hashlib.sha256
    ).hexdigest()


# Normal Authentication
nonce = secrets.token_hex(8)

print("Challenge (Nonce):", nonce)

response = generate_response(nonce)
print("Client Response:", response)

expected = generate_response(nonce)

if hmac.compare_digest(response, expected):
    print("Authentication Successful")
else:
    print("Authentication Failed")


# Replay Attack Test
print("\n--- Replay Attack Test ---")

old_response = response
new_nonce = secrets.token_hex(8)

print("New Challenge:", new_nonce)
print("Replayed Old Response:", old_response)

expected_new = generate_response(new_nonce)

if hmac.compare_digest(old_response, expected_new):
    print("Replay Attack Not Detected")
else:
    print("Replay Attack Detected")
