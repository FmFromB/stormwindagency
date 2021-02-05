from django.urls import path, include
from .views import *

urlpatterns = [

    #home urls
    path('', HomeListView.as_view(), name='home'),

    #Property urls
    path('properties', PropertyListView.as_view(), name='properties'),
    path('detail_property/<int:pk>', PropertyDetailView.as_view(), name='detail_property_page'),
    path('add_property', PropertyCreateView.as_view(), name='add_property'),
    path('update_property/<int:pk>', PropertyUpdateView.as_view(), name='update_property'),
    path('delete_property/<int:pk>', PropertyDeleteView.as_view(), name='delete_property'),

    #offer urls
    path('offers', OffersListView.as_view(), name='offers'),
    path('detail/<int:pk>', OffersDetailView.as_view(), name='detail_page'),
    path('add_offer', OfferCreateView.as_view(), name='add_offer'),
    path('update_offer/<int:pk>', OfferUpdateView.as_view(), name='update_offer'),
    path('delete_offer/<int:pk>', OfferDeleteView.as_view(), name='delete_offer'),
    
    #reqs urls
    path('reqs', ReqsListView.as_view(), name='reqs'),
    path('detail_req/<int:pk>', ReqsDetailView.as_view(), name='detail_req_page'),
    path('add_req', ReqsCreateView.as_view(), name='add_req'),
    path('update_req/<int:pk>', ReqsUpdateView.as_view(), name='update_req'),
    path('delete_req/<int:pk>', ReqsDeleteView.as_view(), name='delete_req'),

    #client urls
    path('clients', СlientListView.as_view(), name='clients'),
    path('detail_client/<int:pk>', ClientsDetailView.as_view(), name='detail_client_page'),
    path('add_client', ClientCreateView.as_view(), name='add_client'),
    path('update_client/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    #Deal urls
    path('deals', DealListView.as_view(), name='deals'),
    path('detail_deal/<int:pk>', DealDetailView.as_view(), name='detail_deal_page'),
    path('add_deal', DealCreateView.as_view(), name='add_deal'),
    path('update_deal/<int:pk>', DealUpdateView.as_view(), name='update_deal'),
    path('delete_deal/<int:pk>', DealDeleteView.as_view(), name='delete_deal'),

    #Realtor urls
    path('realtors', RealtorListView.as_view(), name='realtors'),
    path('detail_realtor/<int:pk>', RealtorDetailView.as_view(), name='detail_realtor_page'),
    path('add_realtor', RealtorCreateView.as_view(), name='add_realtor'),
    path('update_realtor/<int:pk>', RealtorUpdateView.as_view(), name='update_realtor'),
    path('delete_realtor/<int:pk>', RealtorDeleteView.as_view(), name='delete_realtor'),

    #login/logout urls
    path('login_page', StormwindLoginView.as_view(), name='login_page'),
    path('register_page', RegisterUserView.as_view(), name='register_page'),
    path('logout_page', StormwindLogoutView.as_view(), name='logout_page'),

 

]
