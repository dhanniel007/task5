from django.urls import path
from .views import watercurls, bonestraight, pinkycurls, products

urlpatterns = [
    path('watercurls', watercurls),
    path('bonestraight', bonestraight),
    path('pinkycurls', pinkycurls),
    path('', products)
    
]
