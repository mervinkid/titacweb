#coding=utf-8
import datetime
from django.conf import settings
from django.shortcuts import render
from portal.models import GlobalSetting, Slide

def home(request):
    '''
    :param request:
    :return:
    '''
    #load slide data
    slide_list = Slide.objects.filter(enable=1).order_by('-update')

    return render(
        request,
        'home/home.html',
        generate_context(
            current='home',
            slides=slide_list
        )
    )

def solution(request):
    '''
    :param request:
    :return:
    '''
    context = generate_context(current='solution')
    return render(request, 'solution/solution.html', context)

def solution_detail(request, param):
    '''
    :param id:
    :return:
    '''
    context = generate_context(current='solution')
    return render(request, 'solution/solution_detail.html', context)

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
    current = contexts
    #获取DEBUG状态
    debug = settings.DEBUG
    #获取全局页面关键字设置
    try:
        keyword = GlobalSetting.objects.get(key='keyword').value
    except Exception, error:
        keyword = ''
    #获取页面简述设置
    try:
        description = GlobalSetting.objects.get(key='description').value
    except Exception, error:
        description = ''
    #获取联系电话
    try:
        call = GlobalSetting.objects.get(key='call').value
    except Exception, error:
        call = ''
    #获取联系邮箱
    try:
        mail = GlobalSetting.objects.get(key='mail').value
    except Exception, error:
        mail = ''
    #获取当前年份
    year = datetime.datetime.now().year
    #将数据装入页面上下文
    context = {
        'current': current,
        'debug': debug,
        'keyword': keyword,
        'description': description,
        'call': call,
        'mail': mail,
        'year': year,
    }
    return context
