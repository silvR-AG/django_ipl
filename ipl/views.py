from itertools import count
from django.shortcuts import render
from .models import deliveries,matches
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum,Count
from django.urls import reverse

# Create your views here.

def matches_per_year(request):
    result = matches.objects.values('season').annotate(played = Count('season')).order_by('season')
    return render(request, 'ipl/mppy.html', {'result' : result})

def matches_won(request):
    result = matches.objects.values('season','winner').annotate(won = Count('winner')).order_by('season')
    return render(request, 'ipl/mwpy.html', {'result': result})

def extra_runs(request):
    result = deliveries.objects.filter(match_id__season = 2016).values('bowling_team').annotate(er = Sum('extra_runs')).order_by('-er')
    return render(request,'ipl/erc.html',{'result':result})

def econ_bowler(request):
    result = deliveries.objects.filter(match_id__season = 2015).values('bowler').annotate(economy = Sum('total_runs')/Count('over',distinct=True)).order_by('economy')[:10]
    return render(request,'ipl/eb.html',{'result':result})
