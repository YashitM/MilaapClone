from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cause
from .forms import FundForm


def index(request):
    causes = Cause.objects.all()
    return render(request, 'website/index.html', {'causes': causes})


def show_details(request, item_id):
    current_cause = Cause.objects.get(pk=item_id)
    funded_amount = current_cause.already_funded

    response = {"current_cause": current_cause}
    if request.method == 'POST':
        form = FundForm(request.POST)  # create form object
        if form.is_valid():
            amount = form.cleaned_data['fund_amount']
            current_cause.already_funded = funded_amount + amount
            current_cause.save()
            return render(request, 'website/details.html', response)
    return render(request, 'website/details.html', response)
