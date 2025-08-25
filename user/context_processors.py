from django.urls import reverse


def global_modal_urls(request):
    """
    Add commonly used URLs to the template context for global modal forms.

    This context processor makes the following variables available in all
    templates:
      - ``dashboard_url``: The URL for the members dashboard.
      - ``next_url``: The URL to redirect to after login or form submission.
        Defaults to the members dashboard if no 'next' parameter is provided.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        dict: A dictionary containing ``dashboard_url`` and ``next_url``.
    """
    return {
        'dashboard_url': reverse('user:members_dashboard'),
        'next_url': request.GET.get('next', reverse('user:members_dashboard')),
    }
