# coding=utf-8
from datetime import datetime
from urllib.parse import quote, unquote

from django.conf import settings
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from portal.models import *
from portal.utils import remove_html_tag


@cache_page(60 * 5)
def home(request):
    """
    :param request:
    :return:
    """
    # load slide data
    slide_list = Slide.objects.get_enabled_slide()
    # load top data
    top_data_count = 10
    # load solution top data
    solution_list = [{'title': solution.title, 'pid': solution.id} for solution in
                     Solution.objects.get_enabled_solution(count=top_data_count)]

    # load product top data
    product_list = [{'title': product.title, 'pid': product.id} for product in
                    Product.objects.get_enabled_product(count=top_data_count)]

    # load service top data
    service_list = [{'title': service.title, 'pid': service.id} for service in
                    Service.objects.get_enabled_service(count=top_data_count)]

    # load partner top data
    top_data_count = 8
    partner_list = [{'title': partner.title, 'website': partner.website, 'logo': partner.logo} for partner in
                    Partner.objects.get_partners(count=top_data_count)]

    # load customer top data
    customer_list = [{'title': customer.title, 'logo': customer.logo} for customer in
                     Customer.objects.get_all_customer(count=top_data_count)]

    return render(
        request,
        'home/home.html',
        generate_context(
            current='home',
            slides=slide_list,
            partner_list=partner_list,
            customer_list=customer_list,
            solution_list=solution_list,
            product_list=product_list,
            service_list=service_list,
        )
    )


@cache_page(60 * 5)
def solution(request):
    """
    :param request:
    :return:
    """
    solution_list = Solution.objects.get_enabled_solution()
    solutions = []
    for solution_item in solution_list:
        solution_id = solution_item.id
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
        )
    )


@cache_page(60 * 5)
def solution_detail(request, solution_id):
    """
    :param request:
    :param solution_id:
    :return:
    """
    solution_id = solution_id
    solution_item = Solution.objects.get_solution_by_id(solution_id)
    if not solution_item:
        raise Http404
    # 获取关键词
    solution_keywords = solution_item.keyword
    # 获取内容
    solution_content_list = SolutionContent.objects.get_content_by_solution_id(solution_id)
    # 获取相关信息
    # 获取相关产品
    product_list = list(solution_item.products.all().filter(enable=1))
    customer_list = set()
    partner_list = set()
    for product_item in product_list:
        # 获取相关用户
        for customer_item in list(product_item.customers.all()):
            customer_list.add(customer_item)
        # 获取相关合作伙伴
        partner_list.add(product_item.partner)

    return render(
        request,
        'solution/solution_detail.html',
        generate_context(
            current='solution',
            solution_item=solution_item,
            solution_content_list=solution_content_list,
            product_list=product_list,
            product_count=len(product_list),
            customer_list=customer_list,
            customer_count=len(customer_list),
            partner_list=partner_list,
            partner_count=len(partner_list),
            keywords=solution_keywords,
        )
    )


@cache_page(60 * 5)
def product(request):
    """
    :param request:
    :return:
    """
    product_list = Product.objects.get_enabled_product()
    products = list()
    for product_item in product_list:
        product_id = product_item.id
        product_title = product_item.title
        product_subtitle = product_item.subtitle
        product_partner = product_item.partner
        product_data = {
            'product_id': product_id,
            'product_title': product_title,
            'product_subtitle': product_subtitle,
            'product_partner': product_partner,
        }
        products.append(product_data)
    return render(
        request,
        'product/product.html',
        generate_context(
            current='product',
            products=products,
        )
    )


@cache_page(60 * 5)
def product_detail(request, product_id):
    """
    :param request:
    :param product_id:
    :return:
    """
    product_id = product_id
    product_item = Product.objects.get_product_by_id(product_id)
    if not product_item:
        raise Http404
    keywords = product_item.keyword
    # 获取内容
    product_content_list = ProductContent.objects.get_content_by_product_id(product_id)
    # 获取相关方案
    solution_list = list(product_item.solutions.all().filter(enable=1))
    # 获取相关客户信息
    customer_list = list(product_item.customers.all())

    return render(
        request,
        'product/product_detail.html',
        generate_context(
            current='product',
            product_item=product_item,
            keywords=keywords,
            solution_list=solution_list,
            solution_count=len(solution_list),
            product_content_list=product_content_list,
            customer_list=customer_list,
            customer_count=len(customer_list)
        )
    )


