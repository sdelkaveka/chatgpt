import json

from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_site_keywords_response(request: Request):
    # Название сервиса

    max_role_tokens = 100          # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 500
    max_response_tokens = 2000   # Kоличество токенов ответа чата по умолчанию
    set_token_price = 0.000002        # Цена одного токена
    temperature = 0.7                 # Температура
    timeout = 5                       # Таймаут при нецензурном слове
    model_chat_gpt = 'gpt-3.5-turbo'  # Версия модели чата GPT

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    input1 = str(data.get('input1', ''))          # Название страницы сайта
    input2 = str(data.get('input2', ''))          # Регион
    textarea1 = str(data.get('textarea1', ''))    # Ключевые слова
    textarea2 = str(data.get('textarea2', ''))    # Минус слова

    # Выбор Модели чата GPT для обработки данных
    dropdown1 = str(data.get('dropdown1', ''))    # Версия модели чата GPT
    if dropdown1.strip():
        model_chat_gpt = dropdown1                  # Версия модели чата GPT

    # Роль чата GPT
    chat_role = (
        'Представь ты лучший копирайтер и SEO специалист, подбери пожалуйста '
        'ключевые слова для страницы сайта.'
    )

    # Пользовательский промт
    prompt = ''

    # Название страницы сайта
    prompt += f' Название страницы сайта: "{input1}"'
    if input2.strip():
        # Регион
        prompt += f'. Напиши слова без региона и с регионм: {input2}'
    if textarea1.strip():
        # Ключевые слова
        prompt += (
            f'. Сначала напиши максимально расширенный твой список, '
            f'потом добавь мои слова: [{textarea1}] и размножь мои слова и '
            f'подбери похожие'
        )
    if textarea2.strip():
        # Минус слова
        prompt += f'. Не учитывай такие ключевые слова: [{textarea2}]'

    prompt += (
        '. Напиши максимально расширенный список, без пояснений. Каждое '
        'ключевое слово должно быть разделено символом переноса строки.'
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
        model_chat_gpt=model_chat_gpt,
    )
