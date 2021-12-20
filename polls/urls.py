from django.urls import path

from .views import CreatePollView, ResultsView, VoteView, PollsView

urlpatterns = [
    path('create/', CreatePollView.as_view(), name="createPoll"),
    path('<int:pk>/results', ResultsView.as_view(), name="results"),
    path('<int:pk>', VoteView.as_view(), name="vote"),
    path('polls', PollsView.as_view(), name="polls")
]