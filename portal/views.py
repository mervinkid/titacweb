#coding=utf-8
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http.response import Http404
from portal.models import GlobalSetting, Slide, Solution
from portal.utils import convert_to_data_value, convert_to_view_value

def home(request):
    '''
    :param request:
    :return:
    '''
    #load slide data
    slide_list = Slide.objects.get_enabled_slide()

    return render(
                request,
                'home/home.html',
                generate_context(
                    current='home',
                    slides=slide_list
                ))

def solution(request):
    '''
    :param request:
    :return:
    '''
    return render(
                request,
                'solution/solution.html',
                generate_context(
                    current='solution',
                ))

def solution_detail(request, id):
    '''
    :param request:
    :param id:
    :return:
    '''
    solution_id = convert_to_data_value(id)
    solution_item = Solution.objects.get_solution_by_id(solution_id)
    if not solution_item:
        raise Http404

    return render(
                request,
                'solution/solution_detail.html',
                generate_context(
                    current='current',
                    solution_item=solution_item,
                ))

def product(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='product')
    return render(request, 'product/product.html', context)

def product_detail(request, param):
    '''
    :param request:
    :param param:
    :return:
    '''
    context = generate_context(current='product')
    context['current'] = 'product'
    return render(request, 'product/product_detail.html', context)
def service(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='service')
    return render(request, 'service/service.html', context)

def download(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='download')
    return render(request, 'download/download.html', context)

def partner(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='partner')
    return render(request, 'partner/parter.html', context)

def career(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='career')
    return render(request, 'career/career.html', context)

def company(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='company')
    return render(request, 'company/company.html', context)
    
def privacy(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='company')
    return  render(request, 'company/privacy.html', context)

def term(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='company')
    return render(request, 'company/term.html', context)

def generate_context(**contexts):
    '''
    生成页面上下文信息
    :return:
    '''
    #获取传入的上下文
    input_context = dict(contexts)
    #获取DEBUG状态
    debug = settings.DEBUG
    #获取全局设置
    g_settings = GlobalSetting.objects.get_settings()
    #获取当前年份
    year = datetime.datetime.now().year
    #将数据装入页面上下文
    setting_context = {
        'debug': debug,
        'g_settings': g_settings,
        'year': year,
    }
    context = dict(input_context.items() + setting_context.items())
    return context
