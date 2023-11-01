import math

import tiktoken
from rest_framework.exceptions import ValidationError


def count_tokens_and_price(
        messages: list[dict],
        set_token_price: int,
        max_role_tokens: int,
        max_prompt_tokens: int,
        max_response_tokens: int,
):
    max_tokens = max_role_tokens + max_prompt_tokens + max_response_tokens
    tokens_per_message = 5  # Спец символы GPT3-turbo
    tokens_per_name = 1  # Спец символы при name сообщении
    total_tokens = 0
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    response = {
        "calculated_data": {},
        "calculated_prompt_tokens": 0,
        "calculated_role_tokens": 0,
        "input_data": {
            "set_token_price": set_token_price,
            "tokens_sum": max_tokens,
            "max_role_tokens": max_role_tokens,
            "max_prompt_tokens": max_prompt_tokens,
            "max_response_tokens": max_response_tokens
        }
    }

    msg_num = 1
    for message in messages:
        tokens_count = 0
        tokens_count += tokens_per_message
        tokens_count += len(encoding.encode(message['content']))
        if message['role'] == "system":
            response['calculated_role_tokens'] += len(
                encoding.encode(message['content'])) + tokens_per_message
        # Если у сообщения есть имя, добавляем токен
        if message['role'] == "name":
            tokens_count += tokens_per_name
        if message['role'] == "user":
            tokens_count += tokens_per_name
            response["calculated_prompt_tokens"] += tokens_count
        total_tokens += tokens_count
        msg_name = message['role'] + '_' + str(msg_num)
        response["calculated_data"][msg_name] = {
            'tokens': tokens_count
        }
        msg_num += 1

    # Определяем превышает ли Промпт ограничение
    if max_prompt_tokens < response['calculated_prompt_tokens']:
        raise ValidationError('Промпт превышает ограничение!')

    # Определяем превышает ли Роль ограничение
    if max_role_tokens < response['calculated_role_tokens']:
        raise ValidationError('Роль превышает ограничение!')

    return response


def price_from_tokens(
        openai_response,
        set_token_price: int,
):
    total_tokens = openai_response['usage']['total_tokens']
    prompt_tokens = openai_response['usage']['prompt_tokens']
    completion_tokens = openai_response['usage']['completion_tokens']

    # Считаем стоимость (округляем в большую сторону)
    price = math.ceil(total_tokens * set_token_price)
    return {
        'actual_combined_tokens': total_tokens,
        'actual_prompt_tokens': prompt_tokens,
        'actual_response_tokens': completion_tokens,
        'total_cost': price,
        'current_token_price': set_token_price
    }
