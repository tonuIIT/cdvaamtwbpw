from django.urls import path


from . views import (
    EventDashboardView,
    EventCreateView,
    EventListView,
    EventDetailView,
    OrganizerProfileVew,
    EventTrainerCreateView,
    # EventParticipantCreateView,
    EventDetailUpdateView,
    EventDeleteView,
)

urlpatterns = [
    path('', EventDashboardView.as_view(), name='dashboard'),
    path('profile/', OrganizerProfileVew.as_view(), name="organizer_profile"),
    path('event_create/', EventCreateView.as_view(), name="event_create"),
    path('event_trainer/', EventTrainerCreateView.as_view(), name="event_trainer"),
    # path('event_participant/', EventParticipantCreateView.as_view(), name="event_participant"),
    path('event_list/', EventListView.as_view(), name="event_list"),
    path('<slug:slug>/', EventDetailView.as_view(), name="detail"),
    path('<slug:slug>/update/', EventDetailUpdateView.as_view(), name="event_detail"),
    path('delete/<slug:slug>', EventDeleteView.as_view(), name="event_delete"),

]