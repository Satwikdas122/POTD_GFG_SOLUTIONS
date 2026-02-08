"""Password strength evaluator with actionable suggestions."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Tuple


COMMON_PASSWORDS = {
    "password",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "111111",
    "letmein",
    "admin",
    "iloveyou",
}


@dataclass(frozen=True)
class StrengthResult:
    score: int
    level: str
    suggestions: List[str]


def _unique_char_ratio(password: str) -> float:
    if not password:
        return 0.0
    return len(set(password)) / len(password)


def _has_sequence(password: str) -> bool:
    sequences = ["abcdefghijklmnopqrstuvwxyz", "0123456789"]
    lowered = password.lower()
    for seq in sequences:
        for i in range(len(seq) - 3):
            chunk = seq[i : i + 4]
            if chunk in lowered or chunk[::-1] in lowered:
                return True
    return False


def _classify(password: str) -> Tuple[int, List[str]]:
    score = 0
    suggestions: List[str] = []

    length = len(password)
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15
        suggestions.append("Use at least 12 characters for better strength.")
    else:
        suggestions.append("Increase the password length to at least 12 characters.")

    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    variety = sum([has_lower, has_upper, has_digit, has_symbol])
    score += variety * 10

    if not has_lower:
        suggestions.append("Add lowercase letters.")
    if not has_upper:
        suggestions.append("Add uppercase letters.")
    if not has_digit:
        suggestions.append("Include numbers.")
    if not has_symbol:
        suggestions.append("Include special characters (e.g., !, #, $).")

    ratio = _unique_char_ratio(password)
    if ratio >= 0.7:
        score += 15
    else:
        suggestions.append("Avoid repeated characters or patterns.")

    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid common passwords or dictionary words.")
        score = max(score - 30, 0)

    if _has_sequence(password):
        suggestions.append("Avoid sequential characters like 1234 or abcd.")
        score = max(score - 10, 0)

    return min(score, 100), suggestions


def evaluate_password(password: str) -> StrengthResult:
    score, suggestions = _classify(password)
    if score >= 80:
        level = "Very Strong"
    elif score >= 60:
        level = "Strong"
    elif score >= 40:
        level = "Moderate"
    elif score >= 20:
        level = "Weak"
    else:
        level = "Very Weak"

    return StrengthResult(score=score, level=level, suggestions=suggestions)


def main() -> None:
    password = input("Enter a password to evaluate: ").strip()
    result = evaluate_password(password)
    print(f"Strength: {result.level} ({result.score}/100)")
    if result.suggestions:
        print("Suggestions:")
        for suggestion in result.suggestions:
            print(f"- {suggestion}")


if __name__ == "__main__":
    main()
