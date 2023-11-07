
from rest_framework.request import Request

from core.gpt import handle_gpt3


def get_fairy_tale_response(request: Request):

    max_role_tokens = 100       	# Kоличество токенов роль чата по умолчанию
    # Kоличество токенов пользовательского запроса по умолчанию
    max_prompt_tokens = 2000
    max_response_tokens = 2000    # Kоличество токенов ответа чата по умолчанию
    set_token_price = 0.000002    # Цена одного токена
    temperature = 0.5             # Температура
    timeout = 5                   # Таймаут при нецензурном слове

    # Получаем JSON-данные из запроса от frontend
    data = request.data

    # Извлекаем 'Переменные' из запроса от frontend
    textarea1 = data.get('textarea1', '')         # Название
    textarea2 = data.get('textarea2', '')         # Главные(й) герои(й)
    textarea3 = data.get('textarea3', '')         # Остальные персонажи
    # Любые слова, они будут в сказке
    textarea4 = data.get('textarea4', '')
    textarea5 = data.get('textarea5', '')         # Сюжет
    dropdown1 = data.get('dropdown1', '')         # Стиль
    textarea6 = data.get('textarea6', '')         # Концовка

    # Роль чата GPT
    chat_role = (
        'Представь ты лучший российский детский писатель и пишешь очень '
        'оригинально и крайне разнообразно, умело применяешь юмор и шутки для '
        'детей и подросткод до 18 лет.'
    )

    # Пользовательский промт
    prompt = (
        ' Напиши пожалуйста интересную, захватывающую историю, простыми '
        'русскими словами по вот этим данным:'
    )

    if textarea1.strip():
        prompt += f' Название: [{textarea1}]'  # Название
    if textarea2.strip():
        # Главные(й) герои(й)
        prompt += f'. Главный герой: [{textarea2}]'
    if textarea3.strip():
        # Остальные персонажи
        prompt += f'. Остальные персонажи: [{textarea3}]'
    if textarea4.strip():
        # Любые слова, они будут в сказке
        prompt += (
            f'. Любые слова которые должны встречаться в тексте: [{textarea4}]'
        )
    if textarea5.strip():
        prompt += f'. Сюжет: [{textarea5}]'  # Сюжет
    if dropdown1.strip():
        prompt += f'. Пиши в стиле: [{dropdown1}]'  # Стиль
    if textarea6.strip():
        prompt += f'. В конце: [{textarea6}]'  # Концовка

    prompt += (
        '. Пиши с душой, интересный рассказ, по человечески и с юмором. Пиши '
        'без комментариев. Пиши оригинально не стандартно, придумывай '
        'разнообразные новые сюжеты, максимально включи фантазию. Не '
        'используй стандатрные шаблоны про дружбу и приключения.'
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
