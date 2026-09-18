import os
from cryptography.fernet import Fernet

def restore_files(target_dir, key_file_path="decryption_key.txt"):
    """Reads the generated key and decrypts files altered by Fernet symmetric encryption."""
    if not os.path.exists(key_file_path):
        print(f"[!] Error: Key file '{key_file_path}' not found.")
        return

    with open(key_file_path, "rb") as k_file:
        key = k_file.read()

    cipher = Fernet(key)
    target_extensions = ('.txt', '.pdf', '.docx', '.jpg')

    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(target_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'rb') as f:
                        encrypted_data = f.read()

                    decrypted_data = cipher.decrypt(encrypted_data)

                    with open(file_path, 'wb') as f:
                        f.write(decrypted_data)

                    print(f"[+] Restored: {file_path}")
                except Exception as e:
                    print(f"[!] Failed to decrypt {file_path}: {e}")

if __name__ == "__main__":
    # Point this to the target folder containing encrypted test files
    demo_dir = "./demo_vault"
    restore_files(demo_dir)