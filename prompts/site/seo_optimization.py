
from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_site_seo_optimization_response(request: Request):

    max_role_tokens = 50         # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 1950
    # Kоличество токенов ответа чата (ПО умолчанию) - Задается пользователем
    max_response_tokens = 1850
    set_token_price = 0.000002    # Цена одного токена
    temperature = 0.7             # Температура
    timeout = 5                   # Таймаут при нецензурном слове
    model_chat_gpt = 'gpt-3.5-turbo'  # Версия модели чата GPT

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    textarea1 = str(data.get('textarea1', ''))         # Текст для оптимизации
    textarea2 = str(data.get('textarea2', ''))         # Ключевые слова
    textarea3 = str(data.get('textarea3', ''))         # Минус слова
    textarea4 = str(data.get('textarea4', ''))         # Дополнительные данные
    # dropdown1 = data.get('dropdown1', '')      # Уровень творчества
    dropdown2 = float(data.get('dropdown2', ''))       # Кол-во символов

    # Выбор Модели чата GPT для обработки данных
    dropdown3 = str(data.get('dropdown3', ''))    # Версия модели чата GPT
    if dropdown3.strip():
        model_chat_gpt = dropdown3                  # Версия модели чата GPT

    if dropdown3.strip():
        # Преобразуем в число и делим на 10 Уровень творчества
        temperature = float(dropdown3) / 10
    # Переводим Символы в Токены Ограничения ответ чата
    max_response_tokens = round(dropdown2 / 1.5)
    # Кол-во. Символов для Промта в чат
    max_response_simvolov_promt = round(dropdown2 / 1.0)

    # Роль чата GPT
    chat_role = (
        'Представь ты лучший в мире копирайтер, веб разработчик и оптимизатор '
        'текста.'
    )

    # Пользовательский промт
    prompt = 'Оптимизируй пожалуйста текс'

    prompt += f': [{textarea1}]'     # Текст для оптимизации
    prompt += (
        ', для SEO, улучшения его видимости в поисковых системах и '
        'привлечения органического трафика. Сохраните текущую структуру, '
        'абзацы и смысл текста. Пожалуйста, внесите изменения, чтобы сделать '
        'текст более SEO-дружелюбным и добавьте ключевые слова'
    )
    if textarea2.strip():
        # Ключевые слова
        prompt += f'. Добавь в этот текст эти ключевые слова: [{textarea2}]'
    if textarea3.strip():
        # Минус слова
        prompt += f'. Не используй эти минус слова: [{textarea3}]'
    if textarea4.strip():
        prompt += f'. Учти: {textarea4}'  # Дополнительные данные

    prompt += f'. Напиши статью до {max_response_simvolov_promt} символов.'

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
