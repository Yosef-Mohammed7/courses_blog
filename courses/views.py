
'''from django.shortcuts import render,get_object_or_404
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
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from memberships.models import UserMembership
from .models import Course, Lesson


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class LessonDetailView(LoginRequiredMixin, View):

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        user_membership = get_object_or_404(UserMembership, user=request.user)
       
        user_membership_type = user_membership.membership.membership_type
        course_allowed_mem_types = course.allowed_memberships.all()
        context = { 'object': None }
        if course_allowed_mem_types.filter(membership_type=user_membership_type).exists():
            context = {'object': lesson}
        return render(request, "courses/lesson_detail.html", context)
