from django.contrib import admin
from django.urls import path
from learn import views as learn_views  # new
admin.autodiscover()
urlpatterns = [
    path('', learn_views.index),  # new
    path('admin/', admin.site.urls),
]