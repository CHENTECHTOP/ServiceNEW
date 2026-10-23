from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeviceRepair, Review
from .forms import RepairForm, ReviewForm


def repair_form_view(request):
    if request.method == 'POST':
        if 'submit_repair' in request.POST:
            form = RepairForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'inventory/success.html')
        elif 'submit_review' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()
                return redirect('repair_form')

    form = RepairForm()
    review_form = ReviewForm()
    reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'inventory/index.html', {
        'form': form,
        'review_form': review_form,
        'reviews': reviews
    })


@login_required(login_url='/login/')
def dashboard_view(request):
    repairs = DeviceRepair.objects.all().order_by('-created_at')
    return render(request, 'inventory/dashboard.html', {'repairs': repairs})