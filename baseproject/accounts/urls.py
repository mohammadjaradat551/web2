from django.urls import path
from .views import *


app_name = 'accounts'

urlpatterns = [
    path('signup', signup, name= 'signup'),
    path('login/', sign_in, name='login'),

    path('profile/', profile, name= 'profile'),
    path('profile/reservations', my_reservations, name= 'my_reservation'),
    path('profile/listing', my_listing, name= 'my_listing'),
    path('profile/edit', edit_profile, name= 'edit_profile'),

]