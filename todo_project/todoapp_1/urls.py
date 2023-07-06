from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'todoapp_1'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('yes/<int:id>', views.y, name='y'),
    path('update/<int:id>', views.update, name='update'),

    path('c-home/', views.TodoListView.as_view(), name='c-home'),
    path('c-detail/<int:pk>/', views.TodoDetailView.as_view(), name='c-details'),
    path('c-update/<int:pk>/', views.TodoUpdateView.as_view(), name='c-update'),
    path('c-delete/<int:pk>/', views.TodoDeleteView.as_view(), name='c-delete'),
    #path('c-yes/<int:pk>/', views.Y.as_view(), name='y'),


    ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
