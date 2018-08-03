from django.urls import path
from .views import home, my_logout
from .views import listar_categoria, nova_categoria, alterar_categoria, mostrar_categoria
from .views import listar_reserva, nova_reserva


urlpatterns = [
    # path('list/', persons_list, name="person_list"),
    # path('new/', persons_new, name="person_new"),
    # path('update/<int:id>/', persons_update, name="persons_update"),
    # path('delete/<int:id>/', persons_delete, name="persons_delete"),

    path('', home, name='home'),
    path('logout/', my_logout, name='logout'),
    path('reserva/', listar_reserva, name="listar_reserva"),
    path('reserva/cadastrar/', nova_reserva, name="cadastrar_reserva"),
    path('categoria/', listar_categoria, name="listar_categoria"),
    path('categoria/cadastrar/', nova_categoria, name="cadastrar_categoria"),
    path('categoria/alterar/<int:id>/', alterar_categoria, name="alterar_categoria"),
    path('categoria/mostrar/<int:id>/', mostrar_categoria, name="mostrar_categoria"),
]