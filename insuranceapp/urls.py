from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_agent/', views.add_agent, name='add_agent'),  # Added trailing slash for consistency
    path('edit_agent/<int:agent_id>/', views.edit_agent, name='edit_agent'),
    path('delete_agent/<int:agent_id>/', views.delete_agent, name='delete_agent'),
    path('add_policy/', views.add_policy, name='add_policy'),  # Added trailing slash for consistency
    path('edit_policy/<int:policy_id>/', views.edit_policy, name='edit_policy'),
    path('delete_policy/<int:policy_id>/', views.delete_policy, name='delete_policy'),
    path('view_agent/<int:agent_id>/', views.view_agent, name='view_agent'),  # Added trailing slash for consistency

    path('agent/', views.agent_dashboard, name='agent_dashboard'),  # Added trailing slash for consistency
    path('add_customer/', views.add_customer, name='add_customer'),  # Added trailing slash for consistency
    path('view_customer/', views.view_customer, name='view_customer'),  # Added trailing slash for consistency
    path('edit_customer/', views.edit_customer, name='edit_customer'),  # Added trailing slash for consistency
    path('delete_customer/', views.delete_customer, name='delete_customer'),  # Added trailing slash for consistency
    path('login/', views.login, name='login'),  # Added trailing slash for consistency
    path('register/', views.register, name='register'),  # Added trailing slash for consistency
]
