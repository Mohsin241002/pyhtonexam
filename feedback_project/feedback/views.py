# feedback/views.py

from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # If the form is valid, display a thank you message
            thank_you_message = "Thank you for your feedback!"
            return render(request, 'feedback/feedback_form.html', {'form': form, 'thank_you_message': thank_you_message})

    return render(request, 'feedback/feedback_form.html', {'form': form})
