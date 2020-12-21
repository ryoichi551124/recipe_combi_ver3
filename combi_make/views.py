from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import random
from . import method
import pandas as pd


def index(request):
    #組み合わせを取得
    params = method.random_get()
    return render(request, 'combi_make/index.html', params)

def ok(request):
    #POSTから選んだ組み合わせの値を取得
    main_num = request.POST['main_num']
    sub_num = request.POST['sub_num']
    soup_num = request.POST['soup_num']
    judge = True

    #trainデータに追加する処理
    method.choice(main_num, sub_num, soup_num, judge)
    #新しい組み合わせを取得
    params = method.random_get()
    return render(request, 'combi_make/index.html', params)

def no(request):
    #POSTから選んだ組み合わせの値を取得
    main_num = request.POST['main_num']
    sub_num = request.POST['sub_num']
    soup_num = request.POST['soup_num']
    judge = False

    #trainデータに追加する処理
    method.choice(main_num, sub_num, soup_num, judge)
    #新しい組み合わせを取得　
    params = method.random_get()
    return render(request, 'combi_make/index.html', params)


def download(request):
    response = HttpResponse(open("train.csv", 'rb').read()) 
    response['Content-Type'] = 'text/csv' 
    response['Content-Disposition'] = 'attachment; filename=train.csv' 
    return response 
