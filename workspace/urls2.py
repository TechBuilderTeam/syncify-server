from django.urls import path
from .views2 import *


urlpatterns = [
    path('members/add/', AddMember.as_view(), name='add-member'),
    path('members/remove/', RemoveMember.as_view(), name='remove-member'),
    path('members/change-role/', ChangeRole.as_view(), name='change-role'),
    path('<int:workspace_id>/members/', WorkspaceMembersList.as_view(), name='workspace-members-list'),
    path('member/acivate/<uid64>/<token>/',ActivateMemberView.as_view(),name='active_member'),
    path('task/update-status/',ChangeStatusView.as_view(),name='change_task_status'),
    path('<int:pk>/details/',WorkSpaceDetailView.as_view(),name='workspace-details'),
]
