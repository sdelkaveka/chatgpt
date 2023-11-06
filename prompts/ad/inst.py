
from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_inst_response(request: Request):
    # Название сервиса

    max_role_tokens = 70          # Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 400
    max_response_tokens = 500     # Kоличество токенов ответа чата по умолчанию
    set_token_price = 0.000002    # Цена одного токена
    temperature = 0.7             # Температура
    timeout = 5                   # Таймаут при нецензурном слове

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    input1 = data.get('input1', '')                # Кто я
    input2 = data.get('input2', '')                # Что делаю
    input3 = data.get('input3', '')                # Регион
    input4 = data.get('input4', '')                # Телефон
    input5 = data.get('input5', '')                # Ссылка
    textarea1 = data.get('textarea1', '')          # Дополнительные данные
    dropdown1 = str(data.get('dropdown1', ''))     # Стиль
    dropdown2 = str(data.get('dropdown2', ''))     # Призывы к действию
    dropdown3 = data.get('dropdown3', '')          # Уровень творчества
    # Кол-во Символов на Отчет чата.
    dropdown4 = int(data.get('dropdown4', ''))

    if dropdown3.strip():  # Hе пустое ли значение Уровень творчества
        temperature = float(dropdown3) / 10
    # Переводим Символы в Токены Ограничения ответ чата
    max_response_tokens = round(dropdown4 / 1.1)
    # Кол-во. Символов для Промта в чат
    max_length = round(dropdown4 / 2.75)

    # Роль чата GPT
    chat_role = (
        'Представь что ты лучший копирайтер в мире и пишешь лучшие объявления '
        'для социальной сети Instagram.'
    )

    # Пользовательский промт
    prompt = (
        ' Напиши объявление максимально отвечающее требованиям в запросе. '
        'Текст пиши со смайликами и разбивай на смысловые абзацы. В самом низу'
        ' добавь хештеги до 5ти слов. Хештеги должны быть релевантные '
        'содержанию данного объявления. Пиши креативно и разнообразно'
    )

    prompt += (
        f'. Из этого сделай краткий заголовок 5 слов, для Instagram: '
        f'{input1}, {input2}'
    )
    if input3.strip():
        prompt += f', {input3}'
    if input4.strip():
        prompt += (
            f'. Далее телефон напиши второй строчкой после заголовка: '
            f'{input4}'
        )
    if textarea1.strip():
        prompt += f'. Далее пиши дополнительные данные: {textarea1}'
    if input5.strip():
        prompt += f'. Вставь эти хештеги: {input5}'
    if dropdown1.strip():
        prompt += f'. Пиши текст в: {dropdown1}'
    if dropdown2.strip():
        prompt += f'. Призови: {dropdown2}'

    prompt += (
        f'. Напиши объявления не более: {max_length} символов. Пиши'
        f'максимально разнообразно.'
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
    )
