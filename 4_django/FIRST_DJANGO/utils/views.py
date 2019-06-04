
from django.shortcuts import render


def index(request):
    return render(request, 'utils/index.html')


def artii(request, keyword):
    import art
    result = art.text2art(keyword, 'ghost')
    context = {
        'result': result,
        'keyword': keyword,
    }
    return render(request, 'utils/artii.html', context)


# 사용자 입력 form 을 제공하는 액션
def stock_input(request):
    return render(request, 'utils/stock_input.html')


# 입력받은 data 를 처리하여 결과를 제공하는 액션
def stock_output(request):
    from iexfinance.stocks import Stock

    company_code = request.GET.get('company_code')
    TOKEN = 'pk_34947d6f20564c52a9dcd62bf4d4ab5f'

    try:
        stock = Stock(company_code, token=TOKEN)
        data = stock.get_quote()
    except:
        return render(request, 'utils/stock_output.html', {
            'is_ok': False,
            'message': '검색할 수 없습니다.'
        })
    return render(request, 'utils/stock_output.html', {
        'is_ok': True,
        'data': data
    })