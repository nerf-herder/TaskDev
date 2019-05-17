from app.models import Task


def getTasks(quad):
    return Task.objects.filter(quad=quad).order_by('ordering')
