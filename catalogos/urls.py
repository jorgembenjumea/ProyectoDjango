from django.urls import path
from catalogos.views import CategoriaView, ProcesosPlantaView, CategoriaNew, CategoriaEdit, CategoriaDel,\
categoria_print, ProcesosPlantaNew, ProcesosPlantaEdit, ProcesosPlantaDel
urlpatterns = [
    path('categorias', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new' ),
    path('categoria/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_delete'),
   
	path('ProcesosPlanta', ProcesosPlantaView.as_view(), name='ProcesosPlanta_list'),
	path('ProcesosPlanta/new', ProcesosPlantaNew.as_view(), name='ProcesosPlanta_new'),
	path('ProcesosPlanta/edit/<int:pk>', ProcesosPlantaEdit.as_view(), name='ProcesosPlanta_edit'),
    path('ProcesosPlanta/delete/<int:pk>', ProcesosPlantaDel.as_view(), name='ProcesosPlanta_delete'),
   
 	path('categoria/print',categoria_print, name='categoria_print'),
    path('categoria/print/<int:pk>',categoria_print, name='categoria_print_one'),
	


]