@cache_page(60 * 5)
def service(request):
    """
    :param request:
    :return:
    """
    # load enabled service
    service_list = Service.objects.get_enabled_service()
    services = list()
    for service_item in service_list:
        service_id = service_item.id
        service_title = service_item.title
        service_sketch = service_item.sketch
        service_data = {
            'service_id': service_id,
            'service_title': service_title,
            'service_sketch': service_sketch,
        }
        services.append(service_data)
    return render(
        request,
        'service/service.html',
        generate_context(
            current='service',
            services=services
        )
    )


@cache_page(60 * 5)
def service_detail(request, service_id):
    """
    :param request:
    :param service_id:
    :return:
    """
    service_id = service_id
    service_item = Service.objects.get_service_by_id(service_id)
    if not service_item:
        raise Http404

    keywords = service_item.keyword

    return render(
        request,
        'service/service_detail.html',
        generate_context(
            current='service',
            service_item=service_item,
            keywords=keywords
        )
    )


def download(request):
    """
    :param request:
    :return:
    """
    return render(
        request,
        'download/download.html',
        generate_context(
            current='download'
        )
    )


@cache_page(60 * 5)
def partner(request):
    """
    :param request:
    :return:
    """
    # load data
    partner_list = Partner.objects.get_partners()
    customer_list = Customer.objects.get_all_customer()
    return render(
        request,
        'partner/partner.html',
        generate_context(
            current='partner',
            partner_list=partner_list,
            customer_list=customer_list,
        )
    )


@cache_page(60 * 5)
def career(request):
    """
    :param request:
    :return:
    """
    context = generate_context(current='career')
    return render(request, 'career/career.html', context)


@cache_page(60 * 5)
def company(request):
    """
    :param request:
    :return:
    """
    return render(
        request,
        'company/company.html',
        generate_context(
            current='company'
        )
    )


@cache_page(60 * 5)
def privacy(request):
    """
    :param request:
    :return:
    """
    return render(
        request,
        'company/privacy.html',
        generate_context(
            current='company'
        )
    )


@cache_page(60 * 5)
def term(request):
    """
    :param request:
    :return:
    """
    return render(
        request,
        'company/term.html',
        generate_context(
            current='company'
        )
    )


