from django.urls import path


from common_tools.webb.views import show_index

import common_tools.webb.signals

urlpatterns = (
    path('', show_index, name='index'),
)

