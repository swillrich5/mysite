from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', view.post_list, name='post_list')
    path('<int:id>/', view.post_detail, name='post_detail')
]