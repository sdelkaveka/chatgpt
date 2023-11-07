from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from prompts.ad.inst import get_inst_ad_response
from prompts.ad.ok import get_ok_ad_response
from prompts.ad.tg import get_tg_ad_response
from prompts.ad.vk import get_vk_ad_response
from prompts.child_par.fairy_tales import get_fairy_tale_response
from prompts.posts.inst import get_inst_post_response
from prompts.posts.ok import get_ok_post_response
from prompts.posts.tg import get_tg_post_response
from prompts.posts.vk import get_vk_post_response
from prompts.site.keywords import get_site_keywords_response
from prompts.site.seo_optimization import get_site_seo_optimization_response
from prompts.site.structure_page import get_structure_page_response
from prompts.site.structure_site import get_structure_site_response
from prompts.site.text__page import get_text_page_response
from prompts.site.url_generator import get_url_generator_response
from prompts.tools.corrector import get_corrector_response
from prompts.tools.enhance import get_enhance_response
from prompts.tools.rewrite import get_rewrite_response
from prompts.tools.shorten import get_shorten_response


@api_view(['post'])
def fairy_tale(request: Request):
    result = get_fairy_tale_response(request)
    return Response(result)


@api_view(['post'])
def corrector(request: Request):
    result = get_corrector_response(request)
    return Response(result)


@api_view(['post'])
def enhance(request: Request):
    result = get_enhance_response(request)
    return Response(result)


@api_view(['post'])
def inst_ad(request: Request):
    result = get_inst_ad_response(request)
    return Response(result)


@api_view(['post'])
def inst_post(request: Request):
    result = get_inst_post_response(request)
    return Response(result)


@api_view(['post'])
def ok_ad(request: Request):
    result = get_ok_ad_response(request)
    return Response(result)


@api_view(['post'])
def ok_post(request: Request):
    result = get_ok_post_response(request)
    return Response(result)


@api_view(['post'])
def rewrite(request: Request):
    result = get_rewrite_response(request)
    return Response(result)


@api_view(['post'])
def shorten(request: Request):
    result = get_shorten_response(request)
    return Response(result)


@api_view(['post'])
def site_seo_optimization(request: Request):
    result = get_site_seo_optimization_response(request)
    return Response(result)


@api_view(['post'])
def site_keywords(request: Request):
    result = get_site_keywords_response(request)
    return Response(result)


@api_view(['post'])
def structure_site(request: Request):
    result = get_structure_site_response(request)
    return Response(result)


@api_view(['post'])
def structure_page(request: Request):
    result = get_structure_page_response(request)
    return Response(result)


@api_view(['post'])
def url_generator(request: Request):
    result = get_url_generator_response(request)
    return Response(result)


@api_view(['post'])
def text_page(request: Request):
    result = get_text_page_response(request)
    return Response(result)


@api_view(['post'])
def tg_ad(request: Request):
    result = get_tg_ad_response(request)
    return Response(result)


@api_view(['post'])
def tg_post(request: Request):
    result = get_tg_post_response(request)
    return Response(result)


@api_view(['post'])
def vk_ad(request: Request):
    result = get_vk_ad_response(request)
    return Response(result)


@api_view(['post'])
def vk_post(request: Request):
    result = get_vk_post_response(request)
    return Response(result)
