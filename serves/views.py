
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import asyncio

from prompts.fairy_tales import get_fairy_tales_response
from prompts.fix import get_fix_response
from prompts.improve import get_improve_response
from prompts.inst import get_inst_response
from prompts.inst_post import get_inst_post_response
from prompts.ok_ad import get_ok_ad_response
from prompts.ok_post import get_ok_post_response
from prompts.rewrite import get_rewrite_response
from prompts.short import get_short_response
from prompts.site_ceo import get_site_ceo_response
from prompts.site_keywords import get_site_keywords_response
from prompts.site_struct import get_site_struct_response
from prompts.site_struct_page import get_site_struct_page_response
from prompts.site_url import get_site_url_response
from prompts.text_struct import get_text_struct_response
from prompts.tg import get_tg_response
from prompts.tg_post import get_tg_post_response
from prompts.translate import get_translate_response
from prompts.vk_ad import get_vk_ad_response
from prompts.vk_post import get_vk_post_response


@api_view(['post'])
def fairy_tales(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_fairy_tales_response(request))
    return Response(result)


@api_view(['post'])
def fix(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_fix_response(request))
    return Response(result)


@api_view(['post'])
def improve(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_improve_response(request))
    return Response(result)


@api_view(['post'])
def inst(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_inst_response(request))
    return Response(result)


@api_view(['post'])
def inst_post(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_inst_post_response(request))
    return Response(result)


@api_view(['post'])
def ok_ad(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_ok_ad_response(request))
    return Response(result)


@api_view(['post'])
def ok_post(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_ok_post_response(request))
    return Response(result)


@api_view(['post'])
def rewrite(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_rewrite_response(request))
    return Response(result)


@api_view(['post'])
def short(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_short_response(request))
    return Response(result)


@api_view(['post'])
def site_ceo(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_site_ceo_response(request))
    return Response(result)


@api_view(['post'])
def site_keywords(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_site_keywords_response(request))
    return Response(result)


@api_view(['post'])
def site_struct(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_site_struct_response(request))
    return Response(result)


@api_view(['post'])
def site_struct_page(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_site_struct_page_response(request))
    return Response(result)


@api_view(['post'])
def site_url(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_site_url_response(request))
    return Response(result)


@api_view(['post'])
def text_struct(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_text_struct_response(request))
    return Response(result)


@api_view(['post'])
def tg(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_tg_response(request))
    return Response(result)


@api_view(['post'])
def tg_post(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_tg_post_response(request))
    return Response(result)


@api_view(['post'])
def translate(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_translate_response(request))
    return Response(result)


@api_view(['post'])
def vk_ad(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_vk_ad_response(request))
    return Response(result)


@api_view(['post'])
def vk_post(request: Request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_vk_post_response(request))
    return Response(result)
