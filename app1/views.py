from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    # this page open request to server for this text for execute,
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, 'home.html', {"title_name": "azhar"}) # here request is using for fetch the data


def profile(request):
    return HttpResponse("<h2>profile page</h2>")
'''
client to server method: GET(to recieve the data from server),POST(to store the data to from),PUT(to store
the data like wikipeadia.
server to client method: Httpresponse(the response from server and show the data, request response(response from server
to redirect into html page)
GET:to get fetch the data
POST: to post the data
'''
# if i using get method instead of using post method then the url shows the number which one we want to calculate,so get method is not secure


def expression(request):
    a = int(request.GET['text1']) # get function is use for when a client needs a information from server
    b = int(request.GET['text2']) # we need type casting because the value comes from html file is string
    c = a+(2*b) # GET,POST,PUT,DELETE these methods always writes in capital format
    return render(request,'output.html', {"result":c }) # here passing a dictionary which key is result and value is c
