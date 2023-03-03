from django.shortcuts import render


def handler_400(request, exception):
    return render(request, "exceptions/400.html")


def handler_403(request, exception):
    return render(request, "exceptions/403.html")


def hander_404(request, exception):
    return render(request, "exceptions/404.html")


def handler_500(request, exception):
    return render(request, "exceptions/500.html")
