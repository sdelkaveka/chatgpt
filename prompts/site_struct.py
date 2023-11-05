from rest_framework.request import Request

from core.gpt import handle_gpt3
import json


async def get_site_struct_response(request: Request):

    # Токены
    max_role_tokens = 500  # количество токенов роль чата по умолчанию
    max_prompt_tokens = 500  # количество токенов пользовательского запроса
    max_response_tokens = 800  # количество токенов ответа чата по умолчанию
    # Цена одного токена
    set_token_price = 1
    # Температура
    temperature = 0.7
    # Таймаут при нецензурном слове
    timeout = 5
    model_chat_gpt = 'gpt-3.5-turbo'  # Версия модели чата GPT

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    textarea1 = data.get('textarea1', '')  # Все направления вашей деятельности
    input1 = data.get('input1', '')       # Регион
    textarea2 = data.get('textarea2', '')  # Какие направления исключить
    textarea3 = data.get('textarea3', '')  # Дополнительные данные

    # Выбор Модели чата GPT для обработки данных
    dropdown1 = str(data.get('dropdown1', ''))    # Версия модели чата GPT
    if dropdown1.strip():
        model_chat_gpt = dropdown1                  # Версия модели чата GPT

    # temperature = round(temperature/10, 1)
    # Я ЭТУ СТРОЧКУ ЗАКОМЕНТИРОВАЛ НАПИСАЛ В ТГ ТЕБЕ ПОЧЕМУ 0,7/10 ЗАЧЕМ?

    # Роль чата GPT
    chat_role = (
        'Представь ты лучший вебмастер, сео специалист и крутой разработчик '
        'сайтов. Мне нужно сделать сайт, каждая страница должна быть '
        'посадочной, seo оптимизированной и название страницы должно '
        'максимально соответствовать популярным в поисковых системах '
        'запросам в этой нише бизнеса.'
    )

    # Пользовательский промт
    prompt = ''
    # Все направления вашей деятельности
    prompt += f'Список направлений чем я занимаюсь: "{textarea1}"'
    if input1.strip():
        prompt += f'. Регион: {input1}'   # Регион
    if textarea2.strip():
        # Какие направления исключить
        prompt += f'. Исключи эти направления: {textarea2}'
    if textarea3.strip():
        # Дополнительные данные
        prompt += f'. Дополнительные данные: {textarea3}'

    prompt += (
        '. Составь пожалуйста максимально расширенный список названий всех '
        'страниц для моего сайта. Структурируй список со вложенными '
        'страницами. И добавь еще страницы необходимые для сайта. Пономеруй '
        'каждую страницу и подстраницу.'
    )

    return await handle_gpt3(
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
