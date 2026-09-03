def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1

    lines = [
        "Password requirements:",
        f"8+ characters       : {'Yes' if len(password) >= 8 else 'No'}",
        f"Uppercase letter    : {'Yes' if any(char.isupper() for char in password) else 'No'}",
        f"Lowercase letter    : {'Yes' if any(char.islower() for char in password) else 'No'}",
        f"Number              : {'Yes' if any(char.isdigit() for char in password) else 'No'}",
        f"Special character   : {'Yes' if any(not char.isalnum() for char in password) else 'No'}",
        "",
        "Password strength:"
    ]

    if score <= 2:
        lines.append("WEAK")
    elif score <= 4:
        lines.append("MEDIUM")
    else:
        lines.append("STRONG")

    return "\n".join(lines)