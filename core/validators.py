import re
from time import sleep

from rest_framework.exceptions import ValidationError
from .profanity_words import words


def validate_text(text: str) -> bool:
    text = text.lower()

    pattern = r'\b(?:' + '|'.join(
        re.escape(word) for word in words
    ) + r')\b'

    return bool(re.search(pattern, text))


def validate_prompt(promt: str, timeout=0):
    # Если поле 'user_prompt_modification' отсутствует в данных запроса
    if not promt:
        raise ValidationError('Отсутствует промпт!')

    # Определяем есть ли нецензурные выражения
    if validate_text(promt):
        sleep(timeout)  # Делаем таймауt
        # Возвращаем на frontend ответ с сообщением
        raise ValidationError('Обнаружено нецензурное выражение!')
