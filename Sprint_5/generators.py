"""Генераторы тестовых учётных данных."""

import secrets
import string
import uuid


def generate_email(cohort: int = 5, domain: str = "yandex.ru") -> str:
    """Создать уникальный email в формате имени, фамилии, когорты и трёх цифр."""
    unique_part = uuid.uuid4().hex[:8]
    three_digits = f"{secrets.randbelow(1000):03d}"
    return f"qa_student{unique_part}_{cohort}_{three_digits}@{domain}"


def generate_password(length: int = 10) -> str:
    """Создать пароль не короче шести символов с буквами и цифрами."""
    if length < 6:
        raise ValueError("Длина пароля должна быть не меньше шести символов")

    tail_alphabet = string.ascii_letters + string.digits
    required_characters = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    tail = [secrets.choice(tail_alphabet) for _ in range(length - 3)]
    password_characters = required_characters + tail
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def generate_user() -> dict[str, str]:
    """Создать полный набор данных нового пользователя."""
    return {
        "name": "Test Student",
        "email": generate_email(),
        "password": generate_password(),
    }
