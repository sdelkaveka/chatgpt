from rest_framework.decorators import api_view
from rest_framework.request import Request

from prompts.ad_ok import get_ok_ad_response
from prompts.tg import get_tg_response
from prompts.vk_ad import get_vk_ad_response


@api_view(['post'])
def vk_ad(request: Request):
    return get_vk_ad_response(request)


@api_view(['post'])
def ok_ad(request: Request):
    return get_ok_ad_response(request)


@api_view(['post'])
def tg_ad(request: Request):
    return get_tg_response(request)
