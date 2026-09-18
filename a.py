import hashlib
import os
import time

# ==========================================
# 1. BUILD THE HOUSE (Develop the App)
# ==========================================

class AppSecurity:
    def __init__(self):
        self.user_database = {}
        self.security_logs = []
        self.is_roof_waterproof = True
        self.wall_integrity = 100

    def install_locks_on_doors_and_windows(self, username, password):
        """Secure Authentication: Hash passwords using salt."""
        salt = os.urandom(16)
        # Hashing password with SHA-256 (Strong Lock)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        self.user_database[username] = {'salt': salt, 'hash': password_hash}
        print(f"[BUILD] Lock installed: Registered user '{username}' with hashed credentials.")

    def use_strong_materials_for_walls(self, user_input):
        """Write Secure Code: Sanitize input to prevent injection attacks."""
        # Clean dangerous characters
        sanitized_input = user_input.replace("<script>", "").replace("SELECT *", "")
        print(f"[BUILD] Strong Wall: Input sanitized -> '{sanitized_input}'")
        return sanitized_input

    def install_waterproof_roof(self, data):
        """Encrypt Data: Simple XOR encryption simulation for data at rest."""
        key = 0xAA
        encrypted = bytes([b ^ key for b in data.encode()])
        print(f"[BUILD] Waterproof Roof: Encrypted data stored -> {encrypted.hex()}")
        return encrypted


# ==========================================
# 2. INSPECT THE HOUSE (Test for Vulnerabilities)
# ==========================================

def test_if_locks_are_working(app, username, password_attempt):
    """Penetration Testing: Attempt login validation."""
    if username not in app.user_database:
        print("[INSPECT] Lock Test Failed: User does not exist.")
        return False
    
    user = app.user_database[username]
    attempt_hash = hashlib.pbkdf2_hmac('sha256', password_attempt.encode(), user['salt'], 100000)
    
    if attempt_hash == user['hash']:
        print("[INSPECT] Lock Test Passed: Authentication successful.")
        return True
    else:
        print("[INSPECT] Lock Test Alert: Invalid password attempt detected!")
        return False

def look_for_cracks_in_walls(app):
    """Check for Bugs/Vulnerabilities in code integrity."""
    if app.wall_integrity < 100:
        print(f"[INSPECT] Vulnerability Found: Wall integrity compromised at {app.wall_integrity}%!")
        return False
    print("[INSPECT] Code Review Passed: No structural cracks found.")
    return True

def test_roof_with_water(app):
    """Test Data Security: Verify encryption layer."""
    if app.is_roof_waterproof:
        print("[INSPECT] Data Security Passed: Encryption layer intact.")
        return True
    print("[INSPECT] Leak Detected: Data exposed in plaintext!")
    return False


# ==========================================
# 3. KEEP THE HOUSE SAFE (Monitoring & Maintenance)
# ==========================================

def install_security_cameras(app, event_details):
    """Monitor for Threats: Log runtime activities."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] CAMERA LOG: {event_details}"
    app.security_logs.append(log_entry)
    print(log_entry)

def repair_cracks_and_replace_broken_locks(app):
    """Patch Vulnerabilities: Restore security health."""
    print("[MAINTAIN] Patching vulnerabilities...")
    app.wall_integrity = 100
    app.is_roof_waterproof = True
    print("[MAINTAIN] System restored to 100% secure state.")


# ==========================================
# MAIN EXECUTION (Protect Application)
# ==========================================

def protect_application():
    print("--- 1. BUILDING THE HOUSE ---")
    app = AppSecurity()
    app.install_locks_on_doors_and_windows("admin", "SuperSecretPass123")
    app.use_strong_materials_for_walls("<script>alert('hack')</script>Hello")
    app.install_waterproof_roof("Sensitive User Data")
    print()

    print("--- 2. INSPECTING THE HOUSE ---")
    test_if_locks_are_working(app, "admin", "WrongPass")    # Failed login
    test_if_locks_are_working(app, "admin", "SuperSecretPass123") # Successful login
    look_for_cracks_in_walls(app)
    test_roof_with_water(app)
    print()

    print("--- 3. MAINTAINING HOUSE SECURITY ---")
    install_security_cameras(app, "Unauthorized access attempt blocked on port 443.")
    
    # Simulate a bug occurring over time
    app.wall_integrity = 75
    look_for_cracks_in_walls(app)
    
    # Patch the bug
    repair_cracks_and_replace_broken_locks(app)

# Run the complete cycle
if __name__ == "__main__":
    protect_application()