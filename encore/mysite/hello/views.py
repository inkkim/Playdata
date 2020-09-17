from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def TellHello(requests):
    html = """<title> 수업 </title>
    <h1> Hello, !! </h1>
    <h2> Hello, !! </h2>
    <h3> Hello, !! </h3>
    <a href="https://naver.com">네이버 </a>
    <p> 테스트 입니다. </p>"""
    return HttpResponse(html)