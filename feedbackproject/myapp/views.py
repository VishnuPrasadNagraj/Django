from django.shortcuts import render
from myapp.forms import FeedBackForm

# Create your views here.
def FeedBackView(request):
    if request.method == "POST":
        f = FeedBackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            rollno = f.cleaned_data['rollno']
            email = f.cleaned_data['email']
            feedback = f.cleaned_data['feedback']

            # Pass data to thank-you page
            context = {
                'name': name,
                'rollno': rollno,
                'email': email,
                'feedback': feedback
            }
            return render(request, 'myapp/output.html', context)
    else:
        f = FeedBackForm()

    # Show the form page initially
    return render(request, 'myapp/input.html', {'form': f})
