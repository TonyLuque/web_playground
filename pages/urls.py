from django.urls import path
from.views import PagesListView, PageDetailView, Pagecreate

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
    path('create/', Pagecreate.as_view(), name="create"),
], 'pages')