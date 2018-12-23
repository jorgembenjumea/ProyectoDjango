from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalogos.models import Categoria, ProcesosPlanta, OperacionDiaria, ControlSulfato
from catalogos.forms import CategoriaForm, ProcesosPlantaForm, OperacionDiariaForm, ControlSulfatoForm
from generales.views import SinPrivilegios


class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "catalogos/categoria_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'


class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_categoria"
    model=Categoria
    template_name="catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("catalogos:categoria_list")
    success_message="Control Diario ingresado Satisfactoriamente"
#----Retorne Usuario-----
    def form_valid(self, form):
        form.instance.creadopor =self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_categoria"
    model=Categoria
    template_name="catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("catalogos:categoria_list")
    success_message="El Control Diario se han ingresado Satisfactoriamente"


class CategoriaDel(LoginRequiredMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "catalogos.delete_categoria"
    model=Categoria
    template_name="catalogos/catalogos_del.html"
    context_object_name = 'obj'
    success_url= reverse_lazy("catalogos:categoria_list")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ProcesosPlantaView(LoginRequiredMixin, generic.ListView):
    model = ProcesosPlanta
    template_name = "catalogos/ProcesosPlanta_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'

class ProcesosPlantaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_ProcesosPlanta"
    model=ProcesosPlanta
    template_name="catalogos/ProcesosPlanta_form.html"
    context_object_name = 'obj'
    form_class=ProcesosPlantaForm
    success_url= reverse_lazy("catalogos:ProcesosPlanta_list")
    success_message="Procesos de Planta han ingresado Satisfactoriamente"

class ProcesosPlantaEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_ProcesosPlanta"
    model=ProcesosPlanta
    template_name="catalogos/ProcesosPlanta_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("catalogos:ProcesosPlanta_list")
    success_message="El Proceso de Planta se ha Actualizado Satisfactoriamente"

class ProcesosPlantaDel(LoginRequiredMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "catalogos.delete_ProcesosPlanta"
    model=ProcesosPlanta
    template_name="catalogos/ProcesosPlanta_del.html"
    context_object_name = 'obj'
    success_url= reverse_lazy("catalogos:ProcesosPlanta_list")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class OperacionDiariaView(LoginRequiredMixin, generic.ListView):
    model = OperacionDiaria
    template_name = "catalogos/OperacionDiaria_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'

class OperacionDiariaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_OperacionDiaria"
    model=OperacionDiaria
    template_name="catalogos/OperacionDiaria_form.html"
    context_object_name = 'obj'
    form_class=OperacionDiariaForm
    success_url= reverse_lazy("catalogos:OperacionDiaria_list")
    success_message="Operacion Diaria ingresada Satisfactoriamente"

class OperacionDiariaEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_OperacionDiaria"
    model=OperacionDiaria
    template_name="catalogos/OperacionDiaria_form.html"
    context_object_name = 'obj'
    form_class=OperacionDiariaForm
    success_url= reverse_lazy("catalogos:OperacionDiaria_list")
    success_message="La Operacion Diaria se han actualizado Satisfactoriamente"

class OperacionDiariaDel(LoginRequiredMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "catalogos.delete_OperacionDiaria"
    model=OperacionDiaria
    template_name="catalogos/OperacionDiaria_del.html"
    context_object_name = 'obj' 
    success_url= reverse_lazy("catalogos:OperacionDiaria_list")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ControlSulfatoView(LoginRequiredMixin, generic.ListView):
    model = ControlSulfato
    template_name = "catalogos/ControlSulfato_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'

class ControlSulfatoNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_ControlSulfato"
    model=ControlSulfato
    template_name="catalogos/ControlSulfato_form.html"
    context_object_name = 'obj'
    form_class=ControlSulfatoForm
    success_url= reverse_lazy("catalogos:ControlSulfato_list")
    success_message="Control sulfato ingresado Satisfactoriamente"

class ControlSulfatoEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_ControlSulfato"
    model=ControlSulfato
    template_name="catalogos/ControlSulfato_form.html"
    context_object_name = 'obj'
    form_class=ControlSulfatoForm
    success_url= reverse_lazy("catalogos:ControlSulfato_list")
    success_message="El Control del Sulfato se han actualizado Satisfactoriamente"

class ControlSulfatoDel(LoginRequiredMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "catalogos.delete_OperacionDiaria"
    model=ControlSulfato
    template_name="catalogos/OperacionDiaria_del.html"
    context_object_name = 'obj' 
    success_url= reverse_lazy("catalogos:OperacionDiaria_list")







#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def categoria_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, landscape
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=landscape(letter),
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    categorias = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Categorías", styles['Heading1'])
    categorias.append(header)
    headings = ('nombre', 'Ag Cruda', 'Creación')
    if not pk:
        todascategorias = [(p.descripcion, p.cruda,p.tratada, p.hr_servidas,
            p.hr_sin_servicio,p.ag_cruda_recibida,p.ag_tratada_despachada,
            p.consumo_sulfato,p.consumo_cloro , p.creado)
                           for p in Categoria.objects.all().order_by('pk')]
    else:
        todascategorias = [(p.descripcion, p.cruda,p.tratada, p.hr_servidas,
            p.hr_sin_servicio,p.ag_cruda_recibida,p.ag_tratada_despachada,
            p.consumo_sulfato,p.consumo_cloro , p.activo, p.creado)
                           for p in Categoria.objects.filter(id=pk)]
    
    t = Table([headings] + todascategorias)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    categorias.append(t)
    doc.build(categorias)
    response.write(buff.getvalue())
    buff.close()
    return response

