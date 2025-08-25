from django.shortcuts import render


# Create your views here.
def home(request):
    """
    Renders the public homepage of the website.

    **Context**
    None

    **Template:**
    :template:`core/home.html`
    """
    return render(request, 'core/home.html')
