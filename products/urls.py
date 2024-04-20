from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views
router = routers.DefaultRouter()

router.register(r'geeks', views.GeeksViewSet)

urlpatterns = [
    path('', views.index,name='home'),
    path('product_list',views.list_products,name='list_product'),
    path('product_details',views.detail_product,name='detail_product'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
