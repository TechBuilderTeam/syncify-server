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
    path('work/create/',UserWorkCreateView.as_view(),name='user_work_create'), 
    path('work/edit/<int:pk>/',UserWorkUpdateView.as_view(),name='user_Work_edit'),
    path('work/delete/<int:pk>/',UserWorkDeleteView.as_view(),name='user_Work_delete'),
    path('work/<int:user_id>/',UserWorkListView.as_view(),name='user_Work_list'),
    path('skills/add/',UserSkillCreateView.as_view(),name='user_Skill'),
    path('skills/<int:user_id>/',UserSkillListView.as_view(),name='user_SkillList'),
    path('designation/',UserDesignationView.as_view(),name='designation'),
    path('<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
]
