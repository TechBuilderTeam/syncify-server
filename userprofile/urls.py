from django.urls import path 
from .views import *

urlpatterns = [
    path('contact/',UserContactView.as_view(),name='user_contact'),
    path('about/',UserAboutView.as_view(),name='user_about'),
    path('portfolio/',UserPortfolioView.as_view(),name='user_portfolio'),
    path('education/create/',UserEducationCreateView.as_view(),name='user_educreate'), 
    path('education/edit/<int:pk>/',UserEducationUpdateView.as_view(),name='user_education_edit'),
    path('education/delete/<int:pk>/',UserEducationDeleteView.as_view(),name='user_education_delete'),
    path('education/<int:user_id>/',UserEducationListView.as_view(),name='user_education_list'),
]
