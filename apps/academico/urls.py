from django.urls import path, include
from .views import *

urlpatterns = [
	path('',academico, name = 'academico'),
	#path('nuevoinscrito/',inscrito_view, name = 'nuevoinscrito'),
	path('listarinscrito',inscritoList.as_view(), name = 'inscrito_listar'),
	path('nuevoinscrito',inscritoCreate.as_view(), name= 'inscrito_crear'),
	path('editarinscrito/<pk>',inscritoUpdate.as_view(), name='inscrito_editar'),
	path('eliminarinscrito/<pk>',inscritoDelete.as_view(), name='inscrito_eliminar'),
	path('listarcurso',cursoList.as_view(), name='curso_listar'),
	path('nuevocurso',cursoCreate.as_view(), name= 'curso_crear'),
	path('editarcurso/<pk>',cursoUpdate.as_view(), name='curso_editar'),
	path('eliminarcurso/<pk>',cursoDelete.as_view(), name='curso_eliminar'),
	path('listarugel',ugelList.as_view(), name='ugel_listar'),
	path('nuevougel',ugelCreate.as_view(), name= 'ugel_crear'),
	path('editarugel/<pk>',ugelUpdate.as_view(), name='ugel_editar'),
	path('eliminarugel/<pk>',ugelDelete.as_view(), name='ugel_eliminar'),
	path('listarmatricula',matriculaList.as_view(), name='matricula_listar'),
	path('nuevomatricula',matriculaCreate.as_view(), name= 'matricula_crear'),
	path('editarmatricula/<pk>',matriculaUpdate.as_view(), name='matricula_editar'),
	path('eliminarmatricula/<pk>',matriculaDelete.as_view(), name='matricula_eliminar'),
	# path('editarinscrito/<int:id_inscrito>/',inscrito_edit, name = 'inscrito_editar'),
	#path('eliminarinscrito/<int:id_inscrito>/',inscrito_delete, name = 'inscrito_eliminar'),
	#path('nuevaugel/',ugel_view, name = 'nuevaugel'),
	#path('ugel/',views.ugel_list, name = 'ugel'),
	#path('editarugel/<int:id_ugel>/',ugel_edit, name = 'ugel_editar'),
	#path('eliminarugel/<int:id_ugel>/',ugel_delete, name = 'ugel_eliminar'),
	#path('nuevocurso/',curso_view, name = 'nuevocurso'),
	#path('curso/',curso_list, name = 'curso'),
	#path('editarcurso/<int:id_curso>/',curso_edit, name = 'curso_editar'),
	#path('eliminarcurso/<int:id_curso>/',curso_delete, name = 'curso_eliminar'),
	
]
