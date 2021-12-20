from django.urls import path
from .views import HomePageView
from .views import FeaturesPageView
from .views import WebappPageView
from .views import InboxView
from .views import CreateTaskView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('features/', FeaturesPageView.as_view(), name='features'),
    path('webapp/', WebappPageView.as_view(), name='webapp'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('create_task/', CreateTaskView.as_view(), name='create_task'),
]