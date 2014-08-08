#coding=utf-8
import datetime
from django.shortcuts import render
from django.conf import settings
from portal.models import GlobalSetting, Slide
from django.http.response import Http404

def home(request):
    '''
    :param request:
    :return:
    '''
    #init response context
    context = init_context('home')
    #load slide data
    slide_list = Slide.objects.filter(enable=1).order_by('-update')
    context['slides'] = slide_list

    return render(request, 'home/home.html', context)

def solution(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('solution')
    return render(request, 'solution/solution.html', context)

def solution_detail(request, param):
    '''
    :param id:
    :return:
    '''
    context = init_context('solution')
    return render(request, 'solution/solution_detail.html', context)

def product(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('product')
    return render(request, 'product/product.html', context)

def product_detail(request, param):
    '''
    :param request:
    :param param:
    :return:
    '''
    context = init_context('product')
    context['current'] = 'product'
    return render(request, 'product/product_detail.html', context)
def service(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('service')
    return render(request, 'service/service.html', context)

def download(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('download')
    return render(request, 'download/download.html', context)

def partner(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('partner')
    return render(request, 'partner/parter.html', context)

def career(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('career')
    return render(request, 'career/career.html', context)

def company(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('company')
    return render(request, 'company/company.html', context)
    
def privacy(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('company')
    return  render(request, 'company/privacy.html', context)

def term(request):
    '''
    :param request:
    :return:
    '''
    context = init_context('company')
    return render(request, 'company/term.html', context)

def init_context(current):
    '''
    init http response context
    :return:
    '''
    #获取DEBUG状态
    debug = settings.DEBUG
    #获取全局页面关键字设置
    try:
        keyword = GlobalSetting.objects.get(key='keyword').value
    except:
        keyword = ''
    #获取页面简述设置
    try:
        description = GlobalSetting.objects.get(key='description').value
    except:
        description = ''
    #获取联系电话
    try:
        call = GlobalSetting.objects.get(key='call').value
    except:
        call = ''
    #获取联系邮箱
    try:
        mail = GlobalSetting.objects.get(key='mail').value
    except:
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

def data_id_to_page_id(param):
    '''
    Convert data id value into page id value.
    :param param:
    :return:
    '''
    try:
        data_id = int(param)
    except:
        data_id = 0
    return data_id + 1000

def page_id_to_data_id(param):
    '''
    Convert page id value into data id value.
    :param parm:
    :return:
    '''
    try:
        page_id = int(param)
    except:
        page_id = 1000
    if page_id < 1000:
        page_id = 1000
    return page_id - 1000
