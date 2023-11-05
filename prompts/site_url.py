import json

from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_site_url_response(request: Request):

    max_role_tokens = 100          # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 1000
    max_response_tokens = 1000   # Kоличество токенов ответа чата по умолчанию
    set_token_price = 0.000002        # Цена одного токена
    temperature = 0.7                 # Температура
    timeout = 5                       # Таймаут при нецензурном слове
    model_chat_gpt = 'gpt-3.5-turbo'  # Версия модели чата GPT

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    # Название всех страниц, список
    textarea1 = str(data.get('textarea1', ''))
    input1 = str(data.get('input1', ''))          # Домен или раздел
    input2 = str(data.get('input2', ''))          # Регион
    # Слова: Латиницей, Английские
    dropdown1 = str(data.get('dropdown1', ''))
    textarea2 = str(data.get('textarea2', ''))    # Дополнительные данные
    dropdown2 = data.get('dropdown2', '')  # Уровень творчества

    # Выбор Модели чата GPT для обработки данных
    dropdown3 = str(data.get('dropdown3', ''))    # Версия модели чата GPT
    if dropdown3.strip():
        model_chat_gpt = dropdown3                  # Версия модели чата GPT

    if dropdown2.strip():
        # Преобразуем в число и делим на 10 Уровень творчества
        temperature = float(dropdown2) / 10

    # Роль чата GPT
    chat_role = (
        'Представь ты лучший в мире веб мастер. Напиши пожалуйста URL для '
        'страниц сайта.'
    )

    # Пользовательский промт
    prompt = (
        'Напиши пожалуйста по всем нормам и правилам веб разработчиков URL '
        'для страниц сайта'
    )

    # Название всех страниц, список
    prompt += f'. Вот названия страниц: {textarea1}'

    if input1.strip():
        # Домен или раздел
        prompt += f'. В начале url напиши {input1}'

    if input2.strip():
        # Регион
        prompt += f'. Это добавь к конце url: {input2} в конце строки'

    if dropdown1.strip():
        # Слова: Латиницей, Английские
        prompt += f'. {dropdown1}'

    if textarea2.strip():
        # Дополнительные данные
        prompt += f'. {textarea2}'

    prompt += (
        '. Пиши без пояснений. Разделяй слова по смыслу нижним подчеркиванием.'
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
