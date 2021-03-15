# I have created this website - Abir
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html',)

def ex1(request):
    return HttpResponse('''<center><h1>Website Directory</h1><table border="1">
    <tr><td>Website Name</td><td>Information</td></tr>
    <tr><td><a href="https://www.youtube.com">Youtube</a></td><td>A free video sharing website</td></tr>
    <tr><td><a href="https://www.facebook.com">Facebook</a></td><td>A social site</td></tr></table></center>''')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        # Analyze the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, "analyze.html", params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    elif charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}



    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on":
        return HttpResponse("Please selecta an operation!!!")

    return render(request, 'analyze.html', params)