from django.urls import path, include
from rest_framework import routers
from .views import *

#* ============= There will be all the routers ========== *#

router = routers.DefaultRouter()

router.register('list' , workSpaceViewSet)
router.register('member' , MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search-member/', search_member, name='search-member'),
# * ================= Work space URLS ================================
    path('userWorkspace/<int:workspace_id>/user/<int:user_id>/is_member/', IsUserMember.as_view(), name='is-user-member'),
    path('singleWorkspace/<int:pk>/', WorkSpaceDetailView.as_view(), name='workspace_detail'),
    path('user/<int:user_id>/workspaces/', UserWorkspaces.as_view(), name='user-workspaces'),
    path('user/<int:user_id>/workspace/<int:workspace_id>/position/', user_position_in_workspace, name='user-position-in-workspace'),
    
# * ================= Members URLS ================================
    path('singleworkspace/<int:workspace_id>/members/', WorkspaceMembersList.as_view(), name='workspace-members'), 
    path('workspace/<int:workspace_id>/members/', WorkspaceMembersList.as_view(), name='workspace-members'),
    
# * ================= Timeline URLS ================================
    path('timelines/create/', TimelineCreateView.as_view(), name='timeline-create'),
    path('timelines/<int:pk>/', TimelineDetailView.as_view(), name='timeline-detail'),
    path('timelines/update/<int:pk>/', TimelineUpdateView.as_view(), name='timeline-update'),
    path('timelines/delete/<int:pk>/', TimelineDeleteView.as_view(), name='timeline-delete'),
    path('timelines/update/status/<int:pk>/', UpdateTimelineStatusView.as_view(), name='update-timeline-status'),
    path('timelines/update/assign/<int:pk>/', TimelineAssignUpdate.as_view(), name='update-timeline-assign'),
    path('singleworkspace/<int:workspace_id>/timelines/list/', WorkspaceTimelinesList.as_view(), name='workspace-timelines'),

# * ================= Scrum URLS ================================
    path('scrum/create/', ScrumCreateAPIView.as_view(), name='create-scrum'),
    path('scrum/<int:pk>/', ScrumRetrieveAPIView.as_view(), name='retrieve-scrum'),
    path('scrum/update/<int:pk>/', ScrumUpdateAPIView.as_view(), name='update-scrum'),
    path('scrum/delete/<int:pk>/', ScrumDeleteAPIView.as_view(), name='delete-scrum'),
    path('timeline/scrum/<int:timeline_id>/', ScrumListByTimelineAPIView.as_view(), name='scrums-by-timeline'),

# * ================= Task URLS ================================
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('scrum/tasks/list/<int:scrum_id>/', ScrumTasksListView.as_view(), name='scrum-tasks'),
    path('task/update/assign/<int:pk>/', TaskUpdateAssignedUserView.as_view(), name='task-update-assign'),
    path('task/update/priority/<int:pk>/', TaskPriorityUpdateView.as_view(), name='task-priority-update'),
    path('task/update/status/<int:pk>/', TaskStatusUpdateView.as_view(), name='task-priority-update'),
    
# * ================= Task Comments URLS ================================
    path('comments/create/', TaskCommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', TaskCommentDetailView.as_view(), name='comment-detail'),
    path('comments/update/<int:pk>/', TaskCommentUpdateView.as_view(), name='comment-update'),
    path('comments/delete/<int:pk>/', TaskCommentDeleteView.as_view(), name='comment-delete'),
    path('singletask/comments/list/<int:task_id>/', task_comments, name='task-comments'),
    
# * ====================== important urls ==================== 
    path('counts/', count_view, name='counts'),
    path('dashbordinfo/<int:workspace_id>/', WorkspaceInfoAPIView.as_view(), name='workspace-info'),

]


