from .models import SiteMain, SocialLink


def main(request):
    if SiteMain.objects.count() > 0:
        main = SiteMain.objects.get()
    else:
        main = {}
    return {'main': main}


def social_links(request):
    return {'social_links': SocialLink.objects.filter(active=True)}
