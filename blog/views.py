from django.shortcuts import render, get_object_or_404, Http404, HttpResponse
from django.views.generic import View
from seo.models import SitePageSeo
from .models import Post
import json


class Index(View):

    def get(self, request):
        posts = Post.objects.all()
        seo, _ = SitePageSeo.objects.get_or_create(page_name='О нас')
        context = {'posts': posts, "page_seo": seo}
        return render(request, 'about.html', context)


class PostDetail(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        context = {'post': post}
        return render(request, 'post_detail.html', context)


def like(request):
    if request.method == 'POST' and request.is_ajax():
        post_id = int(request.POST['post_id'])

        def add_like(post_id):
            post = get_object_or_404(Post, id=post_id)
            post.likes_number += 1
            post.save()
            return post.likes_number

        if 'likes' in request.session:

            likes_list = request.session['likes']

            if post_id in request.session['likes']:
                answer = 0
                likes = None
            else:
                likes_list.append(post_id)
                request.session['likes'] = likes_list
                likes = add_like(post_id)
                answer = 1
        else:
            request.session['likes'] = [post_id]
            likes = add_like(post_id)
            answer = 1
        response = {'answer': answer, 'likes': likes}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404

