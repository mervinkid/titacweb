#coding=utf-8
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http.response import Http404
from portal.models import GlobalSetting, Slide, Solution, Product
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
    solution_list = Solution.objects.get_enabled_solution()
    solutions = []
    for solution_item in solution_list:
        solution_id = convert_to_view_value(solution_item.id)
        solution_title = solution_item.title
        solution_subtitle = solution_item.subtitle
        solution_data = {
            'solution_id': solution_id,
            'solution_title': solution_title,
            'solution_subtitle': solution_subtitle,
        }
        solutions.append(solution_data)

    return render(
                request,
                'solution/solution.html',
                generate_context(
                    current='solution',
                    solutions=solutions
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
                    current='solution',
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

def search(request):
    query = request.GET.get('s', '')
    #对GET到的字符串数据进行转码
    query = unicode(query).encode(encoding='utf-8')
    #移除查询关键词前后的空格
    query = query.strip()
    #将关键词按照空格分割成list
    query_list = query.split(' ')
    search_result = []
    if 'search' not in request.COOKIES:
        #查询解决方案
        solution_result = Solution.objects.get_search(query_list)
        for solution_item in solution_result:
            solution_id = convert_to_view_value(solution_item.id)
            solution_title = solution_item.title
            solution_sketch = solution_item.sketch
            if len(solution_sketch) > 100:
                solution_sketch = solution_sketch[0:100] + '...'
            result_item = {
                'type': 'solution',
                'id': solution_id,
                'title': solution_title,
                'sketch': solution_sketch,
            }
            search_result.append(result_item)
        #查询产品
        product_result = Product.objects.get_search(query_list)
        for product_item in product_result:
            product_id = convert_to_view_value(product_item.id)
            product_title  = product_item.title
            product_sketch = product_item.sketch
            if len(product_sketch) > 100:
                product_sketch = product_sketch[0:100] + '...'
            result_item = {
                'type': 'product',
                'id': product_id,
                'title': product_title,
                'sketch': product_sketch,
            }
            search_result.append(result_item)

    if len(search_result) == 0:
        search_result= None

    query_history = request.COOKIES.get('query_history')
    if not query_history:
        if not query == '':
            query_history = query
    else:
        #将本次关键词加入搜索历史
        tmp = query_history.split(',')
        in_history = False
        #遍历搜索历史的每一项，检查是否有与本次关键词完全一样的项目
        for tmp_item in tmp:
            if query == tmp_item:
                in_history = True
                break
        #不存在完全一样的项则将其加入搜索历史
        if not in_history:
            query_history = query +  ',' + query_history

    #将cookie中取得的历史记录转换成list，该list将传递给页面模板
    if query_history:
        history_list = query_history.split(',')
    else:
        history_list = []

    response = render(
        request,
        'search.html',
        generate_context(
            current='home',
            search_result=search_result,
            query=query,
            history_list=history_list,
        )
    )
    #搜索历史保存在客户端本地Cookie
    response.set_cookie('search', max_age=1)
    #历史列表保存时间为2小时
    response.set_cookie('query_history', query_history, max_age=7200)

    return response

def h404(request):
    return render(request, '404.html', generate_context(current='home'))

def h500(request):
    return render(request, '500.html', generate_context(current='home'))

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
