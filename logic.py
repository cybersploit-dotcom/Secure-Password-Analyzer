import random
import string

def check_strength(password):
    """Analyzes password strength based on length and complexity."""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it longer (8+ chars).")
        
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*" for c in password): score += 1
    
    if score == 5:
        return "STRONG", feedback
    elif score >= 3:
        return "MEDIUM", feedback
    else:
        return "WEAK", feedback

def generate_password(length=12):
    """Generates a random secure password."""
    if length < 8:
        length = 8
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def save_to_file(password, filename="history.txt"):
    """Saves the password to a file (Simulating a Vault)."""
    with open(filename, "a") as f:
        # In a real app, we would encrypt this. 
        # For this project, we append it to show File I/O skills.
        f.write(f"{password}\n")