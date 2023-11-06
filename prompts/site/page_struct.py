
from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_site_struct_page_response(request: Request):

    # Токены
    max_role_tokens = 100  # количество токенов роль чата по умолчанию
    max_prompt_tokens = 500  # количество токенов пользовательского запроса
    max_response_tokens = 2000  # количество токенов ответа чата по умолчанию
    # Цена одного токена
    set_token_price = 1
    # Температура
    temperature = 0.7
    # Таймаут при нецензурном слове
    timeout = 5
    model_chat_gpt = 'gpt-3.5-turbo'  # Версия модели чата GPT
    max_length = 2000

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    input1 = data.get('input1', '')            # Регион
    input2 = data.get('input2', '')            # Телефон
    dropdown1 = str(data.get('dropdown1', ''))  # Цель страницы
    dropdown2 = str(data.get('dropdown2', ''))  # Целевая аудитория
    dropdown3 = str(data.get('dropdown3', ''))  # Призыв к действию
    dropdown4 = str(data.get('dropdown4', ''))  # Стиль
    textarea1 = data.get('textarea1', '')      # Структура страницы
    textarea2 = data.get('textarea2', '')      # Дополнительные данные

    # Выбор Модели чата GPT для обработки данных
    dropdown5 = str(data.get('dropdown5', ''))    # Уровень творчества
    if dropdown5.strip():
        temperature = round(int(dropdown5) / 10)
    dropdown6 = str(data.get('dropdown6', ''))    # Кол-во симоволв
    if dropdown6.strip():
        max_length = int(dropdown6)

    chat_role = (
        'Представь, что ты лучший копирайтер и SEO-специалист, '
        'лучший маркетолог'
    )

    # Пользовательский промт
    prompt = (
        'Разработай пожалуйста структуру посадочной страницы для сайта, '
        'которая будет SEO-оптимизирована. Вот основные данные:'
    )

    # Название страницы
    if dropdown1.strip():
        # Цель страницы
        prompt += f'. Цель страницы: {dropdown1}'
    if dropdown2.strip():
        # Целевая аудитория
        prompt += f'. Целевая аудитория: {dropdown2}'
    if dropdown3.strip():
        # Призыв к действию
        prompt += f'. Призыв к действию: {dropdown3}'
    if dropdown4.strip():
        # Стиль
        prompt += f'. Стиль: {dropdown4}'
    if input2.strip():
        prompt += f'. Телефон: {input2}' 				# Телефон
    if textarea1.strip():
        # Структура
        prompt += f'. Структура : [{textarea1}]'
    if textarea2.strip():
        # Дополнительные данные
        prompt += f'. Дополнительные данные: {textarea2}'
    if input1.strip():
        prompt += f'. Регион: {input1}'

    prompt += (
        '. Пожалуйста, создай для детальную структуру, заточенную под '
        'релевантные запросы пользователей, на основе предоставленной '
        'информации. Разбей страницу на смысловые блоки и укажи заголовки '
        f'H1 H2 H3. Не используй более {max_length} символов.'
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
