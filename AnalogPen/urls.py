
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('home/', home_views.home, name='home-page'),
    path('', home_views.home, name='home-page'),
    path('livetext/', home_views.live_text, name='livetext-page'),
    path('textdocument/', home_views.doc_text, name='doc-page'),
    path('textdocument2/', home_views.doc_text2, name='doc-page'),
]
