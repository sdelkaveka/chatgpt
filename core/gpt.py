
import openai
from rest_framework.exceptions import ValidationError

from .token_price import count_tokens_and_price, price_from_tokens
from .validators import validate_prompt
from chatgpt.settings import env


async def handle_gpt3(
    chat_role,
    promt,
    timeout=0,
    temperature=0.7,
    set_token_price=1,
    max_role_tokens=50,
    max_prompt_tokens=50,
    max_response_tokens=50,
    model_chat_gpt="gpt-3.5-turbo"  # or gpt-4
):

    openai.api_key = env.str('OPEN_AI_KEY')

    # Определяем сообщения для GPT-3
    messages = [
        {"role": "system", "content": chat_role},
        {"role": "user", "content": promt}
    ]

    # Валидируем промпт
    validate_prompt(promt, timeout)

    # Считаем стоимость запроса
    server_tokens_and_price = count_tokens_and_price(
        messages,
        set_token_price,
        max_role_tokens,
        max_prompt_tokens,
        max_response_tokens
    )

    try:
        # Создаем запрос к GPT-3 и получаем ответ
        openai_response = await openai.ChatCompletion.create(
            model=model_chat_gpt,
            messages=messages,
            temperature=temperature,
            max_tokens=max_response_tokens
        )

    except Exception as exc:
        raise ValidationError(exc)

    # Считаем стоимость ответа
    chat_tokens_and_price = price_from_tokens(
        openai_response,
        set_token_price
    )

    return get_response(
        openai_response,
        chat_role,
        promt,
        server_tokens_and_price,
        chat_tokens_and_price
    )


def get_response(
        openai_response,
        chat_role,
        promt,
        server_tokens_and_price,
        chat_tokens_and_price
):
    return {
        "answer": openai_response['choices'][0]['message']['content'],
        "adminFieldContent": chat_role,
        "use_promt": promt,
        "server_system_info": server_tokens_and_price,
        "chat_system_info": chat_tokens_and_price,
    }
