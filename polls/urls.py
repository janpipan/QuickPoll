from django.urls import path

from .views import CreatePollView, ResultsView, VoteView, PollsView

urlpatterns = [
    path('create/', CreatePollView.as_view(), name="createPoll"),
    path('results/<int:pk>', ResultsView.as_view(), name="results"),
    path('vote/<int:pk>', VoteView.as_view(), name="vote"),
    path('polls', PollsView.as_view(), name="polls")
]