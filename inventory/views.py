from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeviceRepair
from .forms import RepairForm

def repair_form_view(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inventory/success.html')
    else:
        form = RepairForm()
    return render(request, 'inventory/index.html', {'form': form})

@login_required(login_url='/login/')
def dashboard_view(request):
    repairs = DeviceRepair.objects.all().order_by('-created_at')
    return render(request, 'inventory/dashboard.html', {'repairs': repairs})