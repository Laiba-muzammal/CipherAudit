from flask import Blueprint, render_template, request,abort
import re, math, hashlib, requests

checker = Blueprint("checker", __name__, template_folder="templates", static_folder="static")

# Check if password has been pwned
def check_pwned_password(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    for line in res.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return True, count
    return False, 0

# Entropy calculator
def entropy_checker(password):
    charset_size = 0
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"\d", password):
        charset_size += 10
    if re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:'\",.<>/?`~]", password):
        charset_size += 33

    if charset_size == 0:
        return 0
    return round(len(password) * math.log2(charset_size), 2)

# Time to crack estimation
def estimate_crack_time(entropy):
    seconds = (2 ** entropy) / 1_000
    if seconds < 60:
        return "⚡ Instantly"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} hours"
    else:
        return f"{int(seconds / 86400)} days"

# File-based pattern checker
def checker_from_files(filename, password):
    filepath = f"patterns/{filename}"
    with open(filepath, encoding="utf-8") as file:
        lines = [line.strip() for line in file]
        for pattern in lines:
            if pattern == password.lower():
                return f"⚠️ Contains weak pattern: {filename}"
    return None

# Main route
@checker.route("/", methods=["GET", "POST"])
def pass_checker():
    if request.method == "POST":
        password = request.form.get("password")
        if not password:
            abort("400", "Password is required")
        result = []
        score = 0

        # Length check
        if len(password) < 8:
            result.append("❌ Too short password (minimum 8 characters)")
        else:
            result.append("✅ Good length")
            score += 1

        # Uppercase
        if re.search(r"[A-Z]", password):
            result.append("🔠 Contains uppercase letter")
            score += 1
        else:
            result.append("❌ Must contain at least one uppercase letter")

        # Lowercase
        if re.search(r"[a-z]", password):
            result.append("🔡 Contains lowercase letter")
            score += 1
        else:
            result.append("❌ Must contain at least one lowercase letter")

        # Digits
        if re.search(r"\d", password):
            result.append("🔢 Contains digit")
            score += 1
        else:
            result.append("❌ Must contain at least one digit")

        # Special Characters
        if re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:'\",.<>/?`~]", password):
            result.append("💥 Contains special character")
            score += 1
        else:
            result.append("❌ Must contain at least one special character")

        # Check patterns from files
        pattern_match_found = False  # 🟡 flag to track if any match found

        for filename in [
            "sequence.txt",
            "repetition.txt",
            "keyboard_patterns.txt",
            "common_password.txt",
            "dictionary.txt"
        ]:
            pattern_result = checker_from_files(filename, password)
            if pattern_result:
                result.append(pattern_result)
                pattern_match_found = True

        # If no match found in any file, add score once
        if not pattern_match_found:
            score += 1


        # Entropy and cracking time
        entropy = entropy_checker(password)
        time_crack = estimate_crack_time(entropy)

        result.append(f"🧠 Entropy: {entropy} bits")
        result.append(f"⏱️ Estimated Crack Time: {time_crack}")

        # Pwned check
        pwned, count = check_pwned_password(password)
        if pwned:
            result.append(f"⚠️ Password has been pwned {count} times")
        else:
            result.append("✅ Password hasn't been pwned yet")
            score+=1

        # Final score
        if score >= 7:
            result.append(f"🔒 Strong password with strength: {score}/8")
        elif score >= 5:
            result.append(f"🟡 Medium password with strength: {score}/8")
        else:
            result.append(f"🔓 Weak password with strength: {score}/8")

        return render_template("response.html", results=result , password=password)

    return render_template("home.html")


@checker.route("/response", methods=["GET","POST"])
def response():
    return render_template("response.html")