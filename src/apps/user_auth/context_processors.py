from .forms import SignInForm


def get_context(request):
    """Context available for all applications"""
    context = {
        "login_ajax": SignInForm(),
    }

    return context
