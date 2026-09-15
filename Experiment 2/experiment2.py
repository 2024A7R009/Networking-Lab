import hashlib
import hmac


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("Error: File not found.")
        return None


filename = input("Enter the file path: ")

print("\nCalculating original hash...")
old_hash = calculate_hash(filename)

if old_hash is not None:
    print("Hash before modification:")
    print(old_hash)

    input("\nModify the file, save it, and press Enter...")

    new_hash = calculate_hash(filename)

    print("\nHash after modification:")
    print(new_hash)

    if hmac.compare_digest(old_hash, new_hash):
        print("\nINTEGRITY CHECK: PASSED")
        print("No changes were detected.")
    else:
        print("\nINTEGRITY CHECK: FAILED")
        print("The file has been modified.")
