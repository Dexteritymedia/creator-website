import random
import json

from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Q

from .forms import *
from .models import *
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDER_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def homepage(request):
    return render(request, 'app/search.html')
            
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)

            contact.ip_address = get_client_ip(request)
            contact.date_submitted = timezone.now()
            contact.save()
            messages.success(request, 'Your message has been submitted successfully!')
            return JsonResponse({'status': 'success', 'message': 'Your message has been submitted successfully!'})
        else:
            print("Form errors", form.errors)
            messages.error(request, 'There was an error with your submission')
            return JsonResponse({'status': 'error', 'errors': 'There was an error with your submission!'})
    else:
        form = ContactForm()
    return form


def index(request):
    form = contact_view(request)
    content = Content.objects.all()
    faqs = FAQ.objects.all()
    works = WorkHistory.objects.filter(accept=True)
    try:
        creator_detail = CreatorDetail.objects.get()
    except ObjectDoesNotExist:
        creator_detail = None
    context = {
        'form': form,
        'content': creator_detail,
        'creator_contents': content,
        'faqs': faqs,
        'works': works,
    }
    return render(request, 'app/index.html', context)


def add_review(request):
    if request.method == 'POST':
        form = WorkHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            messages.success(request, 'Your review has been submitted successfully!')
            return redirect('/')
        else:
            print("Form errors", form.errors)
            messages.error(request, 'There was an error with your submission')
            return render(request, 'app/add_review.html', {'form':form})
    else:
        form = WorkHistoryForm()
    return render(request, 'app/add_review.html', {'form':form})


def budget_view(request):
    if request.method == "POST":
        form  = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.cleaned_data['budget']
            selected_categories = form.cleaned_data['categories']
            print(list(selected_categories))
            include_accommodation = form.cleaned_data['include_accommodation']
            print(include_accommodation)
            activities = Activity.objects.filter(cost__lte=budget)

            if include_accommodation:
                #filter_items = ['stay'] + selected_categories
                print(filter_items)
                activities = activities.filter(category__in=filter_items)
                activities = list(activities)
                random.shuffle(activities)
            else:
                activities = activities.filter(category__in=selected_categories)
                activities = list(activities)
                random.shuffle(activities)
                


            """
            selected_activities = []
            total_cost = 0
            for activity in activities:
                if total_cost + activity.cost <= budget:
                    selected_activities.append(activity)
                    total_cost += activity.cost

            context = {
                'activities': selected_activities,
                'total_cost': total_cost,
                'form': form,
            }
            return render(request, 'app/budget_activities.html', context)
            """
   
            activities_including_accommodation = []
            selected_activities = []
            total_cost = 0
            for activity in activities:
                if activity.category.name.lower() in ['stay'] and include_accommodation:
                    if total_cost + activity.cost <= budget:
                        activities_including_accommodation.append(activity)
                        total_cost += activity.cost
                else:
                    if total_cost + activity.cost <= budget:
                        selected_activities.append(activity)
                        total_cost += activity.cost
                    
            context = {
                'accommodation_activities': activities_including_accommodation,
                'activities': selected_activities,
                'total_cost': total_cost,
                'form': form,
            }
            return render(request, 'app/budget_activities_accommodation.html', context)
            

            if request.user.is_authenticated and 'save' in request.POST:
                saved_view = SavedBudget.objects.create(user=request.user, budget=budget)
                saved_view.activities.set(activities)
                saved_view.save()
                return redirect('')
    else:
        form = BudgetForm()
    return render(request, 'app/budget_form.html', {'form': form})

def activities(request):
    """Render the mood matrix page"""
    return render(request, 'app/activities_page.html')

def get_suggestions(request):
    """API endpoint to get activity suggestions based on mood"""
    if request.method == 'GET':
        # Get parameters from request
        energy = int(request.GET.get('energy', 50))
        stress = int(request.GET.get('stress', 50))
        budget = float(request.GET.get('budget', 50))
        time = int(request.GET.get('time', 60))
        
        # Calculate energy and stress ranges (±20 points from input)
        energy_min = max(0, energy - 20)
        energy_max = min(100, energy + 20)
        stress_min = max(0, stress - 20)
        stress_max = min(100, stress + 20)
        
        # Query activities that match the criteria
        activities = Activity.objects.filter(
            Q(energy_level__gte=energy_min) &
            Q(energy_level__lte=energy_max) &
            Q(stress_level__gte=stress_min) &
            Q(stress_level__lte=stress_max) &
            Q(cost__lte=budget)
        ).order_by('?')[:3]  # Randomly select 3 matching activities
        
        # Format activities for response
        activities_data = [{
            'name': activity.name,
            'price': float(activity.price),
            #'duration': activity.duration_minutes,
            'location': activity.location,
            'category': activity.category.name
        } for activity in activities]
        
        return JsonResponse({
            'success': True,
            'activities': activities_data
        })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
