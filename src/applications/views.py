from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import LeaveRequest
from .forms import LeaveRequestForm

# Create your views here.
def applications(request):
    if (request.user.is_admin):
        queryset = LeaveRequest.objects.all()
        req_list = list(queryset)
        return render(request, 'applications/applications_admin.html', {'req': req_list})
    else:
        queryset = LeaveRequest.objects.all().filter(user = request.user)
        req_list = list(queryset)
        return render(request, 'applications/applications.html', {'req': req_list})

def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()

            return redirect('applications')
    else:
        form = LeaveRequestForm()
    return render(request, 'applications/leave_request.html', {'form': form})

def approve(request, pk):
    leave_req = LeaveRequest.objects.get(pk=pk)
    leave_req.status = 'Approved'
    leave_req.save()
    return redirect('applications')

def decline(request, pk):
    leave_req = LeaveRequest.objects.get(pk=pk)
    leave_req.status = 'Declined'
    leave_req.save()
    return redirect('applications')
