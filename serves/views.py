from rest_framework.decorators import api_view
from rest_framework.request import Request

from prompts.vk import get_vk_response


@api_view(['post'])
def vk_ad(request: Request):
    return get_vk_response(request)
