from rest_framework.request import Request

from core.gpt import handle_gpt3


async def get_text_struct_response(request: Request):

    max_role_tokens = 50         # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 1300
    max_response_tokens = 2000    # Kоличество токенов ответа чата по умолчанию
    set_token_price = 0.000002    # Цена одного токена
    temperature = 0.7             # Температура
    timeout = 5                   # Таймаут при нецензурном слове
    model_chat_gpt = 'gpt-3.5-turbo'  # Версия модели чата GPT

    # Получаем JSON-данные из запроса от frontend
    data = request.json

    # Извлекаем 'Переменные' из запроса от frontend
    textarea1 = data.get('textarea1', '')         		# Структура страницы
    textarea2 = data.get('textarea2', '')         		# Ключевые слова
    dropdown1 = str(data.get('dropdown1', ''))    		# Тип страницы
    dropdown2 = str(data.get('dropdown2', ''))    		# Целевая аудитория
    dropdown3 = str(data.get('dropdown3', ''))    		# Призвы к действию
    dropdown4 = str(data.get('dropdown4', ''))    		# Стиль
    input1 = data.get('input1', '')               		# Регион
    input2 = data.get('input2', '')               		# Телефон
    textarea3 = data.get('textarea3', '')         		# Дополнительные данные
    dropdown5 = data.get('dropdown5', '')  		# Уровень творчества
    # Кол-во Символов на Отчет чата.
    dropdown6 = float(data.get('dropdown6', ''))

    # Выбор Модели чата GPT для обработки данных
    dropdown7 = str(data.get('dropdown7', ''))    # Версия модели чата GPT
    if dropdown7.strip():
        model_chat_gpt = dropdown7                  # Версия модели чата GPT

    if dropdown5.strip():
        # Преобразуем в число и делим на 10 Уровень творчества
        temperature = float(dropdown5) / 10
    # Переводим Символы в Токены Ограничения ответ чата
    max_response_tokens = round(dropdown6 / 1.1)
    # Кол-во. Символов для Промта в чат
    max_length = round(dropdown6 / 1.35)

    # Роль чата GPT
    chat_role = (
        'Представь ты лучший копирайтер и веб разработчик сайтов в мире.'
    )

    # Пользовательский промт
    prompt = (
        'Напиши пожалуйста текст для страницы сайта. Строго придерживайся '
        'этой структуры страницы: '
    )

    prompt += f' [{textarea1}].' 	# Структура страницы
    if textarea2.strip():
        # Ключевые слова
        prompt += (
            f'. В тексте страницы должны быть ключевые слова: [{textarea2}]'
        )
    if dropdown1.strip():
        # Тип страницы
        prompt += f'. Тип страницы сайта: {dropdown1}'
    if dropdown2.strip():
        # Целевая аудитория
        prompt += f'. Целевая аудитория: {dropdown2}'
    if dropdown3.strip():
        # Призвы к действию
        prompt += f'. Призвы к действию: {dropdown3}'
    if dropdown4.strip():
        # Стиль
        prompt += f'. Стиль повествования: {dropdown4}'
    if input1.strip():
        prompt += f'. Регион: {input1}'                				# Регион
    if input2.strip():
        # Телефон
        prompt += f'. Телефон: {input2}'
    if textarea3.strip():
        # Дополнительные данные
        prompt += f'. {textarea3}'

    prompt += (
        f' Основная задача получить такой текст чтобы страница сайта как '
        f'можно скорее появилось на первой странице выдачи поисковую систему '
        f'и Как можно дольше там удерживалась. Напиши текст до {max_length} '
        f'символов. Пиши чистый текст, не делай разметку тегами.'
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
