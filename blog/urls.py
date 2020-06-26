from django.urls import path
from . import views

# Se hace lo de app_name por si tenemos alguna vista similar en diferentes apps
# Django sepa a cual acceder mediante al app_name
# en la template debe queda asi:  <a href="{% url 'blog:blog' blog.id %}"><h3>{{ blog.title }}</h3></a>
app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name="blog_home"),
    path('<int:blog_id>/', views.blog, name="blog")
]
