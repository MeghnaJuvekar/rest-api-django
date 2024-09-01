from django.urls import path
from . import views
from.views import clientInfo

urlpatterns = [
    # path('', views.apiOverview, name = 'apiOverview'),
    path('', views.listOfAllClients, name = 'clientsList'),
    path('createclient', views.registerClient, name = 'registerClient'),
    
    path('<int:id>', clientInfo.as_view(), name = 'clientsList'),
    path('delete/<int:id>/', views.deleteClient, name='clientdelete'),
    # path('updateclient/<int:id>', clientInfo.as_view(), name = 'updateClient'),
    # path('updateclient/<int:id>', views.updateClient, name = 'updateClient'),
    # path('<int:id>', views.clientInfo, name = 'clientsList'),
    
]