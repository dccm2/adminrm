from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InscritoForm, UgelForm, CursoForm, MatriculaForm
from .models import Inscrito, Ugel, Curso, Matricula
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def academico(request):
	return render(request,'academico/index.html')


"""def inscrito_view(request):
	if request.method == 'POST':
		form = InscritoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('inscrito')
	else:
		form = InscritoForm()

	return render (request, 'academico/inscrito_form.html',{'form':form})


def inscrito_list(request):
	inscrito = Inscrito.objects.all().order_by('id')
	contexto = {'inscritos': inscrito}
	return render (request, 'academico/inscrito.html',contexto)


def inscrito_edit(request, id_inscrito):
	inscrito = Inscrito.objects.get(id = id_inscrito)
	if request.method == 'GET':
		form = InscritoForm(instance=inscrito)
	else:
		form = InscritoForm(request.POST, instance=inscrito)
		if form.is_valid():
			form.save()
		return redirect('inscrito')
	return render(request, 'academico/inscrito_form.html',{'form':form})

def inscrito_delete(request,id_inscrito):
	inscrito = Inscrito.objects.get(id=id_inscrito)
	if request.method=='POST':
		inscrito.delete()
		return redirect('inscrito')
	return render(request, 'academico/inscrito_del.html',{'inscrito': inscrito})


def ugel_view(request):
	if request.method == 'POST':
		form = UgelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('academico')
	else:
		form = UgelForm()

	return render (request, 'academico/ugel_form.html',{'form':form})


def ugel_list(request):
	ugel = Ugel.objects.all().order_by('id')
	contexto = {'ugels': ugel}
	return render (request, 'academico/ugel.html',contexto)


def ugel_edit(request, id_ugel):
	ugel = Ugel.objects.get(id = id_ugel)
	if request.method == 'GET':
		form = UgelForm(instance=ugel)
	else:
		form = UgelForm(request.POST, instance=ugel)
		if form.is_valid():
			form.save()
		return redirect('ugel')
	return render(request, 'academico/ugel_form.html',{'form':form})

def ugel_delete(request,id_ugel):
	ugel = Ugel.objects.get(id=id_inscrito)
	if request.method=='POST':
		ugel.delete()
		return redirect('ugel')
	return render(request, 'academico/ugel_del.html',{'ugel': ugel})

def curso_view(request):
	if request.method == 'POST':
		form = CursoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('academico')
	else:
		form = CursoForm()

	return render (request, 'academico/curso_form.html',{'form':form})


def curso_list(request):
	curso = Curso.objects.all().order_by('id')
	contexto = {'cursos': curso}
	return render (request, 'academico/curso.html',contexto)


def curso_edit(request, id_curso):
	curso = Curso.objects.get(id = id_curso)
	if request.method == 'GET':
		form = CursoForm(instance=curso)
	else:
		form = CursoForm(request.POST, instance=curso)
		if form.is_valid():
			form.save()
		return redirect('curso')
	return render(request, 'academico/curso_form.html',{'form':form})

def curso_delete(request,id_curso):
	curso = Curso.objects.get(id=id_curso)
	if request.method=='POST':
		curso.delete()
		return redirect('curso')
	return render(request, 'academico/curso_del.html',{'curso': curso})


def busqueda(self):
	q = request.GET.get('q','')
	querys = (Q())"""

class inscritoList(ListView):
	model = Inscrito
	template_name = 'academico/inscrito.html'

class inscritoCreate(CreateView):
	model = Inscrito
	form_class = InscritoForm
	template_name = 'academico/inscrito_form.html'
	success_url = reverse_lazy('inscrito_listar')

class inscritoUpdate(UpdateView):
	model = Inscrito
	form_class = InscritoForm
	template_name = 'academico/inscrito_form.html'
	success_url = reverse_lazy('inscrito_listar')

class inscritoDelete(DeleteView):
	model = Inscrito
	form_class = InscritoForm
	template_name = 'academico/inscrito_del.html'
	success_url = reverse_lazy('inscrito_listar')


class cursoList(ListView):
	model = Curso
	template_name = 'academico/curso.html'

class cursoCreate(CreateView):
	model = Curso
	form_class = CursoForm
	template_name = 'academico/curso_form.html'
	success_url = reverse_lazy('curso_listar')

class cursoUpdate(UpdateView):
	model = Curso
	form_class = CursoForm
	template_name = 'academico/curso_form.html'
	success_url = reverse_lazy('curso_listar')

class cursoDelete(DeleteView):
	model = Curso
	form_class = CursoForm
	template_name = 'academico/curso_del.html'
	success_url = reverse_lazy('curso_listar')

class ugelList(ListView):
	model = Ugel
	template_name = 'academico/ugel.html'

class ugelCreate(CreateView):
	model = Ugel
	form_class = UgelForm
	template_name = 'academico/ugel_form.html'
	success_url = reverse_lazy('ugel_listar')

class ugelUpdate(UpdateView):
	model = Ugel
	form_class = UgelForm
	template_name = 'academico/ugel_form.html'
	success_url = reverse_lazy('ugel_listar')

class ugelDelete(DeleteView):
	model = Ugel
	form_class = UgelForm
	template_name = 'academico/ugel_del.html'
	success_url = reverse_lazy('ugel_listar')

class matriculaList(ListView):
	model = Matricula
	template_name = 'academico/matricula.html'

class matriculaCreate(CreateView):
	model = Matricula
	form_class = MatriculaForm
	template_name = 'academico/matricula_form.html'
	success_url = reverse_lazy('matricula_listar')

class matriculaUpdate(UpdateView):
	model = Matricula
	form_class = MatriculaForm
	template_name = 'academico/matricula_form.html'
	success_url = reverse_lazy('matricula_listar')

class matriculaDelete(DeleteView):
	model = Matricula
	form_class = MatriculaForm
	template_name = 'academico/matricula_del.html'
	success_url = reverse_lazy('matricula_listar')

