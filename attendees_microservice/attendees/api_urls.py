from django.urls import path

from .api_views import api_list_attendees, api_show_attendee

urlpatterns = [
    path(
        "conferences/<int:conference_vo_id>/attendees/",
        api_list_attendees,
        name="api_list_attendees",
    ),
    path("attendees/<int:id>/", api_show_attendee, name="api_show_attendee"),
    path("attendees/", api_list_attendees, name="api_create_attendees"),
]
