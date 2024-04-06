from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from kafka_app.producer import kafka_producer_send_message
from kafka_app.consumer import KafkaConsumerThread, get_messages
from data_transfer.settings import kafka_default_config  # 确保从正确的位置导入settings


@require_http_methods(["POST"])  # 限制只接收POST请求
@csrf_exempt
def kafka_producer_view(request):
    # 从HTTP POST请求的body中解析JSON数据
    try:
        data = json.loads(request.body)
        message = data.get('message')
        if message:
            kafka_producer_send_message(message)
            return JsonResponse({'status': 'Message sent to Kafka successfully'})
        else:
            return JsonResponse({'error': 'Message is required'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


# start consumer
@require_http_methods(["GET"])
@csrf_exempt
def kafka_consumer_view(request):
    # 从HTTP POST请求的body中解析JSON数据
    try:
        consumer_thread = KafkaConsumerThread(max_messages=5)
        consumer_thread.start()
        return JsonResponse({'status': 'Message received from Kafka successfully'})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@require_http_methods(["GET"])
@csrf_exempt
def kafka_message_view(request):
    # 从HTTP POST请求的body中解析JSON数据
    try:
        message = get_messages()
        return JsonResponse({'message': message})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)