import hashlib
import math
import string


def calculate_entropy(password):
    """Estimate password entropy in bits."""

    if not password:
        return 0

    character_pool = 0

    if any(char.islower() for char in password):
        character_pool += 26

    if any(char.isupper() for char in password):
        character_pool += 26

    if any(char.isdigit() for char in password):
        character_pool += 10

    if any(char in string.punctuation for char in password):
        character_pool += len(string.punctuation)

    if character_pool == 0:
        return 0

    return len(password) * math.log2(character_pool)


def strength_label(entropy):
    """Convert entropy into a simple strength classification."""

    if entropy < 28:
        return "Very Weak"

    if entropy < 36:
        return "Weak"

    if entropy < 60:
        return "Moderate"

    if entropy < 80:
        return "Strong"

    return "Very Strong"


def hash_password(password):
    """Create a SHA-256 hash for demonstration purposes."""

    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def generate_salt():
    """Generate a cryptographically secure random salt."""

    import secrets

    return secrets.token_hex(16)


def hash_with_salt(password, salt):
    """Hash a password together with a salt."""

    combined = salt + password

    return hashlib.sha256(
        combined.encode("utf-8")
    ).hexdigest()


def analyze_password(password):
    """Return the main security characteristics of a password."""

    entropy = calculate_entropy(password)

    salt_one = generate_salt()
    salt_two = generate_salt()

    salted_hash_one = hash_with_salt(password, salt_one)
    salted_hash_two = hash_with_salt(password, salt_two)

    return {
        "length": len(password),
        "entropy": round(entropy, 2),
        "strength": strength_label(entropy),
        "sha256": hash_password(password),

        "salt_one": salt_one,
        "salted_hash_one": salted_hash_one,

        "salt_two": salt_two,
        "salted_hash_two": salted_hash_two,
    }