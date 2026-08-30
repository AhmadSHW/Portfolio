from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .models import Profile, Skill, Project
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully! I'll get back to you soon. ✅")
            return redirect(reverse('home') + '#contact')
        else:
            messages.error(request, "There was an error with the form. Please check all required fields.")
    else:
        form = ContactForm()

    profile = Profile.objects.first()

    skills = Skill.objects.all()
    skills_by_category = {}
    for choice_key, choice_label in Skill.CATEGORY_CHOICES:
        category_skills = skills.filter(category=choice_key)
        if category_skills.exists():
            skills_by_category[choice_label] = category_skills

    projects = Project.objects.all()

    context = {
        'profile': profile,
        'skills_by_category': skills_by_category,
        'projects': projects,
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)