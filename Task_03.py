import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[@$!%*?&]', password) is not None
    
    # Strength levels
    strength = 0
    if length_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_criteria:
        strength += 1
    
    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character (@$!%*?&).")
    
    return strength, feedback

def main():
    password = input("Enter a password to check its strength: ")
    strength, feedback = password_strength(password)
    
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    
    print(f"Password Strength: {strength_levels[strength]}")
    
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
