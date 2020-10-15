from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




def courses(request):
    return render(request, 'courses/courses.html', {'title': 'الدورات '})

def about(request):
    return render(request, 'courses/about.html', {'title': 'تواصل معنا '})


def index1(request):
    return render(request, 'courses/index1.html', {'title': 'الرئيسية '})

def single(request):
    return render(request, 'courses/single.html', {'title': 'الدورات '})

