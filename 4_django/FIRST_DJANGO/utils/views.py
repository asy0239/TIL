from django.shortcuts import render
import art

# Create your views here.


def index(request):
    return render(request, 'utils/index.html')


def artii(request, keyword):
    result = art.text2art(keyword, font='alpha')
    context = {
        'result': result,
        'keyword': keyword,
    }
    return render(request, 'utils/artii.html', context)


def stock(request):
    pass  # todo: 완성하기
