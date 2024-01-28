from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from .models import Meme


def meme_list(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Meme.objects.order_by('-uploaded_at'), 10)
    try:
        memes = paginator.page(page)
    except PageNotAnInteger:
        memes = paginator.page(1)
    except EmptyPage:
        memes = paginator.page(paginator.num_pages)

    return render(request, 'memes/meme_list.html', {'memes': memes})


def load_more_memes(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Meme.objects.order_by('-uploaded_at'), 10)

    try:
        memes = paginator.page(page)
    except EmptyPage:
        return JsonResponse({'has_next': False})

    memes_data = [{'template': meme.template, 'text': meme.text, 'media_file': meme.media_file.url} for meme in memes]

    return JsonResponse({'memes': memes_data, 'has_next': memes.has_next()})
