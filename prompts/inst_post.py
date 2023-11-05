import json

from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_inst_post_response(request: Request):
    # Название сервиса

    max_role_tokens = 100     # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 500
    max_response_tokens = 500     # Kоличество токенов ответа чата по умолчанию
    set_token_price = 0.000002    # Цена одного токена
    temperature = 0.7             # Температура
    timeout = 5                   # Таймаут при нецензурном слове

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    textarea1 = data.get('textarea1', '')         # Тема поста
    textarea2 = data.get('textarea2', '')         # Краткое описание
    dropdown1 = data.get('dropdown1', '')         # Стиль
    dropdown2 = data.get('dropdown2', '')         # Призывы к действию
    input1 = data.get('input1', '')               # Регион
    input2 = data.get('input2', '')               # Телефон
    input3 = data.get('input3', '')               # Ссылка
    dropdown3 = data.get('dropdown3', '')         # Смайлики
    dropdown4 = data.get('dropdown4', '')  # Уровень творчества/температура
    # Кол-во Символов на Отчет чата.
    dropdown5 = float(data.get('dropdown5', ''))

    if dropdown4.strip():
        # Преобразуем в число и делим на 10 Уровень творчества
        temperature = float(dropdown4) / 10
    # Переводим Символы в Токены Ограничения ответ чата
    max_response_tokens = round(dropdown5 / 1.1)
    # Кол-во. Символов для Промта в чат
    max_length = round(dropdown5 / 2.75)

    # Роль чата GPT
    chat_role = (
        'Представь ты лучший копирайтер в мире и лучший SMM-менеджер в '
        'социальной сети Instagram. Напиши пожалуйста качественный '
        'привлекательные тексты для поста. Пиши с абзацами.'
    )

    prompt = ''
    prompt += f'Тема поста: [{textarea1}.] Сделай из этого мощьный заголовок '
    if textarea2.strip():
        # Краткое описание
        prompt += f'. Краткое описание поста: {textarea2}'
    if dropdown1.strip():
        # Стиль
        prompt += f'. Используй: {dropdown1}'
    if dropdown2.strip():
        # Призывы к действию
        prompt += f'. В тексте должен быть призыв к действию: {dropdown2}'
    if input1.strip():
        # Регион
        prompt += f'. {input1}'
    if input2.strip():
        # Телефон
        prompt += f'. Телефон напиши в самом верху, второй строчкой: {input2}'
    if input3.strip():
        # Хэштег
        prompt += f'. Используй хэштеги: {input3}'
    if dropdown3.strip():
        # Смайлики
        prompt += f'. Смайлики и эмодзи {dropdown3}'

    prompt += (
        f'. Напиши текст не более: {max_length} символов. Пиши пост креативно '
        f'и разнообразно. Применяй хэштеги релевантные содержимому поста, до '
        f'5 шт.'
    )
    return handle_gpt3(
        chat_role=chat_role,
        prompt=prompt,
        timeout=timeout,
        temperature=temperature,
        set_token_price=set_token_price,
        max_role_tokens=max_role_tokens,
        max_prompt_tokens=max_prompt_tokens,
        max_response_tokens=max_response_tokens,
    )
