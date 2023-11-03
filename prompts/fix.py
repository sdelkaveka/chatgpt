from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_fix_response(request: Request):

    max_role_tokens = 100  # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 2000
    # Kоличество токенов ответа чата (ПО умолчанию) - Задается пользователем
    max_response_tokens = 2000
    set_token_price = 0.000002    						# Цена одного токена
    temperature = 0.7             						# Температура
    timeout = 5                   						# Таймаут при нецензурном слове
    model_chat_gpt = "gpt-3.5-turbo"  # Версия модели чата GPT

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем "Переменные" из запроса от frontend
    textarea1 = str(data.get('textarea1', ''))      		# Текст для рерайта
    textarea2 = str(data.get('textarea2', ''))      		# Дополнительные данные
    dropdown1 = str(data.get('dropdown1', ''))      		# Стиль
    dropdown2 = float(data.get('dropdown2', ''))    		# Уровень творчества

    # Выбор Модели чата GPT для обработки данных
    dropdown3 = str(data.get('dropdown3', ''))    # Версия модели чата GPT
    if dropdown3.strip():
        model_chat_gpt = dropdown3                  # Версия модели чата GPT

    # Делаем температуру меньше еденицы
    temperature = round(dropdown2 / 10, 1)

    # Роль чата GPT
    chat_role = (
        'Представь ты автор книги '
        '"ПИШИ, СОКРАЩАЙ: Как создавать сильный текст" написанная Максимом '
        'Ильяховым и Людмилой Сарычевой.'
    )

    # Пользовательский промт
    prompt = (
        'Используй, пожалуйста советы книги "ПИШИ, СОКРАЩАЙ: Как создавать '
        'сильный текст" и как рекомендуется в этой книге отредактируй мой '
        'текст, исправлять ошибки, улучши структуру и стиль текста, а также '
        'сделай текст более ясным и читабельным'
    )

    # Текст для перевода
    prompt += f". Вот текст: [{textarea1}]"
    if textarea2.strip():
        # Дополнительные данные
        prompt += f". {textarea2}"
    if dropdown1.strip():
        prompt += f". Пиши в {dropdown1} стиле"    # Стиль
    prompt += (
        '. В ответе не упоминай о книге "ПИШИ, СОКРАЩАЙ" Пиши пожалуйста '
        'только обработанный текст без комментариев. Спасибо!'
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
