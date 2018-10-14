from django.shortcuts import render
from .forms import formsingup
from .models import UserData
from .models import Queries
from .models import Solutions
from .models import EventsLog
from django.core.serializers.json import DjangoJSONEncoder
import json
import datetime
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        print("Already Logged iN")

    return render(request, 'index.html')



def signup(request):
    if request.user.is_authenticated:
        print("Already Logged iN")

    print(f"TEST: {request.method}")

    if request.method == "POST":
        form = formsingup(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(username=form.cleaned_data['Username'],
                                                password=form.cleaned_data['Password'])
                user.save()


                userdata = UserData()
                userdata.username = form.cleaned_data['Username']
                userdata.fname = form.cleaned_data['First_Name']
                userdata.lname = form.cleaned_data['Last_Name']
                userdata.email = form.cleaned_data['Email']

                userdata.save()

            except Exception as ex:
                return render(request, 'index.html', {'error': 'user ' + form.cleaned_data['Username']+ ' exists already'})

            return render(request, 'index.html')

    form = formsingup()
    context = {'signupf': form}

    return render(request, 'signup.html', context)



def userprofile(request):
    if not request.user.is_authenticated:
        print("NOT Logged iN")
        return render(request, 'index.html')

    userdata = UserData.objects.get(username=request.user.username)
    data = viz1(request)
    (mtot, mmor, mday,meve) = viz2(request)


    #print("INTO USER PROFILE METHOD")

    context = {
        'userdata': userdata,
        'data': data,
        'mtot': mtot,
        'mmor': mmor,
        'mday': mday,
        'meve': meve
    }

    return render(request, 'userprofile.html', context)


def stackoverflow(request):
    if not request.user.is_authenticated:
        print("NOT Logged iN")
        return render(request, 'index.html')

    querydata = Queries.objects.all()
    context = {
        'querydata': querydata,
    }
    return render(request, 'stackoverflow.html', context)


def answers(request):
    if not request.user.is_authenticated:
        print("NOT Logged iN")
        return render(request, 'index.html')

    title = request.GET.get('qid', None)

    #print (title)

    answers = Solutions.objects.all().filter(title=title)
    context = {
        'answers' : answers,
    }
    return render(request, 'answers.html', context)

def saveDB(request):
   # print("SAVEDB")
    eventloggedobj = EventsLog()
    eventloggedobj.userid = UserData.objects.get(username=request.user.username)
    eventloggedobj.username=request.user.username
    eventloggedobj.currentTime = datetime.datetime.now()
    eventloggedobj.event = request.GET.get('Event')
   # print("Event is :....", request.GET.get('Event'))
    eventloggedobj.save()
    return render(request, 'index.html')

def viz1(request):
   # print ("INTO VIZ Function")
    hoverEvent=EventsLog.objects.all().filter(event='hover')
    mouseMoveEvent = EventsLog.objects.all().filter(event='MouseMove')
    scrollEvent = EventsLog.objects.all().filter(event='SCROLL')
    clickEvent = EventsLog.objects.all().filter(event='click')
    starEvent = EventsLog.objects.all().filter(event='click_star')

    hv = hoverEvent.filter(username=request.user.username).__len__()

    mm = mouseMoveEvent.filter(username=request.user.username).__len__()

    sc = scrollEvent.filter(username=request.user.username).__len__()

    cl = clickEvent.filter(username=request.user.username).__len__()

    st = starEvent.filter(username=request.user.username).__len__()

    lst = [['Event Name' , 'Count'],
           ['hover', hv],
           ['MouseMove', mm],
           ['Scroll',sc],
           ['Click',cl],
           ['Star Click',st]
    ]

   # print(lst)

    data = json.dumps(lst,cls= DjangoJSONEncoder)
    return data




def viz2(request):

    # hoverEvent=EventsLog.objects.all().filter(event='hover')
    # mouseMoveEvent = EventsLog.objects.all().filter(event='MouseMove')
    # scrollEvent = EventsLog.objects.all().filter(event='SCROLL')
    clickEvent = EventsLog.objects.all().filter(event='click').filter(username=request.user.username)
    starEvent = EventsLog.objects.all().filter(event='click_star').filter(username=request.user.username)

    incr = 8
    lst_mrng = list([['Event Name' , 'Count']])
    lst_day = list([['Event Name' , 'Count']])
    lst_even = list([['Event Name' , 'Count']])
    lst_tot = list([['Event Name' , 'Count']])
    for i in range(0,24,incr):
        count_cl = 0
        count_st = 0
        tmplist = list()
        for j in range(i, i+incr):
            count_cl += len(clickEvent.filter(currentTime__hour=j))
            count_st += len(starEvent.filter(currentTime__hour=j))


        if i == 0:
            lst_mrng.append(['click', count_cl])
            lst_mrng.append(['star', count_st])
            lst_tot.append(['morning', count_cl+count_st])
        elif i ==8:
            lst_day.append(['click', count_cl])
            lst_day.append(['star', count_st])
            lst_tot.append(['day', count_cl+count_st])
        elif i ==16:
            lst_even.append(['click', count_cl])
            lst_even.append(['star', count_st])
            lst_tot.append(['evening', count_cl+count_st])

    lst_mrng = json.dumps(lst_mrng,cls= DjangoJSONEncoder)
    lst_day = json.dumps(lst_day,cls= DjangoJSONEncoder)
    lst_even = json.dumps(lst_even,cls= DjangoJSONEncoder)
    lst_tot = json.dumps(lst_tot,cls= DjangoJSONEncoder)

    #print(lst_mrng)
    #print(lst_day)
    #print(lst_even)
    #print(lst_tot)

    # data = "xxx"

    # print(data)
    return lst_tot, lst_mrng, lst_day,lst_even



