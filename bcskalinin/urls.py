from django.contrib import admin
from django.urls import path
from block.views import BlockListView, BlockView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlockListView.as_view()),
    path('blocks/<int:height>/', BlockView.as_view()),
]
