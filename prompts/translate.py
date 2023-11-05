import json

from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_translate_response(request: Request):

    max_role_tokens = 50  # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 2000
    # Kоличество токенов ответа чата (ПО умолчанию) - Задается пользователем
    max_response_tokens = 2000
    set_token_price = 0.000002    						# Цена одного токена
    temperature = 0.7             						# Температура
    timeout = 5                   						# Таймаут при нецензурном слове
    model_chat_gpt = 'gpt-3.5-turbo'  # Версия модели чата GPT

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    textarea1 = str(data.get('textarea1', ''))      		# Текст для рерайта
    textarea2 = str(data.get('textarea2', ''))      		# Дополнительные данные
    dropdown1 = str(data.get('dropdown1', ''))      		# Стиль
    dropdown2 = data.get('dropdown2', '')    		# Уровень творчества
    dropdown3 = float(data.get('dropdown3', ''))    		# Кол-во символов

    if dropdown2.strip():  # Hе пустое ли значение Уровень творчества
        # Преобразуем в число и делим на 10 Уровень творчества
        temperature = float(dropdown2) / 10

    # Переводим Символы в Токены Ограничения ответ чата
    max_response_tokens = round(dropdown3 / 1.5)
    # Кол-во. Символов для Промта в чат
    max_length = round(dropdown3 / 1.2)

    # Роль чата GPT
    chat_role = 'Представь ты лучший в мире рерайтер.'

    # Пользовательский промт
    prompt = (
        'Пожалуйста перепиши этот текст, сохраняя при этом смысл и основную '
        'информацию, чтобы текст стал уникальным на 80%. Перепишите '
        'предложения, используя синонимы и другой лексический материал. '
        'Перераспределите фразы и слова в предложениях, измените порядок слов.'
        ' Заменяйте ключевые слова и фразы на их синонимы или близкие по '
        'значению. При этом обязательно следите за тем, чтобы смысл оставался'
        ' неизменным. Внесите дополнительные сведения. Перепишите абзацы в '
        'другом порядке или даже измените структуру текста, чтобы придать ему '
        'новый логический ход. Если текст содержит специфическую терминологию,'
        ' попробуйте заменить ее на аналогичные понятия или термины. '
        'Вот исходный текст:'
    )

    prompt += f' [{textarea1}]'            	# Текст для перевода
    if textarea2.strip():
        prompt += f'. {textarea2}'      		# Дополнительные данные
    if dropdown1.strip():
        # На какой язык перевести
        prompt += f'. Пиши в {dropdown1} стиле'
    # Кол-во. Символов для Промта в чат
    prompt += (
        f'. Напиши текст {max_length} символов. Пиши хорошо, '
        f'старайся!!!'
    )

    # Вызов обработчика GPT3 и возврат результата
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
