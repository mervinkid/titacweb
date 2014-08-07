from django.shortcuts import render
from django.conf import settings
from portal.models import Slide
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
    debug = settings.DEBUG
    context = {
        'current': current,
        'debug': debug,
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
