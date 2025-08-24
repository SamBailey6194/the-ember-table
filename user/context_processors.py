from django.urls import reverse


def global_modal_urls(request):
    return {
        'dashboard_url': reverse('user:members_dashboard'),
        'next_url': request.GET.get('next', reverse('user:members_dashboard')),
    }
