#this file is created by abhinav
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    #checkbox value
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newline=request.POST.get('newline','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=='on':
        analyzed = ""
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params={'purpose':'analyzed text','analyze':analyzed}
        djtext=analyzed

    if uppercase=='on':
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'uppercase', 'analyze': analyzed}
        djtext=analyzed

    if newline=='on':
        analyzed = ""
        for char in djtext:
            if char!='/n':
                analyzed=analyzed+char
        params = {'purpose': 'newline removed', 'analyze': analyzed}
        djtext=analyzed

    if charcount=='on':
        analyzed=len(djtext)
        params = {'purpose': 'total character', 'analyze': analyzed}



    if(removepunc!='on' and uppercase!='on' and newline!='on' and charcount!='on'):
        return HttpResponse('please enter the checkbox')

    return render(request, 'analyze.html', params)

def contact(request):
    return render(request,'contact.html')