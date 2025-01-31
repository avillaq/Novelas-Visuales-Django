from django.urls import path
from VNDisplay.views import home, directory, novel_detail, android, android_apk, android_kirikiroid2, search, update_novels

app_name = 'VNDisplay'
urlpatterns = [
    path('', view=home, name='home'),
    path('directorio', view=directory, name='directory'),
    path('search', view=search, name='search'),
    path('android', view=android, name='android'),
    path('android/apk', view=android_apk, name='android_apk'),
    path('android/kirikiroid2', view=android_kirikiroid2, name='android_kirikiroid2'),
    path('update/', view=update_novels, name='update_novels'),


    path('novel/<str:id_post>/', novel_detail, name='novel_detail'),
]