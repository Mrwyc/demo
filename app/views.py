from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from app import models
import json

@csrf_exempt
def upload(request):
    """
    保存客户端，分数
    获取最新插入一条数据
    :param request: 
    :return: 
    
    agentnum： 客户端
    fraction： 分数
    POST请求
    /api/upload/
    """
    result = {}
    if request.method == 'POST':
        agent = request.POST['agentnum']
        fraction = request.POST['fraction']
        if agent and fraction:
            user_score = models.Fraction.objects.all()
            new_data = user_score.order_by('id').last()
            result['code'] = '200'
            result['message'] = '添加成功'
            result['newData'] = {'client':new_data.client, 'score':new_data.score}
        else:
            result['code'] = '201'
            result['message'] = '添加失败'
    return  JsonResponse(result)



def scored(request):
    """
    分数排序，去除当前用户最小分数，获取最大分数
    :param request: 
    :return: 
    GET请求
    /api/score/
    """
    client = []
    score_num = []
    score_li = [score_obj for score_obj in models.Fraction.objects.all().order_by('-score')]
    for i in score_li:
        if i.client not in client and i.score not in score_num:
            client.append(i.client)
            score_num.append(i.score)
    result = {k:v for k,v in zip(client, score_num)}
    return JsonResponse({'code':200, 'data':result})