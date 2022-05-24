from django.urls import re_path as url
from . import views

urlpatterns=[
    url(r'^$',views.news_today,name = 'newsToday'),
    # url('^today/$',views.news_of_day,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/',view.search_results,name='search_results')
]