def search(request):
    query = request.GET.get('s', '')
    # 对GET到的字符串数据进行转码
    # 移除查询关键词前后的空格
    # query = str(query).encode(encoding='utf-8')
    query = query.strip()
    # 将关键词按照空格分割成list
    query_list = query.split(' ')
    search_result = []
    # 判断用户行为是否允许进行查询
    valid_rate = False
    valid_keyword = False
    # 搜索频率是否正常
    if 'search' not in request.COOKIES:
        valid_rate = True
    # 搜索词是否为空
    if not query == '':
        valid_keyword = True
    # 开始进行查询
    if valid_rate and valid_keyword:
        # 查询解决方案
        solution_result = Solution.objects.get_search(query_list)
        for solution_item in solution_result:
            solution_id = solution_item.id
            solution_title = solution_item.title
            solution_sketch = remove_html_tag(solution_item.sketch)
            if len(solution_sketch) > 100:
                solution_sketch = solution_sketch[0:100] + '...'
            result_item = {
                'type': 'solution',
                'id': solution_id,
                'title': solution_title,
                'sketch': solution_sketch,
            }
            search_result.append(result_item)

        # 查询解决方案内容
        solution_content_result = SolutionContent.objects.get_search(query_list)
        # 检查所属解决方案在查询结果是否已存在
        for solution_content_item in solution_content_result:
            solution_id = solution_content_item.solution.id
            exist = False
            for search_result_item in search_result:
                if search_result_item['type'] == 'solution' \
                        and search_result_item['id'] == solution_id:
                    exist = True
                    break
            if not exist:
                solution_item = Solution.objects.get_solution_by_id(solution_id)
                if not solution_item:
                    continue
                solution_id = solution_id
                solution_title = solution_item.title
                solution_sketch = solution_item.sketch
                solution_sketch = remove_html_tag(solution_sketch)
                if len(solution_sketch) > 100:
                    solution_sketch = solution_sketch[0:100] + '...'
                result_item = {
                    'type': 'solution',
                    'id': solution_id,
                    'title': solution_title,
                    'sketch': solution_sketch
                }
                search_result.append(result_item)

        # 查询产品
        product_result = Product.objects.get_search(query_list)
        for product_item in product_result:
            product_id = product_item.id
            product_title = product_item.title
            product_sketch = remove_html_tag(product_item.sketch)
            if len(product_sketch) > 100:
                product_sketch = product_sketch[0:100] + '...'
            result_item = {
                'type': 'product',
                'id': product_id,
                'title': product_title,
                'sketch': product_sketch,
            }
            search_result.append(result_item)

        # 查询产品内容
        product_content_result = ProductContent.objects.get_search(query_list)
        # 检查所属产品在查询结果是否已存在
        for product_content_item in product_content_result:
            product_id = product_content_item.product.id
            exist = False
            for search_result_item in search_result:
                if search_result_item['type'] == 'product' \
                        and search_result_item['id'] == product_id:
                    exist = True
                    break
            if not exist:
                product_item = Product.objects.get_product_by_id(product_id)
                if not product_item:
                    continue
                product_id = product_id
                product_title = product_item.title
                product_sketch = product_item.sketch
                product_sketch = remove_html_tag(product_sketch)
                if len(product_sketch) > 100:
                    product_sketch = product_sketch[0:100] + '...'
                result_item = {
                    'type': 'product',
                    'id': product_id,
                    'title': product_title,
                    'sketch': product_sketch
                }
                search_result.append(result_item)

        # 查询服务
        service_result = Service.objects.get_search(query_list)
        for service_item in service_result:
            service_id = service_item.id
            service_title = service_item.title
            service_sketch = remove_html_tag(service_item.sketch)
            if len(service_sketch) > 100:
                service_sketch = service_sketch[0:100] + '...'
            result_item = {
                'type': 'service',
                'id': service_id,
                'title': service_title,
                'sketch': service_sketch
            }
            search_result.append(result_item)

    # 没有查询到数据的消息反馈
    # 消息类型：
    # 0：搜索频率过快
    # 1：关键词为空
    # 2：没有查询到结果
    message = ''
    search_result_count = len(search_result)
    if search_result_count == 0:
        search_result = None
        if not valid_rate:
            message = 0
        elif not valid_keyword:
            message = 1
        else:
            message = 2

    query_history = request.COOKIES.get('query_history')
    if not query_history or query_history == 'None':
        if query != '':
            query_history = list()
            query_history.append(query)
    else:
        # 将本次关键词加入搜索历史
        query_history = unquote(query_history).split(',')
        # 遍历搜索历史的每一项，检查是否有与本次关键词完全一样的项目
        for i in range(0, len(query_history), 1):
            if query == query_history[i]:
                del query_history[i]
                break
        # 不存在完全一样的项则将其加入搜索历史
        if not query == '':
            query_history.insert(0, query)
        # 保持历史记录项目数量不超过6
        while len(query_history) > 6:
            del query_history[len(query_history) - 1]

    # 将cookie中取得的历史记录转换成list，该list将传递给页面模板
    history_list = query_history
    query_history = ','.join(query_history)

    response = render(
        request,
        'search/search.html',
        generate_context(
            current='home',
            search_result=search_result,
            search_result_count=search_result_count,
            query=query,
            history_list=history_list,
            message=message
        )
    )
    # 搜索历史保存在客户端本地Cookie
    response.set_cookie('search', max_age=1)
    # 历史列表保存时间为2小时
    response.set_cookie('query_history', value=quote(query_history), max_age=7200)

    return response


@cache_page(60 * 5)
def h404(request):
    return render(
        request,
        'common/http404.html',
        generate_context(
            current='home'
        )
    )


@cache_page(60 * 5)
def h500(request):
    return render(
        request,
        'common/http500.html',
        generate_context(
            current='home'
        )
    )


def generate_context(**contexts):
    """
    生成页面上下文信息
    :return:
    """
    # 获取传入的上下文
    input_context = dict(contexts)
    # 获取DEBUG状态
    use_cdn = settings.USE_CDN
    # 获取设置
    call_setting = GlobalSetting.objects.get_phone_setting()
    mail_setting = GlobalSetting.objects.get_mail_setting()
    keyword_setting = GlobalSetting.objects.get_keyword_setting()
    description_setting = GlobalSetting.objects.get_description_setting()
    # 获取当前年份
    year = datetime.now().year
    # 将数据装入页面上下文
    setting_context = {
        'use_cdn': use_cdn,
        'year': year,
        'call_setting': call_setting,
        'mail_setting': mail_setting,
        'description_setting': description_setting,
    }
    context = dict(list(input_context.items()) + list(setting_context.items()))
    if ('keywords' in context) is False:
        context['keywords'] = keyword_setting
    else:
        if context['keywords'] == str():
            context['keywords'] = keyword_setting
    return context


def media_direct(request, *args):
    url = str(args[0])
    url = url.replace('http:/', 'http://')
    return redirect(to=url)
