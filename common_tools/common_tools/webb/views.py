import random

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from common_tools.webb.models import Profile

'''
    @cache_page(15 * 60 * 60) - 15 hours
    @cache_page(15 * 60) - 15 minutes
'''


# @cache_page(15)
# def show_index(request):
#     context = {
#         'value': random.randint(1, 1024),
#     }
#
#     return render(request, 'index.html', context)


def show_index(request):
    Profile.objects.create(
        name='Lubo',
        email='lubo@istrev.tg',
    )

    profiles = Profile.objects.all()

    if not cache.get('value2'):
        cache.set('value2', random.randint(1, 1024), 30)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    paginator = Paginator(profiles, per_page=5)

    context = {
        'value': random.randint(1, 1024),
        'value2': cache.get('value2'),
        'count': request.session.get('count'),
        'profiles': profiles,
        'profiles_page': paginator.get_page(1),
    }

    return render(request, 'index.html', context)


# def show_book_details(request, pk):
#     request.session['last_viewed_book_id'] = pk


def show_book_details(request, pk):
    last_viewed = request.session.get('last_viewed_books', [])
    last_viewed.append(pk)

    request.session['last_viewed_book'] = last_viewed
