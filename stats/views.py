from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Test
from . import forms
from . import urls
from django.urls import reverse
import numpy as np
from scipy import stats
import scipy.stats as stats
from scipy.stats import ttest_ind, ttest_ind_from_stats
from scipy.special import stdtr
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def basic_home(request):
    return render(request, 'home.html')

@login_required
def all_tests(request):
    all_tests = Test.objects.all().order_by('-created_at')
    return render(request, 'all_tests.html', {'all_tests':all_tests})

@login_required
def my_tests(request):
    my_tests = Test.objects.filter(created_by=request.user)
    return render(request, 'my_tests.html', {'my_tests':my_tests})

@login_required
def new_test(request):
    test = forms.TestForm()
    if request.method == 'POST':
        test = forms.TestForm(request.POST)
        ause = request.POST.get("a_users")
        aconv = request.POST.get("a_conversions")
        buse = request.POST.get("b_users")
        bconv = request.POST.get("b_conversions")
        winner = ""
        if float(aconv) > 0 and float(ause) > 0:
            aconvers = float(aconv)/float(ause)*100
        else:
            aconvers = 0
        if float(bconv) > 0 and float(buse) > 0:
            bconvers = float(bconv)/float(buse)*100
        else:
            bconvers = 0
        if aconvers>bconvers:
            winner = "Control"
        elif aconvers == bconvers:
            winner = "None"
        else:
            winner = "Variant"
        if test.is_valid():
            form = test.save(commit=False)
            form.a_conversionrate = aconvers
            form.b_conversionrate = bconvers
            form.winner = winner
            form.created_by = request.user
            form.save()
            messages.add_message(request, messages.INFO, 'Save Successful.')
            return HttpResponseRedirect(reverse('testform'))
    return render(request, 'new_test.html', {'test':test})

def get_names(request):
    returnname = request.GET.get("name_one")
    #get sample 1
    sample1gen = float(request.GET.get("control_users")) - float(request.GET.get("control_conversions"))
    smp1 = [0]*int(sample1gen)
    smp1 += [1]*int(request.GET.get("control_conversions"))

    #get sample 2
    sample2gen = float(request.GET.get("variant_users")) - float(request.GET.get("variant_conversions"))
    smp2 = [0]*int(sample2gen)
    smp2 += [1]*int(request.GET.get("variant_conversions"))

    sample1 = smp1
    sample2 = smp2
    t_stat, p_val = stats.ttest_ind(sample1, sample2, equal_var=False)
    a = t_stat.tolist()
    t_level = a
    p = p_val.tolist()
    p_level = p
    if p_level <= 0.05:
        sig = 1
        return JsonResponse({"t_stat": t_level, "p_value": p_level, "signif": sig })
    else:
        sig = 0
        return JsonResponse({"t_stat": t_level, "p_value": p_level, "signif": sig })



def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
