from django.urls import path
from catalogos.views import CategoriaView, ProcesosPlantaView, CategoriaNew, CategoriaEdit, CategoriaDel,\
categoria_print, ProcesosPlantaNew, ProcesosPlantaEdit, ProcesosPlantaDel, OperacionDiariaView,\
OperacionDiariaNew, OperacionDiariaEdit, OperacionDiariaDel, ControlSulfatoView,\
ControlSulfatoNew, ControlSulfatoEdit, ControlSulfatoDel

urlpatterns = [
    path('categorias', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new' ),
    path('categoria/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_delete'),
   
    path('ProcesosPlanta', ProcesosPlantaView.as_view(), name='ProcesosPlanta_list'),
    path('ProcesosPlanta/new', ProcesosPlantaNew.as_view(), name='ProcesosPlanta_new'),
    path('ProcesosPlanta/edit/<int:pk>', ProcesosPlantaEdit.as_view(), name='ProcesosPlanta_edit'),
    path('ProcesosPlanta/delete/<int:pk>', ProcesosPlantaDel.as_view(), name='ProcesosPlanta_delete'),
   

    path('OperacionDiaria', OperacionDiariaView.as_view(), name='OperacionDiaria_list'),
    path('OperacionDiaria/new', OperacionDiariaNew.as_view(), name='OperacionDiaria_new' ),
    path('OperacionDiaria/edit/<int:pk>', OperacionDiariaEdit.as_view(), name='OperacionDiaria_edit'),
    path('OperacionDiaria/delete/<int:pk>', OperacionDiariaDel.as_view(), name='OperacionDiaria_delete'),

    path('ControlSulfato', ControlSulfatoView.as_view(), name='ControlSulfato_list'),
    path('ControlSulfato/new', ControlSulfatoNew.as_view(), name='ControlSulfato_new' ),
    path('ControlSulfato/edit/<int:pk>', ControlSulfatoEdit.as_view(), name='ControlSulfato_edit'),
    path('ControlSulfato/delete/<int:pk>', ControlSulfatoDel.as_view(), name='ControlSulfato_delete'),





    path('categoria/print',categoria_print, name='categoria_print'),
    path('categoria/print/<int:pk>',categoria_print, name='categoria_print_one'),
    


]

