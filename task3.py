import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Rating
    if strength == 5:
        rating = "Very Strong 💪"
    elif strength >= 4:
        rating = "Strong ✅"
    elif strength >= 3:
        rating = "Moderate ⚠️"
    else:
        rating = "Weak ❌"

    return rating, feedback

# Example usage
password = input("Enter your password to check: ")
rating, suggestions = check_password_strength(password)

print(f"\nPassword Strength: {rating}")
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
