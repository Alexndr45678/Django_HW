from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)


def log(view_func):
    def wrapper(request):
        logger.info(f"The view function was called {view_func.__name__}")
        return view_func(request)

    return wrapper


@log
def main(request):
    logger.info("Main page accessed")
    return HttpResponse("My first site")


@log
def about(request):
    logger.info("About page accessed.")
    return HttpResponse("This page contain info about me.")
