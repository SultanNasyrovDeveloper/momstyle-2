from .models import SiteMain


def main(request):
    if SiteMain.objects.count() > 0:
        main = SiteMain.objects.get()
    else:
        main = {}
    return {'main': main}
